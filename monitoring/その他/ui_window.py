# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 547)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(700, 500))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabPillowSensor = QtGui.QWidget()
        self.tabPillowSensor.setObjectName(_fromUtf8("tabPillowSensor"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tabPillowSensor)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.graphicsView_acc_x = PlotWidget(self.tabPillowSensor)
        self.graphicsView_acc_x.setObjectName(_fromUtf8("graphicsView_acc_x"))
        self.verticalLayout_3.addWidget(self.graphicsView_acc_x)
        self.graphicsView_acc_y = PlotWidget(self.tabPillowSensor)
        self.graphicsView_acc_y.setObjectName(_fromUtf8("graphicsView_acc_y"))
        self.verticalLayout_3.addWidget(self.graphicsView_acc_y)
        self.graphicsView_acc_z = PlotWidget(self.tabPillowSensor)
        self.graphicsView_acc_z.setObjectName(_fromUtf8("graphicsView_acc_z"))
        self.verticalLayout_3.addWidget(self.graphicsView_acc_z)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tabPillowSensor, _fromUtf8(""))
        self.tabBedSensor = QtGui.QWidget()
        self.tabBedSensor.setObjectName(_fromUtf8("tabBedSensor"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tabBedSensor)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.graphicsView_ch1 = PlotWidget(self.tabBedSensor)
        self.graphicsView_ch1.setObjectName(_fromUtf8("graphicsView_ch1"))
        self.verticalLayout_5.addWidget(self.graphicsView_ch1)
        self.graphicsView_ch2 = PlotWidget(self.tabBedSensor)
        self.graphicsView_ch2.setObjectName(_fromUtf8("graphicsView_ch2"))
        self.verticalLayout_5.addWidget(self.graphicsView_ch2)
        self.graphicsView_ch3 = PlotWidget(self.tabBedSensor)
        self.graphicsView_ch3.setObjectName(_fromUtf8("graphicsView_ch3"))
        self.verticalLayout_5.addWidget(self.graphicsView_ch3)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.graphicsView_ch4 = PlotWidget(self.tabBedSensor)
        self.graphicsView_ch4.setObjectName(_fromUtf8("graphicsView_ch4"))
        self.verticalLayout_4.addWidget(self.graphicsView_ch4)
        self.graphicsView_ch5 = PlotWidget(self.tabBedSensor)
        self.graphicsView_ch5.setObjectName(_fromUtf8("graphicsView_ch5"))
        self.verticalLayout_4.addWidget(self.graphicsView_ch5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tabBedSensor, _fromUtf8(""))
        self.tabStatus = QtGui.QWidget()
        self.tabStatus.setObjectName(_fromUtf8("tabStatus"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tabStatus)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.textEdit_status = QtGui.QTextEdit(self.tabStatus)
        self.textEdit_status.setObjectName(_fromUtf8("textEdit_status"))
        self.verticalLayout_6.addWidget(self.textEdit_status)
        self.textEdit_log = QtGui.QTextEdit(self.tabStatus)
        self.textEdit_log.setObjectName(_fromUtf8("textEdit_log"))
        self.verticalLayout_6.addWidget(self.textEdit_log)
        self.tabWidget.addTab(self.tabStatus, _fromUtf8(""))
        self.tabSetting = QtGui.QWidget()
        self.tabSetting.setObjectName(_fromUtf8("tabSetting"))
        self.checkBox_message = QtGui.QCheckBox(self.tabSetting)
        self.checkBox_message.setGeometry(QtCore.QRect(10, 30, 191, 22))
        self.checkBox_message.setAccessibleName(_fromUtf8(""))
        self.checkBox_message.setObjectName(_fromUtf8("checkBox_message"))
        self.pushButton_reset = QtGui.QPushButton(self.tabSetting)
        self.pushButton_reset.setGeometry(QtCore.QRect(20, 130, 161, 27))
        self.pushButton_reset.setObjectName(_fromUtf8("pushButton_reset"))
        self.comboBox_message = QtGui.QComboBox(self.tabSetting)
        self.comboBox_message.setGeometry(QtCore.QRect(40, 60, 141, 27))
        self.comboBox_message.setObjectName(_fromUtf8("comboBox_message"))
        self.comboBox_message.addItem(_fromUtf8(""))
        self.comboBox_message.addItem(_fromUtf8(""))
        self.comboBox_message.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tabSetting, _fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ベッドモニタリングツール", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPillowSensor), _translate("MainWindow", "枕センサ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBedSensor), _translate("MainWindow", "ベッドセンサ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStatus), _translate("MainWindow", "離床モニタリング", None))
        self.checkBox_message.setText(_translate("MainWindow", "担当者へ通知する", None))
        self.pushButton_reset.setText(_translate("MainWindow", "一時情報をリセットする", None))
        self.comboBox_message.setItemText(0, _translate("MainWindow", "電話", None))
        self.comboBox_message.setItemText(1, _translate("MainWindow", "SMS", None))
        self.comboBox_message.setItemText(2, _translate("MainWindow", "Eメール", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSetting), _translate("MainWindow", "設定", None))

from pyqtgraph import PlotWidget
