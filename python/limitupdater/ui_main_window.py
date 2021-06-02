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
        MainWindow.resize(1024, 512)
        self.act_load = QAction(MainWindow)
        self.act_load.setObjectName(u"act_load")
        self.act_output = QAction(MainWindow)
        self.act_output.setObjectName(u"act_output")
        self.act_xlsx_record = QAction(MainWindow)
        self.act_xlsx_record.setObjectName(u"act_xlsx_record")
        self.act_exit = QAction(MainWindow)
        self.act_exit.setObjectName(u"act_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.item_edit = QGridLayout()
        self.item_edit.setObjectName(u"item_edit")
        self.tl_origin = QLabel(self.centralwidget)
        self.tl_origin.setObjectName(u"tl_origin")
        self.tl_origin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.item_edit.addWidget(self.tl_origin, 2, 0, 1, 1)

        self.auto_range = QLabel(self.centralwidget)
        self.auto_range.setObjectName(u"auto_range")

        self.item_edit.addWidget(self.auto_range, 3, 1, 1, 1)

        self.origin_range = QLabel(self.centralwidget)
        self.origin_range.setObjectName(u"origin_range")

        self.item_edit.addWidget(self.origin_range, 2, 1, 1, 1)

        self.tl_auto = QLabel(self.centralwidget)
        self.tl_auto.setObjectName(u"tl_auto")
        self.tl_auto.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.item_edit.addWidget(self.tl_auto, 3, 0, 1, 1)

        self.tl_input = QLabel(self.centralwidget)
        self.tl_input.setObjectName(u"tl_input")
        self.tl_input.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.item_edit.addWidget(self.tl_input, 4, 0, 1, 1)

        self.input_range = QLineEdit(self.centralwidget)
        self.input_range.setObjectName(u"input_range")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_range.sizePolicy().hasHeightForWidth())
        self.input_range.setSizePolicy(sizePolicy)

        self.item_edit.addWidget(self.input_range, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.item_edit)

        self.btn_item_submit = QPushButton(self.centralwidget)
        self.btn_item_submit.setObjectName(u"btn_item_submit")

        self.verticalLayout.addWidget(self.btn_item_submit)

        self.item_edit_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.item_edit_spacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

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
        self.xml_structure.setAnimated(True)
        self.xml_structure.header().setHighlightSections(True)

        self.horizontalLayout.addWidget(self.xml_structure)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 23))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_output = QMenu(self.menu_file)
        self.menu_output.setObjectName(u"menu_output")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menu_file.addAction(self.act_load)
        self.menu_file.addAction(self.menu_output.menuAction())
        self.menu_file.addAction(self.act_exit)
        self.menu_output.addAction(self.act_output)
        self.menu_output.addAction(self.act_xlsx_record)

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
        self.tl_origin.setText(QCoreApplication.translate("MainWindow", u"\u539f\u95e8\u9650", None))
        self.auto_range.setText("")
        self.origin_range.setText("")
        self.tl_auto.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u4fee\u6539", None))
        self.tl_input.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u4fee\u6539", None))
        self.btn_item_submit.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_output.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
    # retranslateUi

