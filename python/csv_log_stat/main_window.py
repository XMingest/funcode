# -*- coding: utf-8 -*-
import re
import time
from pathlib import Path

import qdarkstyle
from PySide2.QtCore import QSize, Qt, QPoint, Slot
from PySide2.QtGui import QIcon, QMouseEvent
from PySide2.QtWidgets import QMainWindow, QStyle, QFileDialog, QMessageBox, QTreeWidgetItem

from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    # region 属性
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
        # 主题
        self.setMinimumSize(1024, 600)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        # 去掉标题栏
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 最小化关闭图标
        self.ui.btn_exit.setIcon(self.style().standardPixmap(QStyle.SP_TitleBarCloseButton))
        self.ui.btn_show_min.setIcon(self.style().standardPixmap(QStyle.SP_TitleBarMinButton))
        # 表样式
        for i in range(5):
            self.ui.data_table.setColumnWidth(i, 72)
        for i in range(5, 7):
            self.ui.data_table.setColumnWidth(i, 56)
        self.ui.data_table.horizontalHeader().setStretchLastSection(True)
        # 打开目录
        self.ui.btn_open_folder.clicked.connect(self.handle_open_folder)
        # 修改设备装备
        self.ui.device_select.currentIndexChanged.connect(self.handle_device_change)
        self.ui.equip_select.currentIndexChanged.connect(self.handle_equip_change)
        # 选中树节点
        self.ui.data_tree.itemClicked.connect(self.handle_tree_item_click)
        return

    # region 数据处理
    def reinit_data(self):
        """
        重新打开目录时数据清理
        :return:
        """
        self.csv_log_data.clear()
        self.ui.data_table.clear()
        self.ui.data_tree.clear()
        self.ui.device_select.clear()
        self.ui.equip_select.clear()
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
        self.ui.equip_select.addItems(self.csv_log_data[device].keys())
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
            date_item.setText(0, date)
            for station in date_data:
                station_item = QTreeWidgetItem()
                date_item.addChild(station_item)
                station_item.setText(0, station)
        self.ui.data_tree.expandAll()
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
                i += 1
                self.set_process(i * 100 / total_file_n)
            self.ui.device_select.addItems(self.csv_log_data.keys())
            self.logging(f'文件夹{folder}下数据加载完毕')
        return

    @Slot(QTreeWidgetItem)
    def handle_tree_item_click(self, item: QTreeWidgetItem):
        # 子节点状态与其统一
        item.checkState(0)
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
