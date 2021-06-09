# -*- coding: utf-8 -*-
import csv
import datetime
import re
import time
from pathlib import Path

import qdarkstyle
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QSize, Qt, QPoint, Slot
from PySide2.QtGui import QIcon, QMouseEvent
from PySide2.QtWidgets import QMainWindow, QStyle, QFileDialog, QMessageBox, QTreeWidgetItem, QTableWidgetItem

from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    # region 属性
    chart: QtCharts.QChart = None  # 图标实例
    csv_log_data: dict = {}  # csv文档数据结构化
    logs: list = []  # 用以存储工具运行日志
    mouse_point: QPoint or None = None  # 点击位置以实现移动窗口
    openning_folder: Path or None = None  # 当前打开的目录
    ui: Ui_MainWindow or None = None  # class gen by pyside2-uic

    # endregion

    def __init__(self):
        # 基本加载
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        self.ui = ui
        ui.setupUi(self)
        # 图标
        icon = QIcon()
        icon.addFile('icon.ico', QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        # 添加图表视图
        self.clear_chart()
        # 主题
        self.setMinimumSize(1024, 600)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        # 去掉标题栏
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 最小化关闭图标
        self.ui.btn_exit.setIcon(self.style().standardPixmap(QStyle.SP_TitleBarCloseButton))
        self.ui.btn_show_min.setIcon(self.style().standardPixmap(QStyle.SP_TitleBarMinButton))
        # 表样式
        for i in range(7):
            self.ui.data_table.setColumnWidth(i, 72)
        self.ui.data_table.horizontalHeader().setStretchLastSection(True)
        # 打开目录
        self.ui.btn_open_folder.clicked.connect(self.handle_open_folder)
        # 修改设备装备
        self.ui.device_select.currentIndexChanged.connect(self.handle_device_change)
        self.ui.equip_select.currentIndexChanged.connect(self.handle_equip_change)
        # 选中树节点
        self.ui.data_tree.itemClicked.connect(self.handle_tree_item_click)
        # 处理选中的树节点数据
        self.ui.btn_display_selections.clicked.connect(self.handle_display_selection)
        return

    # region 数据处理
    def clear_chart(self):
        """
        清理图表
        :return:
        """
        try:
            self.ui.data_chart.deleteLater()
        except AttributeError:
            pass
        self.ui.data_chart = QtCharts.QChartView(self)
        self.ui.data_chart_container.addWidget(self.ui.data_chart)
        self.chart = self.ui.data_chart.chart()
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        self.chart.setBackgroundVisible(False)
        return self

    def clear_table(self):
        """
        清理表格
        :return:
        """
        self.ui.data_table.setRowCount(0)
        self.ui.data_table.clearContents()
        return self

    def reinit_data(self):
        """
        重新打开目录时数据清理
        :return:
        """
        self.clear_chart()
        self.clear_table()
        self.csv_log_data.clear()
        self.ui.data_tree.clear()
        self.ui.device_select.clear()
        return self

    # endregion

    # region 日志与提示
    def logging(self, message, level='INFO', use_status_bar=True):
        """
        记录日志
        :param message:
        :param level: 日志等级
        :param use_status_bar: 使用状态栏或者弹窗
        :return:
        """
        dspl_msg = f'[{time.strftime("%Y-%m-%d %H:%M:%S")}]{f"[{level}]":<12}{message}'
        if use_status_bar:
            self.ui.status_bar.showMessage(dspl_msg)
        else:
            QMessageBox.information(self, level, dspl_msg)
        self.logs.append(dspl_msg)
        return self

    def set_process(self, process: float):
        """
        设置进度条显示（0~100）
        :param process:
        :return:
        """
        self.ui.data_loading.setValue(process)
        return self

    # endregion

    # region 槽
    @Slot()
    def handle_device_change(self):
        device = self.ui.device_select.currentText()
        self.ui.equip_select.clear()
        if device and device in self.csv_log_data:
            self.ui.equip_select.addItems(self.csv_log_data[device].keys())
        return

    @Slot()
    def handle_display_selection(self):
        # 获取当前选中项
        csv_total = 0
        csv_paths = []
        for item in self.ui.data_tree.selectedItems():
            if item.parent():
                csv_paths.append((item.parent().text(0), item.csv_path))
                csv_total += 1
        # 获取csv数
        data = {}
        index = 0
        while index < csv_total:
            csv_path = csv_paths[index][1]
            self.set_process(index * 100 / csv_total)
            with open(csv_path, 'r') as csv_fobj:
                reader = csv.reader(csv_fobj)
                # 第一行为表头一，但测试项会重复
                header1 = reader.__next__()
                header2 = reader.__next__()
                if header2[0] == 'LSL':
                    header = header1
                    reader.__next__()
                else:
                    header = [f'{a}.{b}' if b else f'{a}' for (a, b) in zip(header1, header2)]
                for row in reader:
                    csv_data = {k: v for (k, v) in zip(header, row)}
                    actual_date = datetime.datetime.strptime(csv_data['START TIME'][
                                                             :csv_data['START TIME'].index(' ')],
                                                             '%Y/%m/%d')
                    data_item = data.setdefault(csv_data['Vendor'], {}).setdefault(actual_date.strftime('%Y%m%d'), {
                        'bsn': {},
                        'fail_item': {},
                        'fail_times': 0,
                        'times': 0,
                    })
                    # 统计测试次数
                    data_item['times'] += 1
                    if csv_data['RESULT'] == 'PASS':
                        data_item['bsn'].setdefault(csv_data['BSN'], {'f': 0, 'p': 0})['p'] += 1
                    else:
                        data_item['fail_times'] += 1
                        data_item['bsn'].setdefault(csv_data['BSN'], {'f': 0, 'p': 0})['f'] += 1
                        # 失败项
                        try:
                            result_item = csv_data['RESULT_ITEM'].split(':')[2]
                            if result_item.startswith('LSTM_'):
                                result_item = result_item[5:]
                            data_item['fail_item'].setdefault(result_item, 0)
                            data_item['fail_item'][result_item] += 1
                        except (IndexError, KeyError):
                            self.logging(f'csv文件中未识别到失败项数据：{csv_path}')
            index += 1
        # 表格
        data_area = {'dates': set(), 'max_times': 0}
        self.clear_table()
        for vendor, vendor_item in data.items():
            for datitle, date_item in vendor_item.items():
                data_area['dates'].add(datitle)
                tb = self.ui.data_table
                row_index = tb.rowCount()
                tb.insertRow(row_index)
                # 厂商
                tb.setItem(row_index, 0, QTableWidgetItem(vendor))
                # 日期
                tb.setItem(row_index, 1, QTableWidgetItem(datitle))
                # 测试次数
                if data_item['times'] > data_area['max_times']:
                    data_area['max_times'] = data_item['times']
                tb.setItem(row_index, 2, QTableWidgetItem(f'{date_item["times"]}'))
                # 失败次数
                tb.setItem(row_index, 3, QTableWidgetItem(f'{date_item["fail_times"]}'))
                # 误判次数与误判率不良率
                bsn_n = 0
                error_n = 0
                broken_n = 0
                for bsn_item in date_item['bsn'].values():
                    bsn_n += 1
                    if bsn_item['p'] and bsn_item['f']:
                        error_n += 1
                    elif bsn_item['f']:
                        broken_n += 1
                tb.setItem(row_index, 4, QTableWidgetItem(f'{error_n}'))
                tb.setItem(row_index, 5, QTableWidgetItem(f'{error_n / bsn_n:.3%}'))
                tb.setItem(row_index, 6, QTableWidgetItem(f'{broken_n / bsn_n: .3%}'))
                # 失败项
                sorted_fail_items = sorted(date_item['fail_item'].items(), key=lambda item: item[1], reverse=True)
                if len(sorted_fail_items) > 5:
                    sorted_fail_items = sorted_fail_items[:5]
                tb.setItem(row_index, 7,
                           QTableWidgetItem('\n'.join([f'{count: >8} - {item}'
                                                       for (item, count) in sorted_fail_items])))
        self.ui.data_table.resizeRowsToContents()
        # 绘图
        self.clear_chart()
        bar_series = QtCharts.QBarSeries()
        self.chart.addSeries(bar_series)
        # X轴
        date_axis = QtCharts.QBarCategoryAxis()
        self.chart.setAxisX(date_axis, bar_series)
        data_area['dates'] = sorted(data_area['dates'])
        date_axis.append(data_area['dates'])
        date_axis.setGridLineVisible(False)
        # 左侧Y轴
        times_axis = QtCharts.QValueAxis()
        self.chart.setAxisY(times_axis, bar_series)
        times_axis.setRange(0, (data_area['max_times'] // 10 + 2) * 10)
        times_axis.setLabelFormat('%d')
        for vendor, vendor_item in data.items():
            bar_set = QtCharts.QBarSet(vendor)
            bar_series.append(bar_set)
            for datitle in data_area['dates']:
                try:
                    bar_set << vendor_item[f'{datitle}']['times']
                except KeyError:
                    bar_set << 0
        # 进度完成
        self.set_process(100)
        return

    @Slot()
    def handle_equip_change(self):
        try:
            date_items = (self.csv_log_data[self.ui.device_select.currentText()]
                          [self.ui.equip_select.currentText()].items())
        except KeyError:
            return
        self.ui.data_tree.clear()
        for date, date_data in date_items:
            date_item = QTreeWidgetItem()
            self.ui.data_tree.addTopLevelItem(date_item)
            date_item.setSelected(True)
            date_item.setText(0, date)
            for station, station_data in date_data.items():
                station_item = QTreeWidgetItem()
                date_item.addChild(station_item)
                station_item.setSelected(True)
                station_item.setText(0, station)
                station_item.csv_path = station_data['path']
        self.ui.data_tree.expandAll()
        self.ui.data_tree.setFocus()
        return

    @Slot()
    def handle_open_folder(self):
        folder = Path(QFileDialog.getExistingDirectory(self, '请选择日志所在目录'))
        if folder.is_dir():
            self.openning_folder = folder
            self.logging(f'打开文件夹{folder}')
            # 清理上次遗留
            self.reinit_data()
            # 搜索目录下的csv文件
            csv_files = list(folder.glob('**/*.csv'))
            total_file_n = len(csv_files)
            i = 0
            while i < total_file_n:
                csv_file = csv_files[i]
                match = re.match(('(?P<device>[^\-]+)-(?P<equip>\w+)_MediaTest(?P<media>[^_]+)_'
                                  '(?P<station>Station\d)_(?P<date>\d{8})\.csv'), csv_file.name)
                if match:
                    self.csv_log_data.setdefault(
                        match.group('device'), {}).setdefault(
                        match.group('equip'), {}).setdefault(
                        match.group('date'), {}).setdefault(
                        match.group('station'), {'path': csv_file})
                else:
                    self.csv_log_data.setdefault(
                        'unknown', {}).setdefault(
                        'unknown', {}).setdefault(
                        'unknown', {}).setdefault(
                        csv_file.stem, {'path': csv_file})
                i += 1
                self.set_process(i * 100 / total_file_n)
            self.ui.device_select.addItems(self.csv_log_data.keys())
            self.logging(f'文件夹{folder}下数据加载完毕')
        return

    @Slot(QTreeWidgetItem)
    def handle_tree_item_click(self, item: QTreeWidgetItem):
        # 获得当前点击后item状态
        is_selected = item.isSelected()
        # 子节点状态与其统一
        child_index = 0
        while child_index < item.childCount():
            item.child(child_index).setSelected(is_selected)
            child_index += 1
        # 检查父节点
        parent_node = item.parent()
        if parent_node:
            # 如果父节点选中，子节点点击后未选中，那么将父节点置为未选中
            if parent_node.isSelected() and not is_selected:
                parent_node.setSelected(False)
            # 如果父节点未选中，子节点点击后选中，那么检查所有兄弟节点是否都为选中，如是则置为选中
            elif not parent_node.isSelected() and is_selected:
                child_index = 0
                while child_index < parent_node.childCount():
                    if not parent_node.child(child_index).isSelected():
                        break
                    child_index += 1
                else:
                    parent_node.setSelected(True)
        return

    # endregion

    # region 覆盖事件
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        return

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.mouse_point and not self.isMaximized():
            self.move(self.pos() + event.pos() - self.mouse_point)
        return

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.mouse_point = event.pos()
        return

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if self.mouse_point:
            self.mouse_point = None
        return
    # endregion
