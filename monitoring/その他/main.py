#!/usr/bin/python3
# encoding: utf-8

import sys
from PyQt4 import QtGui
from main_window import MainWindow

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
