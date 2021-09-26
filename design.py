# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mega_Mike\Desktop\layout-main\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(378, 458)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(378, 458))
        MainWindow.setMaximumSize(QtCore.QSize(378, 458))
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(350, 350))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutsPorts = QtWidgets.QHBoxLayout()
        self.horizontalLayoutsPorts.setObjectName("horizontalLayoutsPorts")
        spacerItem = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutsPorts.addItem(spacerItem)
        self.labelPort = QtWidgets.QLabel(self.centralwidget)
        self.labelPort.setMaximumSize(QtCore.QSize(40, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelPort.setFont(font)
        self.labelPort.setObjectName("labelPort")
        self.horizontalLayoutsPorts.addWidget(self.labelPort)
        spacerItem1 = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutsPorts.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayoutsPorts)
        self.horizontalLayoutPortsMain = QtWidgets.QHBoxLayout()
        self.horizontalLayoutPortsMain.setObjectName("horizontalLayoutPortsMain")
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy)
        self.settingsButton.setMinimumSize(QtCore.QSize(10, 20))
        self.settingsButton.setMaximumSize(QtCore.QSize(25, 25))
        self.settingsButton.setBaseSize(QtCore.QSize(20, 20))
        self.settingsButton.setStyleSheet("image: url(:/images/images/settings-gear.png);")
        self.settingsButton.setText("")
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayoutPortsMain.addWidget(self.settingsButton)
        self.selectionWindow = QtWidgets.QComboBox(self.centralwidget)
        self.selectionWindow.setObjectName("selectionWindow")
        self.horizontalLayoutPortsMain.addWidget(self.selectionWindow)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.connectButton.setFont(font)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayoutPortsMain.addWidget(self.connectButton)
        self.verticalLayout.addLayout(self.horizontalLayoutPortsMain)
        self.verticalLayoutMain = QtWidgets.QVBoxLayout()
        self.verticalLayoutMain.setObjectName("verticalLayoutMain")
        self.horizontalLayoutScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalLayoutScrollArea.sizePolicy().hasHeightForWidth())
        self.horizontalLayoutScrollArea.setSizePolicy(sizePolicy)
        self.horizontalLayoutScrollArea.setMinimumSize(QtCore.QSize(320, 140))
        self.horizontalLayoutScrollArea.setMaximumSize(QtCore.QSize(370, 200))
        self.horizontalLayoutScrollArea.setWidgetResizable(True)
        self.horizontalLayoutScrollArea.setObjectName("horizontalLayoutScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 354, 138))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout_2.addWidget(self.verticalScrollBar)
        self.horizontalLayoutScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutMain.addWidget(self.horizontalLayoutScrollArea)
        self.buttons = QtWidgets.QGridLayout()
        self.buttons.setObjectName("buttons")
        self.weighButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weighButton.sizePolicy().hasHeightForWidth())
        self.weighButton.setSizePolicy(sizePolicy)
        self.weighButton.setMinimumSize(QtCore.QSize(150, 70))
        self.weighButton.setBaseSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.weighButton.setFont(font)
        self.weighButton.setStyleSheet("QPushButton{\n"
"  color: black;                     \n"
"  width: 50px;                     \n"
"  height: 10px;                    \n"
"  font-size: 14px;                 \n"
"  font-weight: bold;        \n"
"  border-raduis:10px;                    \n"
"  text-align: center;\n"
"}")
        self.weighButton.setIconSize(QtCore.QSize(150, 50))
        self.weighButton.setObjectName("weighButton")
        self.buttons.addWidget(self.weighButton, 0, 0, 1, 1)
        self.calibButton = QtWidgets.QPushButton(self.centralwidget)
        self.calibButton.setMinimumSize(QtCore.QSize(150, 70))
        self.calibButton.setStyleSheet("QPushButton{\n"
"  color: black;                     \n"
"  width: 75px;                     \n"
"  height: 50px;                    \n"
"  font-size: 14px;                 \n"
"  font-weight: bold;                             \n"
"  text-align: center;\n"
"}")
        self.calibButton.setObjectName("calibButton")
        self.buttons.addWidget(self.calibButton, 0, 1, 1, 1)
        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setMinimumSize(QtCore.QSize(150, 70))
        self.scanButton.setStyleSheet("QPushButton{\n"
"  color: black;                     \n"
"  width: 75px;                     \n"
"  height: 50px;                    \n"
"  font-size: 14px;                 \n"
"  font-weight: bold;                         \n"
"  text-align: center;\n"
"}")
        self.scanButton.setObjectName("scanButton")
        self.buttons.addWidget(self.scanButton, 2, 1, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setMinimumSize(QtCore.QSize(150, 70))
        self.saveButton.setStyleSheet("QPushButton{\n"
"  color: black;                     \n"
"  width: 75px;                     \n"
"  height: 50px;                    \n"
"  font-size: 14px;                 \n"
"  font-weight: bold;                                  \n"
"  text-align: center;\n"
"}")
        self.saveButton.setObjectName("saveButton")
        self.buttons.addWidget(self.saveButton, 2, 0, 1, 1)
        self.verticalLayoutMain.addLayout(self.buttons)
        self.verticalLayout.addLayout(self.verticalLayoutMain)
        self.horizontalLayoutWorkStatus = QtWidgets.QHBoxLayout()
        self.horizontalLayoutWorkStatus.setObjectName("horizontalLayoutWorkStatus")
        self.labelWorkStatus = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelWorkStatus.setFont(font)
        self.labelWorkStatus.setObjectName("labelWorkStatus")
        self.horizontalLayoutWorkStatus.addWidget(self.labelWorkStatus)
        self.lineEditWorkStatus = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWorkStatus.setObjectName("lineEditWorkStatus")
        self.horizontalLayoutWorkStatus.addWidget(self.lineEditWorkStatus)
        self.verticalLayout.addLayout(self.horizontalLayoutWorkStatus)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.settingsButton, self.selectionWindow)
        MainWindow.setTabOrder(self.selectionWindow, self.connectButton)
        MainWindow.setTabOrder(self.connectButton, self.horizontalLayoutScrollArea)
        MainWindow.setTabOrder(self.horizontalLayoutScrollArea, self.weighButton)
        MainWindow.setTabOrder(self.weighButton, self.calibButton)
        MainWindow.setTabOrder(self.calibButton, self.saveButton)
        MainWindow.setTabOrder(self.saveButton, self.scanButton)
        MainWindow.setTabOrder(self.scanButton, self.lineEditWorkStatus)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelPort.setText(_translate("MainWindow", "Порт"))
        self.connectButton.setText(_translate("MainWindow", "Подключиться"))
        self.weighButton.setText(_translate("MainWindow", "Взвешивание"))
        self.calibButton.setText(_translate("MainWindow", "Калибровка"))
        self.scanButton.setText(_translate("MainWindow", "Сканер"))
        self.saveButton.setText(_translate("MainWindow", "Сохранение"))
        self.labelWorkStatus.setText(_translate("MainWindow", "Статус работы"))
import icons