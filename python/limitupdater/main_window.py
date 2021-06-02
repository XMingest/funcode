# -*- coding: utf-8 -*-
import time
from pathlib import Path

from PySide2 import QtCore
from PySide2.QtGui import QColor, QIcon
from PySide2.QtWidgets import QFileDialog, QMainWindow, QTreeWidgetItem

from limitupdater.limit_xml import LimitXml
from limitupdater.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    current_item_data = None
    limit: LimitXml = None
    logs: list = []

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 获取加载ui后的原始标题
        self.origin_title = self.windowTitle()
        # 结构视图调整
        xml_struct = self.ui.xml_structure
        xml_struct.setColumnWidth(0, 462)
        xml_struct.setColumnWidth(1, 128)
        xml_struct.setColumnWidth(2, 128)
        xml_struct.itemClicked.connect(self.handle_item_click)
        # 导入文件
        self.ui.act_load.triggered.connect(self.handle_load)
        # 提交修改
        self.ui.btn_item_submit.clicked.connect(self.handle_item_submit)
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
        self.logs.append(f'{time.strftime("[%Y-%m-%d %H:%M:%S]"): <32}{message}')
        self.ui.statusbar.showMessage(f'{message}')
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
                        criterion_item.setText(2, criterion_data[2])
                        criterion_item.setTextColor(2, QColor.fromRgb(255, 0, 0))
                        need_expand_algorithm = True
                    algorithm_item.addChild(criterion_item)
                if need_expand_algorithm:
                    xml_struct.expandItem(algorithm_item)
                    need_expand_screen = True
            if need_expand_screen:
                xml_struct.expandItem(screen_item)
        return self

    # 槽
    @QtCore.Slot(QTreeWidgetItem)
    def handle_item_click(self, item: QTreeWidgetItem):
        if item.text(1):
            # 找到当前节点父代关系
            parents = [item]
            while parents[-1]:
                parents.append(parents[-1].parent())
            parents.reverse()
            parents = [parent.text(0) for parent in parents if parent]
            # 找到当前节点对应数据
            self.current_item_data = None
            for parent in parents:
                self.current_item_data = (self.current_item_data[parent]
                                          if self.current_item_data else
                                          self.limit.data[parent])
            if not isinstance(self.current_item_data, list) or len(self.current_item_data) < 3:
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
            self.current_item_data.append(parents)
        return

    @QtCore.Slot()
    def handle_item_submit(self):
        # 检查是否有所更改
        if self.current_item_data:
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
            if self.limit.data:
                self.expand_title(limit_fp)
                self.refresh_xml_struct()
                self.logging('门限文件解析完成')
            else:
                self.logging('门限文件解析失败')
        else:
            self.logging(f'取消门限文件导入')
        return
