# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\项目\uClock\clock.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(434, 284)
        font = QtGui.QFont()
        font.setFamily("黑体")
        Form.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.weatherIcon = QtWidgets.QLabel(Form)
        self.weatherIcon.setText("")
        self.weatherIcon.setObjectName("weatherIcon")
        self.gridLayout.addWidget(self.weatherIcon, 3, 0, 1, 1)
        self.chinese = QtWidgets.QLabel(Form)
        self.chinese.setText("")
        self.chinese.setObjectName("chinese")
        self.gridLayout.addWidget(self.chinese, 2, 0, 1, 1)
        self.view = QtWebEngineWidgets.QWebEngineView(Form)
        self.view.setObjectName("view")
        self.gridLayout.addWidget(self.view, 0, 1, 6, 1)
        self.weather = QtWidgets.QLabel(Form)
        self.weather.setText("")
        self.weather.setObjectName("weather")
        self.gridLayout.addWidget(self.weather, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.time = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.time.setFont(font)
        self.time.setText("")
        self.time.setObjectName("time")
        self.gridLayout.addWidget(self.time, 0, 0, 1, 1)
        self.date = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("萍方0")
        font.setPointSize(16)
        self.date.setFont(font)
        self.date.setText("")
        self.date.setObjectName("date")
        self.gridLayout.addWidget(self.date, 1, 0, 1, 1)
        self.famous = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        self.famous.setFont(font)
        self.famous.setText("")
        self.famous.setAlignment(QtCore.Qt.AlignCenter)
        self.famous.setObjectName("famous")
        self.gridLayout.addWidget(self.famous, 7, 0, 1, 2)
        self.djs = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.djs.setFont(font)
        self.djs.setText("")
        self.djs.setAlignment(QtCore.Qt.AlignCenter)
        self.djs.setObjectName("djs")
        self.gridLayout.addWidget(self.djs, 6, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
from PyQt5 import QtWebEngineWidgets
