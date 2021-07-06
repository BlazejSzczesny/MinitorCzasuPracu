import PySide2
import numpy as np
import win32con
from PyQt5.QtChart import QPieSeries
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import SubplotParams, Figure

import database
from PyQt5 import QtWidgets, QtGui, QtCore
from main import *
import datetime
import time
import win32gui
import pyqtgraph as pg
from win32api import GetSystemMetrics


class UIFunctions(MainWindow):

    def calculateData(self):
        x = time.strptime(self.ui.timeEdit.text().split(',')[0], '%H:%M')
        y = time.strptime(self.ui.timeEdit_2.text().split(',')[0], '%H:%M')
        s1=datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min).total_seconds()
        s2=datetime.timedelta(hours=y.tm_hour, minutes=y.tm_min).total_seconds()
        if(s2>s1):
            subtraction=s2-s1
        else:
            subtraction = s2-s1+86400
        result=str(datetime.timedelta(seconds=subtraction))[:-3]
        self.ui.label_16.setText(result)


    def clearData(self):
        self.ui.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.timeEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.timeEdit_2.setDateTime(QDateTime.currentDateTime().addSecs(28800))
        self.ui.label_16.setText("0")

    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width()

            maxExtend = maxWidth
            standard = 70

            if width == 70:
                widthExtended = maxExtend

            else:
                widthExtended = standard
                icon = QIcon()
                icon.addFile(u"img/menu.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.Btn_Toggle.setIcon(icon)
                self.ui.Btn_Toggle.setIconSize(QSize(25, 25))
                self.ui.label_20.setText("Hello,\n"+self.ui.lineEdit.text())
                self.ui.btn_page_1.setText("")
                self.ui.btn_page_2.setText("")
                self.ui.btn_page_3.setText("")
                self.ui.btn_page_4.setText("")


            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(PySide2.QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

            if (widthExtended == 200):
                icon = PySide2.QtGui.QIcon()
                icon.addFile(u"img/left-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.Btn_Toggle.setIcon(icon)
                self.ui.Btn_Toggle.setIconSize(QSize(25, 25))
                self.ui.label_20.setText("Hello, "+self.ui.lineEdit.text())
                self.ui.btn_page_1.setText("Home Page")
                self.ui.btn_page_2.setText("Add hours")
                self.ui.btn_page_3.setText("Settings")
                self.ui.btn_page_4.setText("Stats")


    def pushButton_10_clicked(self):
        options = QFileDialog.Options()
        result=""
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",options=options)
        if fileName:
            database.dataBase.insert_image(self,fileName)


    def fadeOut(self):
        label=self.ui.label_22
        label.setVisible(True)
        MainWindow.opacity_effect = QGraphicsOpacityEffect()
        label.setGraphicsEffect(MainWindow.opacity_effect)

        self.a=QPropertyAnimation(MainWindow.opacity_effect, b"opacity")
        self.a.setDuration(4000)
        self.a.setStartValue(1)
        self.a.setEndValue(0)
        self.a.setEasingCurve(PySide2.QtCore.QEasingCurve.InOutQuart)
        self.a.start(QPropertyAnimation.DeleteWhenStopped)


    def close(self):
        self.close()

    def MAXIMIZE(self):
        if (self.height()==GetSystemMetrics(1) and self.width()==GetSystemMetrics(0)):
            #hwnd = win32gui.GetForegroundWindow()
            self.resize(500,500)
            icon2 = QIcon()
            icon2.addFile(u"img/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.pushButton_9.setIcon(icon2)
        else:
            self.setGeometry(0, 0,GetSystemMetrics(0),GetSystemMetrics(1))
            icon2 = QIcon()
            icon2.addFile(u"img/shrink.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.pushButton_9.setIcon(icon2)
            self.ui.pushButton_9.setIconSize(QSize(16, 16))


    def minimalize(self):
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)











