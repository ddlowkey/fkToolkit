#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Frank.Ding'

import sys
reload(sys)
import os
import re
import json
import time
import subprocess
import threading
import getpass
import locale
import shutil
import stat

sys.setdefaultencoding('utf-8')
rootPath = os.getcwd()
sys.path.append(rootPath)

try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *


class mainWin(QMainWindow):
    def __init__(self, parent=None, **kwargs):
        super(mainWin, self).__init__(parent, **kwargs)
        self.user_setup()
        self.load_config()
        self.setup_ui(parent)
        self.init_style()
        self.init_ui()
        self.init_signal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def setup_ui(self, parent=None):
        self.pt = parent or QMainWindow()
        self.win = assetManager_ui.Ui_MainWindow()
        self.win.setupUi(self.pt)
        size_ = self.pt.size()
        self.resize(size_)
        self.setCentralWidget(self.pt)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle('Example')
        self.setWindowIcon(QIcon(rootPath + '/icon/window_icon.png'))


    def init_signal(self):
	pass

    def init_ui(self):
	pass

    def update_ui(self):
	pass

    def init_style(self):
        self.stylesheet_string = diamond_dark.get_stylesheet()
        self.setStyleSheet(self.stylesheet_string)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mainWin()
    w.show()
    sys.exit(app.exec_())



