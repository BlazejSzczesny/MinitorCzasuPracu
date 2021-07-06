# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainltUSSX.ui'
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
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        font = QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"\n"
"QPushButton {\n"
"position: relative;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"border-bottom: 1px solid #B5D5FF;\n"
"border-left: 1px solid;\n"
"border-right: 1px solid;\n"
"border-left-color: #B5D5FF;\n"
"border-image: -webkit-linear-gradient(top, #fff 50%, #B5D5FF 0%) 1 repeat;\n"
"\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u"img/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 8, 8)
        self.frame = QFrame(self.frame_top)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(75, 40))
        self.frame.setMaximumSize(QSize(50, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.frame.setFont(font1)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(107, 107, 107);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"img/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 30))
        self.pushButton_9.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"\n"
"	background-color: rgb(70, 70, 70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"img/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.pushButton_9)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(241, 43, 47);\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"img/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.pushButton_6)


        self.horizontalLayout_3.addWidget(self.frame, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setStyleSheet(u"text-align:left;\n"
"padding-left:12px;")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_top_menus)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	background-repeat: no-repeat;\n"
"	border: 0px solid;\n"
"\n"
"	\n"
"	\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(85, 170, 255);\n"
"border-bottom-left-radius: 7px 7px;\n"
"border-top-left-radius: 7px 7px;\n"
"background-color: rgb(30, 30, 30);\n"
"	margin-right:12px;\n"
"	margin-left:0px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"img/add_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_2.setIcon(icon4)
        self.btn_page_2.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_page_2, 1, 0, 1, 1)

        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setEnabled(True)
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	background-repeat: no-repeat;\n"
"	border: 0px solid;\n"
"\n"
"	\n"
"	\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(85, 170, 255);\n"
"border-bottom-left-radius: 7px 7px;\n"
"border-top-left-radius: 7px 7px;\n"
"background-color: rgb(30, 30, 30);\n"
"	margin-right:12px;\n"
"	margin-left:0px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"img/home_page.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_1.setIcon(icon5)
        self.btn_page_1.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_page_1, 0, 0, 1, 1)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	background-repeat: no-repeat;\n"
"	border: 0px solid;\n"
"\n"
"	\n"
"	\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(85, 170, 255);\n"
"border-bottom-left-radius: 7px 7px;\n"
"border-top-left-radius: 7px 7px;\n"
"background-color: rgb(30, 30, 30);\n"
"	margin-right:12px;\n"
"	margin-left:0px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"img/settings_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_3.setIcon(icon6)
        self.btn_page_3.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_page_3, 2, 0, 1, 1)

        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_4")
        self.btn_page_4.setMinimumSize(QSize(0, 40))
        self.btn_page_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	background-repeat: no-repeat;\n"
"	border: 0px solid;\n"
"\n"
"	\n"
"	\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(85, 170, 255);\n"
"border-bottom-left-radius: 7px 7px;\n"
"border-top-left-radius: 7px 7px;\n"
"background-color: rgb(30, 30, 30);\n"
"	margin-right:12px;\n"
"	margin-left:0px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"img/stats.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_4.setIcon(icon7)
        self.btn_page_4.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_page_4, 3, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.label_20 = QLabel(self.frame_left_menu)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(66, 20))
        self.label_20.setMaximumSize(QSize(200, 16777215))
        font4 = QFont()
        font4.setFamily(u"Sitka")
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_20.setFont(font4)
        self.label_20.setStyleSheet(u"color: rgb(112, 112, 112);")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_20, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pushButton_8 = QPushButton(self.frame_left_menu)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(70, 70))
        self.pushButton_8.setMaximumSize(QSize(70, 70))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(152, 152, 152);\n"
"border:1px solid black;\n"
"margin: 5px;\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(85, 170, 255);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"img/User-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon8)
        self.pushButton_8.setIconSize(QSize(40, 40))
        self.pushButton_8.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.pushButton_8, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_2 = QFrame(self.page_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 26))
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet(u"border:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(47, 0))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_22.setFont(font5)
        self.label_22.setStyleSheet(u"border:none;\n"
"background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 0, 0);\n"
"margin-left:15px;\n"
"margin-right:10px;")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_22)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setContentsMargins(10, 0, 10, -1)
        self.label_11 = QLabel(self.page_1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_4 = QLabel(self.page_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 80))
        self.label_4.setMaximumSize(QSize(80, 80))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: rgb(100, 100, 100);\n"
"	border: 1px solid transparent;\n"
"	border-radius:35px;\n"
"margin:5px\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label_6 = QLabel(self.page_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 80))
        self.label_6.setMaximumSize(QSize(80, 80))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"QLabel{\n"
"background-color: rgb(100, 100, 100);\n"
"	border: 1px solid transparent;\n"
"	border-radius:35px;\n"
"margin:5px\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 2, 1, 1, 1, Qt.AlignHCenter)

        self.label_9 = QLabel(self.page_1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(80, 80))
        self.label_9.setMaximumSize(QSize(16777215, 80))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_5 = QLabel(self.page_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_8 = QLabel(self.page_1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(80, 80))
        self.label_8.setMaximumSize(QSize(80, 80))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"QLabel{\n"
"	border: 1px solid transparent;\n"
"background-color: rgb(100, 100, 100);\n"
"	border-radius:35px;\n"
"margin:5px\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 3, 1, 1, 1, Qt.AlignHCenter)

        self.pushButton_5 = QPushButton(self.page_1)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setMinimumSize(QSize(150, 0))
        self.pushButton_5.setMaximumSize(QSize(150, 16777215))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(15)
        self.pushButton_5.setFont(font6)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	border-radius:15px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 2, 1, 1)

        self.label_10 = QLabel(self.page_1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 80))
        self.label_10.setMaximumSize(QSize(150, 80))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 4, 1, 1, 1)

        self.label_7 = QLabel(self.page_1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.comboBox = QComboBox(self.page_1)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setMinimumSize(QSize(80, 80))
        self.comboBox.setMaximumSize(QSize(200, 80))
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(False)
        font7.setWeight(50)
        font7.setKerning(True)
        self.comboBox.setFont(font7)
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setFocusPolicy(Qt.ClickFocus)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(60, 63, 65);\n"
"border:1px solid rgb(54, 54, 54);\n"
"border-radius:5px;\n"
"margin:5px;\n"
"combobox-popup: 1;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border:1px solid rgb(54, 54, 54);\n"
"}\n"
"QComboBox:focus{\n"
"	background-color: rgb(54, 54, 54);\n"
"	\n"
"	border-color: rgb(0, 170, 255);\n"
"}")
        self.comboBox.setMaxVisibleItems(6)
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_2)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(400, 90))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_3.addWidget(self.label_2, 2, 1, 1, 1)

        self.label_16 = QLabel(self.page_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(80, 80))
        self.label_16.setMaximumSize(QSize(80, 80))
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"QLabel{\n"
"	\n"
"	background-color: rgb(100, 100, 100);\n"
"	border: 1px solid transparent;\n"
"	border-radius:35px;\n"
"margin:5px\n"
"}")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_16, 4, 2, 1, 1, Qt.AlignHCenter)

        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(400, 90))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_3.addWidget(self.label_12, 3, 1, 1, 1)

        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(400, 90))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_3.addWidget(self.label_13, 4, 1, 1, 1)

        self.dateEdit = QDateEdit(self.page_2)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy2.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy2)
        self.dateEdit.setMaximumSize(QSize(150, 16777215))
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet(u"QDateEdit:focus{\n"
"	background-color: rgb(54, 54, 54);\n"
"	\n"
"	border-color: rgb(0, 170, 255);\n"
"}")
        self.dateEdit.setAlignment(Qt.AlignCenter)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(Qt.LocalTime)

        self.gridLayout_3.addWidget(self.dateEdit, 1, 2, 1, 1)

        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 80))
        self.label_14.setMaximumSize(QSize(400, 90))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_3.addWidget(self.label_14, 1, 1, 1, 1)

        self.timeEdit = QTimeEdit(self.page_2)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy2.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy2)
        self.timeEdit.setFont(font)
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.timeEdit.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.timeEdit, 2, 2, 1, 1)

        self.timeEdit_2 = QTimeEdit(self.page_2)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        sizePolicy2.setHeightForWidth(self.timeEdit_2.sizePolicy().hasHeightForWidth())
        self.timeEdit_2.setSizePolicy(sizePolicy2)
        self.timeEdit_2.setFont(font)
        self.timeEdit_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.timeEdit_2, 3, 2, 1, 1)

        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	border-radius:045px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton, 2, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	border-radius:45px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_2, 3, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMaximumSize(QSize(200, 16777215))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	border-radius:45px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_3, 1, 3, 1, 1)

        self.gridLayout_3.setColumnStretch(3, 5)

        self.verticalLayout_6.addLayout(self.gridLayout_3)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_21 = QLabel(self.page_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 50))
        self.label_21.setMaximumSize(QSize(16777215, 50))
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_4.addWidget(self.label_21, 1, 0, 1, 1)

        self.radioButton = QRadioButton(self.page_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(0, 40))
        self.radioButton.setStyleSheet(u"QRadioButton{\n"
"	height:40px;\n"
"	width:50px;\n"
"	background:#c6c6c6;\n"
"	border-radius:20px;\n"
"	border:2px solid #999999;\n"
"\n"
"}\n"
"QRadioButton:hover::unchecked{\n"
"border:2px solid #03a9f4;\n"
"}\n"
"QRadioButton:hover::checked{\n"
"border:2px solid #999999;\n"
"}\n"
"QRadioButton:checked{\n"
"	background:#03a9f4;\n"
"}\n"
"QRadioButton::indicator::unchecked {\n"
"\n"
"height:40px;\n"
"width:50%;\n"
"border-radius:20px;\n"
"    background:#fff;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"	height:40px;\n"
"	width:50%;\n"
"	border-radius:20px;\n"
"	left:56px;\n"
"    background:#fff;\n"
"	\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.radioButton, 0, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.page_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_4.addWidget(self.pushButton_10, 5, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.page_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setMaximumSize(QSize(200, 30))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	border-radius:14px;\n"
"	left:25px;\n"
"	margin-left:auto;\n"
"	margin-right:auto;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_4, 5, 2, 1, 1)

        self.label_23 = QLabel(self.page_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 50))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_4.addWidget(self.label_23, 5, 0, 1, 1)

        self.IMG = QLabel(self.page_3)
        self.IMG.setObjectName(u"IMG")
        self.IMG.setMaximumSize(QSize(250, 220))
        self.IMG.setPixmap(QPixmap(u"img/User-icon.png"))
        self.IMG.setScaledContents(False)
        self.IMG.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.IMG, 1, 2, 3, 1)

        self.lineEdit = QLineEdit(self.page_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(100, 16777215))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border:2px solid #232323;\n"
"\n"
"	color:#fff;\n"
"	border-radius:15px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(54, 54, 54);\n"
"}\n"
"QLineEdit:focus{\n"
"	background-color: rgb(54, 54, 54);\n"
"	\n"
"	border-color: rgb(0, 170, 255);\n"
"}\n"
"")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.timeEdit_3 = QTimeEdit(self.page_3)
        self.timeEdit_3.setObjectName(u"timeEdit_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.timeEdit_3.sizePolicy().hasHeightForWidth())
        self.timeEdit_3.setSizePolicy(sizePolicy3)
        self.timeEdit_3.setFont(font)
        self.timeEdit_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.timeEdit_3, 2, 1, 1, 1)

        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 50))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_4.addWidget(self.label_19, 4, 0, 1, 1)

        self.label_18 = QLabel(self.page_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 50))
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)

        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 2, 1, 1)

        self.label_15 = QLabel(self.page_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 50))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.page_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy3.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy3)
        self.lineEdit_3.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	border:2px solid #232323;\n"
"\n"
"	color:#fff;\n"
"	border-radius:15px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(54, 54, 54);\n"
"}\n"
"QLineEdit:focus{\n"
"	background-color: rgb(54, 54, 54);\n"
"	\n"
"	border-color: rgb(0, 170, 255);\n"
"}")
        self.lineEdit_3.setMaxLength(50)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_3, 4, 1, 1, 1)

        self.timeEdit_4 = QTimeEdit(self.page_3)
        self.timeEdit_4.setObjectName(u"timeEdit_4")
        sizePolicy3.setHeightForWidth(self.timeEdit_4.sizePolicy().hasHeightForWidth())
        self.timeEdit_4.setSizePolicy(sizePolicy3)
        self.timeEdit_4.setFont(font)
        self.timeEdit_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.timeEdit_4, 3, 1, 1, 1)

        self.label_17 = QLabel(self.page_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 50))
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"background-color: rgb(60, 63, 65);\n"
"border-radius:8px;\n"
"margin:5px;")

        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_4)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setMaximumSize(QSize(910, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.page_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.chart_container = QWidget(self.page_4)
        self.chart_container.setObjectName(u"chart_container")

        self.verticalLayout_4.addWidget(self.chart_container)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText("")
        self.pushButton_7.setText("")
        self.pushButton_9.setText("")
        self.pushButton_6.setText("")
        self.btn_page_2.setText("")
        self.btn_page_1.setText("")
        self.btn_page_3.setText("")
        self.btn_page_4.setText("")
        self.label_20.setText("")
        self.pushButton_8.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Podany miesi\u0105c nie posiada danych!", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Aktualny miesi\u0105c:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"W por\u00f3wnaniu z zesz\u0142ym miesi\u0105cu:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tw\u00f3j zarobek:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Poka\u017c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Mniej", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Przepracowane dni:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Stycze\u0144", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Luty", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Marzec", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Kwiecie\u0144", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Maj", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Czerwiec", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Lipiec", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Sierpie\u0144", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Wrzesie\u0144", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Pa\u017adziernik", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Listopad", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Grudzie\u0144", None))

        self.comboBox.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Twoje przepracowane godziny:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Godzina rozpocz\u0119cia pracy:  ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Godzina i data zako\u0144czenia pracy:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Przepracowane godziny:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy.MM.dd", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Wybierz dat\u0119", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Dodaj godziny", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Policz godziny", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Podaj swoje imi\u0119:", None))
        self.radioButton.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Wybierz swoje zdj\u0119cie", None))
        self.IMG.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Stawka godzinowa (w z\u0142)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Domy\u015blna godzina zako\u0144czenia pracy", None))
        self.label.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Zastosuj wybrane ustawienia", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Domy\u015blna godzina rozpocz\u0119cia pracy", None))
    # retranslateUi

