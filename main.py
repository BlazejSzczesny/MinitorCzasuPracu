import sys
import platform
from random import random

from PyQt5.QtChart import QPieSeries, QPieSlice, QChart, QChartView
from PyQt5.QtGui import QPen

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import calendar

# GUI FILE

import database
import ui_main
import pyqtgraph as pg

from PyQt5 import QtCore, QtWidgets, uic, QtChart
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        database.dataBase.setDeafultValues(self)

        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint)
        ## SELECT FILE


        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))

        self.ui.label_20.setText("Hello,\n"+self.ui.lineEdit.text())

        ## CALCULATE TIME
        self.ui.pushButton_3.clicked.connect(lambda: UIFunctions.calculateData(self))
        self.ui.pushButton_2.clicked.connect(lambda: UIFunctions.clearData(self))
        self.ui.pushButton.clicked.connect(lambda: UIFunctions.calculateData(self))
        self.ui.pushButton.clicked.connect(lambda: database.dataBase.addDataToDatabase(self))

        self.ui.pushButton_10.clicked.connect(lambda :UIFunctions.pushButton_10_clicked(self))

        self.ui.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.timeEdit.setTime(self.ui.timeEdit_3.time())
        self.ui.timeEdit_2.setTime(self.ui.timeEdit_4.time())

        now = datetime.datetime.now()
        self.ui.comboBox.setCurrentIndex(calendar.monthrange(now.year, now.month)[0]-1)
        self.ui.pushButton_5.clicked.connect(lambda :database.dataBase.calculateStats(self))
        self.ui.label_22.setVisible(False)

        ## User Settings

        self.ui.pushButton_4.clicked.connect(lambda: database.dataBase.UserSerrings(self))
        self.ui.pushButton_4.clicked.connect(lambda: database.dataBase.setDeafultValues(self))

        ## CLOSE & MINIMALIZE & MAXIMIZE

        self.ui.pushButton_6.clicked.connect(lambda :UIFunctions.close(self))
        self.ui.pushButton_7.clicked.connect(lambda :UIFunctions.minimalize(self))
        self.ui.pushButton_9.clicked.connect(lambda :UIFunctions.MAXIMIZE(self))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # PAGE 4
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))


        # User

        self.ui.pushButton_8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        #plot


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.oldPos = self.pos()


        ## ==> END ##



    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
