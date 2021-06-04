# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.act_load = QAction(MainWindow)
        self.act_load.setObjectName(u"act_load")
        self.act_output = QAction(MainWindow)
        self.act_output.setObjectName(u"act_output")
        self.act_xlsx_record = QAction(MainWindow)
        self.act_xlsx_record.setObjectName(u"act_xlsx_record")
        self.act_exit = QAction(MainWindow)
        self.act_exit.setObjectName(u"act_exit")
        self.act_view_log_hist = QAction(MainWindow)
        self.act_view_log_hist.setObjectName(u"act_view_log_hist")
        self.act_au_exec = QAction(MainWindow)
        self.act_au_exec.setObjectName(u"act_au_exec")
        self.act_au_clear = QAction(MainWindow)
        self.act_au_clear.setObjectName(u"act_au_clear")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edit_area = QVBoxLayout()
        self.edit_area.setObjectName(u"edit_area")
        self.item_edit = QGridLayout()
        self.item_edit.setObjectName(u"item_edit")
        self.tl_input = QLabel(self.centralwidget)
        self.tl_input.setObjectName(u"tl_input")
        self.tl_input.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.item_edit.addWidget(self.tl_input, 9, 0, 1, 1)

        self.origin_range = QLabel(self.centralwidget)
        self.origin_range.setObjectName(u"origin_range")

        self.item_edit.addWidget(self.origin_range, 2, 2, 1, 3)

        self.tl_origin = QLabel(self.centralwidget)
        self.tl_origin.setObjectName(u"tl_origin")
        self.tl_origin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.item_edit.addWidget(self.tl_origin, 2, 0, 1, 1)

        self.tl_ttn_tp_spl = QFrame(self.centralwidget)
        self.tl_ttn_tp_spl.setObjectName(u"tl_ttn_tp_spl")
        self.tl_ttn_tp_spl.setFrameShape(QFrame.HLine)
        self.tl_ttn_tp_spl.setFrameShadow(QFrame.Sunken)

        self.item_edit.addWidget(self.tl_ttn_tp_spl, 4, 0, 1, 1)

        self.tl_tighten = QLabel(self.centralwidget)
        self.tl_tighten.setObjectName(u"tl_tighten")
        self.tl_tighten.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.item_edit.addWidget(self.tl_tighten, 5, 0, 3, 1)

        self.item_edit_rt_border = QFrame(self.centralwidget)
        self.item_edit_rt_border.setObjectName(u"item_edit_rt_border")
        self.item_edit_rt_border.setFrameShape(QFrame.VLine)
        self.item_edit_rt_border.setFrameShadow(QFrame.Sunken)

        self.item_edit.addWidget(self.item_edit_rt_border, 2, 6, 8, 1)

        self.tl_ttn_bt_spl = QFrame(self.centralwidget)
        self.tl_ttn_bt_spl.setObjectName(u"tl_ttn_bt_spl")
        self.tl_ttn_bt_spl.setFrameShape(QFrame.HLine)
        self.tl_ttn_bt_spl.setFrameShadow(QFrame.Sunken)

        self.item_edit.addWidget(self.tl_ttn_bt_spl, 8, 0, 1, 1)

        self.auto_range = QLabel(self.centralwidget)
        self.auto_range.setObjectName(u"auto_range")

        self.item_edit.addWidget(self.auto_range, 3, 2, 1, 3)

        self.btn_tighten5 = QPushButton(self.centralwidget)
        self.btn_tighten5.setObjectName(u"btn_tighten5")

        self.item_edit.addWidget(self.btn_tighten5, 7, 2, 1, 1)

        self.tl_auto = QLabel(self.centralwidget)
        self.tl_auto.setObjectName(u"tl_auto")
        self.tl_auto.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.item_edit.addWidget(self.tl_auto, 3, 0, 1, 1)

        self.tl_op_spl = QFrame(self.centralwidget)
        self.tl_op_spl.setObjectName(u"tl_op_spl")
        self.tl_op_spl.setFrameShape(QFrame.VLine)
        self.tl_op_spl.setFrameShadow(QFrame.Sunken)

        self.item_edit.addWidget(self.tl_op_spl, 2, 1, 8, 1)

        self.btn_tighten10 = QPushButton(self.centralwidget)
        self.btn_tighten10.setObjectName(u"btn_tighten10")

        self.item_edit.addWidget(self.btn_tighten10, 7, 3, 1, 1)

        self.btn_tighten100 = QPushButton(self.centralwidget)
        self.btn_tighten100.setObjectName(u"btn_tighten100")

        self.item_edit.addWidget(self.btn_tighten100, 7, 4, 1, 1)

        self.input_range = QLineEdit(self.centralwidget)
        self.input_range.setObjectName(u"input_range")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_range.sizePolicy().hasHeightForWidth())
        self.input_range.setSizePolicy(sizePolicy)

        self.item_edit.addWidget(self.input_range, 9, 2, 1, 2)

        self.btn_item_submit = QPushButton(self.centralwidget)
        self.btn_item_submit.setObjectName(u"btn_item_submit")

        self.item_edit.addWidget(self.btn_item_submit, 9, 4, 1, 1)

        self.tighten_top_spl = QFrame(self.centralwidget)
        self.tighten_top_spl.setObjectName(u"tighten_top_spl")
        self.tighten_top_spl.setFrameShape(QFrame.HLine)
        self.tighten_top_spl.setFrameShadow(QFrame.Sunken)

        self.item_edit.addWidget(self.tighten_top_spl, 4, 2, 1, 3)

        self.tighten_bottom_spl = QFrame(self.centralwidget)
        self.tighten_bottom_spl.setObjectName(u"tighten_bottom_spl")
        self.tighten_bottom_spl.setFrameShape(QFrame.HLine)
        self.tighten_bottom_spl.setFrameShadow(QFrame.Sunken)

        self.item_edit.addWidget(self.tighten_bottom_spl, 8, 2, 1, 3)

        self.btn_tighten_003 = QPushButton(self.centralwidget)
        self.btn_tighten_003.setObjectName(u"btn_tighten_003")

        self.item_edit.addWidget(self.btn_tighten_003, 5, 4, 1, 1)

        self.btn_tighten_004 = QPushButton(self.centralwidget)
        self.btn_tighten_004.setObjectName(u"btn_tighten_004")

        self.item_edit.addWidget(self.btn_tighten_004, 6, 2, 1, 1)

        self.btn_tighten_01 = QPushButton(self.centralwidget)
        self.btn_tighten_01.setObjectName(u"btn_tighten_01")

        self.item_edit.addWidget(self.btn_tighten_01, 6, 3, 1, 1)

        self.btn_tighten_05 = QPushButton(self.centralwidget)
        self.btn_tighten_05.setObjectName(u"btn_tighten_05")

        self.item_edit.addWidget(self.btn_tighten_05, 6, 4, 1, 1)

        self.btn_tighten_002 = QPushButton(self.centralwidget)
        self.btn_tighten_002.setObjectName(u"btn_tighten_002")

        self.item_edit.addWidget(self.btn_tighten_002, 5, 2, 1, 2)


        self.edit_area.addLayout(self.item_edit)

        self.item_edit_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.edit_area.addItem(self.item_edit_spacer)


        self.horizontalLayout.addLayout(self.edit_area)

        self.xml_structure = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(2, u"\u4fee\u6539\u540e");
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setText(1, u"\u539f\u95e8\u9650");
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setText(0, u"\u6d4b\u8bd5\u9879");
        self.xml_structure.setHeaderItem(__qtreewidgetitem)
        self.xml_structure.setObjectName(u"xml_structure")
        self.xml_structure.setFont(font)
        self.xml_structure.setStyleSheet(u"")
        self.xml_structure.setAnimated(True)
        self.xml_structure.header().setHighlightSections(True)

        self.horizontalLayout.addWidget(self.xml_structure)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 27))
        self.menubar.setFont(font)
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_output = QMenu(self.menu_file)
        self.menu_output.setObjectName(u"menu_output")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_auto_update = QMenu(self.menu_edit)
        self.menu_auto_update.setObjectName(u"menu_auto_update")
        self.menu_log = QMenu(self.menubar)
        self.menu_log.setObjectName(u"menu_log")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(16)
        self.statusbar.setFont(font1)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_log.menuAction())
        self.menu_file.addAction(self.act_load)
        self.menu_file.addAction(self.menu_output.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.act_exit)
        self.menu_output.addAction(self.act_output)
        self.menu_output.addAction(self.act_xlsx_record)
        self.menu_edit.addAction(self.menu_auto_update.menuAction())
        self.menu_auto_update.addAction(self.act_au_exec)
        self.menu_auto_update.addAction(self.act_au_clear)
        self.menu_log.addAction(self.act_view_log_hist)

        self.retranslateUi(MainWindow)
        self.act_exit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6781\u5dee\u5408\u5165\u5de5\u5177", None))
        self.act_load.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.act_output.setText(QCoreApplication.translate("MainWindow", u"\u95e8\u9650\u6587\u4ef6", None))
        self.act_xlsx_record.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5f55\u8868\u683c", None))
        self.act_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.act_view_log_hist.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.act_au_exec.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.act_au_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.tl_input.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u4fee\u6539", None))
        self.origin_range.setText("")
        self.tl_origin.setText(QCoreApplication.translate("MainWindow", u"\u539f\u95e8\u9650", None))
        self.tl_tighten.setText(QCoreApplication.translate("MainWindow", u"\u6536\u7d27", None))
        self.auto_range.setText("")
        self.btn_tighten5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.tl_auto.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u4fee\u6539", None))
        self.btn_tighten10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_tighten100.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.btn_item_submit.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.btn_tighten_003.setText(QCoreApplication.translate("MainWindow", u".003", None))
        self.btn_tighten_004.setText(QCoreApplication.translate("MainWindow", u".004", None))
        self.btn_tighten_01.setText(QCoreApplication.translate("MainWindow", u".01", None))
        self.btn_tighten_05.setText(QCoreApplication.translate("MainWindow", u".05", None))
        self.btn_tighten_002.setText(QCoreApplication.translate("MainWindow", u".002", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_output.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_auto_update.setTitle(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u4fee\u6539", None))
        self.menu_log.setTitle(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7", None))
    # retranslateUi

