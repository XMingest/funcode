# -*- coding: utf-8 -*-
import functools
import sys
import time
from pathlib import Path

import qdarkstyle
from PySide2 import QtCore
from PySide2.QtCore import QSize
from PySide2.QtGui import QColor, QIcon
from PySide2.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QTreeWidgetItem

from limit_xml import LimitXml
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    current_item_data = None
    limit: LimitXml = None
    logs: list = []

    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        self.ui = ui
        ui.setupUi(self)
        # 图标
        try:
            icon = QIcon()
            # sys._MEIPASS为pyinstaller编译为单文件模式后释出资源的路径
            icon.addFile(f'{(Path(sys._MEIPASS) / "icon.ico").resolve()}', QSize(), QIcon.Normal, QIcon.Off)
            self.setWindowIcon(icon)
        except AttributeError:
            self.logging('未找到图标文件')
        # 美化
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        # 获取加载ui后的原始标题
        self.origin_title = self.windowTitle()
        # 结构视图调整
        xml_struct = ui.xml_structure
        xml_struct.setColumnWidth(0, 462)
        xml_struct.setColumnWidth(1, 128)
        xml_struct.setColumnWidth(2, 128)
        xml_struct.itemClicked.connect(self.handle_item_click)
        # 导入文件
        ui.act_load.triggered.connect(self.handle_load)
        # 导出文件
        ui.act_output.triggered.connect(self.handle_output)
        ui.act_xlsx_record.triggered.connect(self.handle_xlsx_record)
        # 提交修改
        ui.btn_item_submit.clicked.connect(self.handle_item_submit)
        # 查看日志
        ui.act_view_log_hist.triggered.connect(self.handle_show_logs)
        # 收紧按钮
        for btn, size in (
            (ui.btn_tighten_002, .002), (ui.btn_tighten_003, .003), (ui.btn_tighten_004, .004),
            (ui.btn_tighten_01, .01), (ui.btn_tighten_05, .05), (ui.btn_tighten5, 5), (ui.btn_tighten10, 10),
            (ui.btn_tighten100, 100),
        ):
            btn.clicked.connect(functools.partial(self.handle_tighten_range, size))
        return

    def expand_title(self, info=None):
        """
        在标题栏附加信息，不可累加
        :param info: 该参数可选，不使用则恢复原有标题
        :return:
        """
        self.setWindowTitle(f'{self.origin_title} - {info}' if info else self.origin_title)
        return self

    def logging(self, message):
        """
        显示日志
        :param message:
        :return:
        """
        self.logs.append(f'{time.strftime("[%Y-%m-%d %H:%M:%S][INFO]"): <32}{message}')
        self.ui.statusbar.showMessage(f'{time.strftime("[%Y-%m-%d %H:%M:%S]")}{message}')
        return self

    def refresh_xml_struct(self):
        """
        刷新xml结构树型视图
        :return:
        """
        # 初始化
        xml_struct = self.ui.xml_structure
        xml_struct.clear()
        for screen, screen_data in self.limit.data.items():
            screen_item = QTreeWidgetItem()
            xml_struct.addTopLevelItem(screen_item)
            screen_item.setText(0, screen)
            need_expand_screen = False
            for algorithm, algorithm_data in screen_data.items():
                algorithm_item = QTreeWidgetItem()
                screen_item.addChild(algorithm_item)
                algorithm_item.setText(0, algorithm)
                need_expand_algorithm = False
                for criterion, criterion_data in algorithm_data.items():
                    criterion_item = QTreeWidgetItem()
                    criterion_item.setText(0, criterion)
                    criterion_item.setText(1, criterion_data[0])
                    # 探测是否有值的修改
                    if criterion_data[2]:
                        # 手动修改置为绿色
                        criterion_item.setText(2, criterion_data[2])
                        criterion_item.setTextColor(2, QColor.fromRgb(0, 255, 0))
                        need_expand_algorithm = True
                    elif criterion_data[1]:
                        # 自动修改置为红色
                        criterion_item.setText(2, criterion_data[1])
                        criterion_item.setTextColor(2, QColor.fromRgb(255, 0, 0))
                        need_expand_algorithm = True
                    algorithm_item.addChild(criterion_item)
                if need_expand_algorithm:
                    xml_struct.expandItem(algorithm_item)
                    need_expand_screen = True
            if need_expand_screen:
                xml_struct.expandItem(screen_item)
        return self

    def warning(self, message):
        """
        显示警告
        :param message:
        :return:
        """
        self.logs.append(f'{time.strftime("[%Y-%m-%d %H:%M:%S][WARN]"): <32}{message}')
        QMessageBox.warning(self, '警告', f'{message}')
        return self

    # TODO: 右键菜单

    # 槽
    @QtCore.Slot(QTreeWidgetItem)
    def handle_item_click(self, item: QTreeWidgetItem):
        if item.text(1):
            # 找到当前节点父代关系
            parents = [item]
            while parents[-1]:
                parents.append(parents[-1].parent())
            parents.pop()
            # 找到当前节点对应数据
            self.current_item_data = None
            while parents:
                parent = parents.pop()
                self.current_item_data = (self.current_item_data[parent.text(0)]
                                          if self.current_item_data else
                                          self.limit.data[parent.text(0)])
            if not isinstance(self.current_item_data, list) or len(self.current_item_data) < 4:
                self.current_item_data = None
                return
            # 数据
            self.ui.auto_range.clear()
            self.ui.origin_range.setText(self.current_item_data[0])
            # 自动
            if self.current_item_data[1]:
                self.ui.auto_range.setText(self.current_item_data[1])
            # 手动
            origin_val = None
            index = 2
            while origin_val is None:
                origin_val = self.current_item_data[index]
                index -= 1
            self.ui.input_range.setText(origin_val)
        return

    @QtCore.Slot()
    def handle_item_submit(self):
        # 检查是否选中某项
        if not self.current_item_data:
            self.logging('未选中测试项')
            return
        # 获得当前值
        origin_val = None
        index = 2
        while origin_val is None:
            origin_val = self.current_item_data[index]
            index -= 1
        # 输入值与
        if origin_val != self.ui.input_range.text():
            self.logging((f'{".".join(self.current_item_data[3])}: '
                          f'{origin_val} -> {self.ui.input_range.text()}'))
            self.current_item_data[2] = self.ui.input_range.text()
            self.refresh_xml_struct()
        return

    @QtCore.Slot()
    def handle_load(self):
        self.logging('正在选择将导入的门限文件')
        limit_fp = Path(QFileDialog.getOpenFileName(self, '导入门限文件', filter='门限文件(*.xml)')[0])
        if limit_fp.is_file():
            self.logging('解析门限文件')
            self.limit = LimitXml(limit_fp)
            # 相关菜单项绑定
            self.ui.act_au_clear.triggered.connect(lambda: (self.limit.clear_auto_update(), self.refresh_xml_struct()))
            self.ui.act_au_exec.triggered.connect(lambda: (self.limit.auto_update(), self.refresh_xml_struct()))
            if self.limit.data:
                self.expand_title(limit_fp)
                self.refresh_xml_struct()
                self.logging('门限文件解析完成')
            else:
                self.warning('门限文件解析失败')
        else:
            self.logging(f'取消门限文件导入')
        return

    @QtCore.Slot()
    def handle_output(self):
        if self.limit is None:
            self.logging('未加载门限文件')
            return
        self.logging('正在导出')
        limit_fp = QFileDialog.getSaveFileName(self, '保存修改后的门限文件至', filter='门限文件(*.xml)')[0]
        if limit_fp:
            try:
                is_same_file = Path(limit_fp).samefile(self.limit.path)
            except FileNotFoundError:
                is_same_file = False
            if is_same_file:
                self.warning('不允许将修改后的门限文件保存至源文件')
                self.logging(f'取消门限文件保存')
                return
            self.limit.write_updated_xml(limit_fp)
            self.logging('导出完毕')
        else:
            self.logging(f'取消门限文件保存')
        return

    @QtCore.Slot()
    def handle_show_logs(self):
        if self.logs:
            QMessageBox.information(self, '查看日志', '\n'.join(self.logs))
        return

    @QtCore.Slot()
    def handle_tighten_range(self, size):
        # 检查是否选中某项
        if not self.current_item_data:
            self.logging('未选中测试项')
            return
        # 收紧门限
        self.limit.tighten_range(self.current_item_data[3], size)
        self.ui.input_range.setText(self.current_item_data[2])
        self.logging((f'{".".join(self.current_item_data[3])}: '
                      f'{self.current_item_data[0]} -> {self.current_item_data[2]}'))
        self.refresh_xml_struct()
        return

    @QtCore.Slot()
    def handle_xlsx_record(self):
        if self.limit is None:
            self.logging('未加载门限文件')
            return
        self.logging('正在导出')
        limit_fp = QFileDialog.getSaveFileName(self, '保存当前修改记录至', filter='记录文件(*.xlsx)')[0]
        if limit_fp:
            try:
                self.limit.record_xlsx(limit_fp)
            except PermissionError:
                self.warning('所选文件无写入权限，可能是已被打开')
                return
            self.logging('导出完毕')
        else:
            self.logging(f'取消记录导出')
        return
