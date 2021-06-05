# -*- coding: utf-8 -*-
import sys

from PySide2 import QtWidgets

from main_window import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
