# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\项目\uClock\error.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorShower(object):
    def setupUi(self, ErrorShower):
        ErrorShower.setObjectName("ErrorShower")
        ErrorShower.setWindowModality(QtCore.Qt.ApplicationModal)
        ErrorShower.resize(468, 312)
        font = QtGui.QFont()
        font.setFamily(".PingFang SC0")
        ErrorShower.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(ErrorShower)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(ErrorShower)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 2, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(ErrorShower)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(ErrorShower)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(ErrorShower)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(ErrorShower)
        font = QtGui.QFont()
        font.setFamily(".PingFang SC0")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(ErrorShower)
        font = QtGui.QFont()
        font.setFamily(".PingFang SC0")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 3)

        self.retranslateUi(ErrorShower)
        QtCore.QMetaObject.connectSlotsByName(ErrorShower)

    def retranslateUi(self, ErrorShower):
        _translate = QtCore.QCoreApplication.translate
        ErrorShower.setWindowTitle(_translate("ErrorShower", "崩溃报告"))
        self.pushButton.setText(_translate("ErrorShower", "关闭"))
        self.pushButton_2.setText(_translate("ErrorShower", "反馈给作者..."))
        self.label_3.setText(_translate("ErrorShower", "崩溃原因："))
        self.label_2.setText(_translate("ErrorShower", "❌"))
        self.label.setText(_translate("ErrorShower", "uClock遇到了严重的问题，导致程序崩溃"))
