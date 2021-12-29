# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
        MainWindow.resize(671, 299)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_get_nombre = QPushButton(self.centralwidget)
        self.pushButton_get_nombre.setObjectName(u"pushButton_get_nombre")

        self.gridLayout.addWidget(self.pushButton_get_nombre, 0, 3, 1, 1)

        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.gridLayout.addWidget(self.lcdNumber, 2, 2, 1, 2)

        self.label_hz = QLabel(self.centralwidget)
        self.label_hz.setObjectName(u"label_hz")
        font = QFont()
        font.setPointSize(24)
        self.label_hz.setFont(font)

        self.gridLayout.addWidget(self.label_hz, 1, 0, 1, 1)

        self.lineEdit_nombre = QLineEdit(self.centralwidget)
        self.lineEdit_nombre.setObjectName(u"lineEdit_nombre")

        self.gridLayout.addWidget(self.lineEdit_nombre, 0, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(32)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setMinimum(1)
        self.dial.setMaximum(100)

        self.gridLayout.addWidget(self.dial, 1, 2, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 671, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test Snap7", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.pushButton_get_nombre.setText(QCoreApplication.translate("MainWindow", u"Get", None))
        self.label_hz.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"i", None))
    # retranslateUi

