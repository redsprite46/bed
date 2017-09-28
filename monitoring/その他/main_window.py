#!/usr/bin/python3
# encoding: utf-8

from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_window import Ui_MainWindow
import pyqtgraph as pg
import numpy as np
import redis
import classifier
import requests
from twilio_wrapper import TwilioWrapper
# from mysql_wrapper import MySQLWrapper


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.x_ = np.arange(0.0, 10.0, 0.02)
        self.acc_ = np.zeros((3, 500), dtype=np.float)
        self.piezo_ = np.zeros((5, 500), dtype=np.float)
        self.redis_ = redis.Redis(host='192.168.60.1', port=6379)
        self.redis_.flushdb()

        self.counter20_ = 0
        self.classifier_ = classifier.Classifier()
        self.log_ = ''
        # self.mysql_wrapper_ = MySQLWrapper()

        self.graphicsView_acc_x.setYRange(-2.0, 4.0)
        self.graphicsView_acc_y.setYRange(-2.0, 4.0)
        self.graphicsView_acc_z.setYRange(-2.0, 4.0)
        self.graphicsView_acc_x.setTitle("枕加速度センサ x方向")
        self.graphicsView_acc_y.setTitle("枕加速度センサ y方向")
        self.graphicsView_acc_z.setTitle("枕加速度センサ z方向")
        self.graphicsView_acc_x.setLabel(axis='left', units='G')
        self.graphicsView_acc_y.setLabel(axis='left', units='G')
        self.graphicsView_acc_z.setLabel(axis='left', units='G')
        self.graphicsView_ch1.setYRange(-5.0, 5.0)
        self.graphicsView_ch2.setYRange(-5.0, 5.0)
        self.graphicsView_ch3.setYRange(-5.0, 5.0)
        self.graphicsView_ch4.setYRange(-5.0, 5.0)
        self.graphicsView_ch5.setYRange(-5.0, 5.0)
        self.graphicsView_ch1.setTitle("ベッド荷重センサ ch1 (左肩)")
        self.graphicsView_ch2.setTitle("ベッド荷重センサ ch2 (右肩)")
        self.graphicsView_ch3.setTitle("ベッド荷重センサ ch3 (左足)")
        self.graphicsView_ch4.setTitle("ベッド荷重センサ ch4 (右足)")
        self.graphicsView_ch5.setTitle("ベッド荷重センサ ch5 (腰)")
        self.graphicsView_ch1.setLabel(axis='left', units='V')
        self.graphicsView_ch2.setLabel(axis='left', units='V')
        self.graphicsView_ch3.setLabel(axis='left', units='V')
        self.graphicsView_ch4.setLabel(axis='left', units='V')
        self.graphicsView_ch5.setLabel(axis='left', units='V')
        self.pushButton_reset.clicked.connect(self.reset)
        # self.checkBox_patlite.stateChanged.connect(self.patlite_state_changed)

        self.timer_ = pg.QtCore.QTimer()
        self.timer_.timeout.connect(self.update)
        self.timer_.start(50)

    def update(self):
        self.update_acc_wave()
        self.update_piezo_wave()

        self.counter20_ += 1
        self.counter20_ %= 20
        if self.counter20_ == 0:
            self.update_classifier()
            self.update_message()
            self.update_patlite()
            self.update_server()
            self.textEdit_log.setPlainText(self.log_)

    def update_acc_wave(self):
        data_len = self.redis_.llen('monitor_acc')
        if data_len > 0:
            # data_len is assured to be less than or equal to 500
            for i in range(3):
                self.acc_[i][0:500 - data_len] = self.acc_[i][data_len:500]

            for j in range(data_len):
                data = self.redis_.lpop('monitor_acc')
                if data is None:
                    next
                data = data.decode('utf-8').split(':')
                for i in range(3):
                    acc = int(data[3 + i])
                    acc = 6.0 * acc / 1023.0 - 2.0
                    self.acc_[i][500 - data_len + j] = acc

        self.graphicsView_acc_x.plot(
            self.x_, self.acc_[0], pen='y', clear=True)
        self.graphicsView_acc_y.plot(
            self.x_, self.acc_[1], pen='y', clear=True)
        self.graphicsView_acc_z.plot(
            self.x_, self.acc_[2], pen='y', clear=True)

    def update_piezo_wave(self):
        data_len = self.redis_.llen('monitor_piezo')
        if data_len > 0:
            # data_len is assured to be less than or equal to 500
            for i in range(5):
                self.piezo_[i][0:500 - data_len] = self.piezo_[i][data_len:500]

            for j in range(data_len):
                data = self.redis_.lpop('monitor_piezo')
                if data is None:
                    next
                data = data.decode('utf-8').split(':')
                for i in range(5):
                    piezo = int(data[3 + i])
                    piezo = piezo / 1023.0 * 10 - 5.0
                    self.piezo_[i][500 - data_len + j] = piezo

        self.graphicsView_ch1.plot(
            self.x_, self.piezo_[0], pen='y', clear=True)
        self.graphicsView_ch2.plot(
            self.x_, self.piezo_[1], pen='y', clear=True)
        self.graphicsView_ch3.plot(
            self.x_, self.piezo_[2], pen='y', clear=True)
        self.graphicsView_ch4.plot(
            self.x_, self.piezo_[3], pen='y', clear=True)
        self.graphicsView_ch5.plot(
            self.x_, self.piezo_[4], pen='y', clear=True)

    def update_classifier(self):
        self.classifier_.classify()

        state = self.redis_.get('prediction')
        if state is None:
            return
        state = state.decode('utf-8')

        stylesheet = 'font-size:100px;font-style:bold;'
        statustext = ''
        if state in ['a', 'b', 'c']:
            stylesheet += 'color:white;background-color:blue;'
            statustext += '就寝中'
        elif state in ['d', 'e', 'f']:
            stylesheet += 'color:black;background-color:yellow;'
            statustext += '離床行動中'
        else:
            stylesheet += 'color:white;background-color:red;'
            statustext += '離床'

        self.textEdit_status.setStyleSheet(stylesheet)
        self.textEdit_status.setPlainText(statustext)

        '''
        img = ''
        if state in ['a', 'b', 'c']:
            img = 'x'
        elif state in ['d', 'e', 'f']:
            img = 'y'
        else:
            img = 'z'
        pixmap = QtGui.QPixmap()
        pixmap.load('/home/ub/scope/image/' + img + '.jpg')
        self.scene_state_ = QtGui.QGraphicsScene(self)
        item = QtGui.QGraphicsPixmapItem(pixmap)
        self.scene_state_.addItem(item)
        self.graphicsView_state.setScene(self.scene_state_)
        '''

        if self.checkBox_message.isChecked():
            if state in ['d', 'e', 'f']:
                if self.redis_.get('inform_moving') is None:
                    self.redis_.set('inform_moving', 'on')
            if state == 'g':
                if self.redis_.get('inform_left') is None:
                    self.redis_.set('inform_left', 'on')

    def update_message(self):
        if not self.checkBox_message.isChecked():
            return

        inform = None

        moving = self.redis_.get('inform_moving')
        if moving:
            moving = moving.decode('utf-8')
            if moving == 'on':
                inform = 'moving'
                self.redis_.set('inform_moving', 'done')

        if inform is None:
            left = self.redis_.get('inform_left')
            if left:
                left = left.decode('utf-8')
                if left == 'on':
                    inform = 'left'
                    self.redis_.set('inform_left', 'done')

        if inform is None:
            return

        if inform == 'moving':
            self.log_ += "離床行動中：担当者へ通知されます。\n"
        elif inform == 'left':
            self.log_ += "離床：担当者へ通知されます。\n"
        self.textEdit_log.setPlainText(self.log_)

        messenger = TwilioWrapper()

        index = self.comboBox_message.currentIndex()
        if index == 0:
            # phone
            messenger.call_phone(inform)
        elif index == 1:
            # SMS
            messenger.send_sms(inform)
        else:
            # Email
            messenger.send_email(inform)

    def update_server(self):
        # if not self.checkBox_server.isChecked():
        #     return

        bed_color = None
        pillow_color = None

        pred = self.redis_.get('prediction')
        if pred is not None:
            pred = pred.decode('utf-8')
            if pred in ['a', 'b', 'c']:
                bed_color = 'blue'
            elif pred in ['d', 'e', 'f']:
                bed_color = 'yellow'

        patlite = self.redis_.get('patlite_status')
        if patlite is not None:
            patlite = patlite.decode('utf-8')
            if patlite == 'red':
                pillow_color = 'red'
                self.redis_.set('patlite_status', 'off')

        path = 'http://sansa.cs.shinshu-u.ac.jp/akita/MMRK/live.php'
        mamoru_id = '2001'
        ver = '1'
        boot = '1'
        post_path = path + "?ID=" + mamoru_id + "&VER=" + ver + "&BOOT=" + boot
        payload = {'ID': '2001', 'VER': '1', 'BOOT': '1'}

        if bed_color is None and pillow_color is None:
            return

        if bed_color is not None:
            payload['BED'] = bed_color

        if pillow_color is not None:
            payload['PIL'] = pillow_color

        r = requests.post(post_path, params=payload)
        print(r.text)

    def update_patlite(self):
        pass
        # query_result = self.mysql_wrapper_.query_mamoru_enabled()
        # if query_result:
        #     self.redis_.set('mamoru_enabled', 'on')
        # else:
        #     self.redis_.set('mamoru_enabled', 'off')

    def reset(self):
        self.redis_.flushdb()
        self.log_ = ''
        if self.classifier_:
            self.classifier_.reset()

    def patlite_state_changed(self, state):
        pass
        # if self.checkBox_patlite.isChecked():
        #     self.redis_.set('mamoru_enabled', 'on')
        # else:
        #     self.redis_.set('mamoru_enabled', 'off')
