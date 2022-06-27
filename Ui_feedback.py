# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\项目\uClock\feedback.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_feedbacker(object):
    def setupUi(self, feedbacker):
        feedbacker.setObjectName("feedbacker")
        feedbacker.setWindowModality(QtCore.Qt.ApplicationModal)
        feedbacker.resize(399, 318)
        font = QtGui.QFont()
        font.setFamily("萍方0")
        feedbacker.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(feedbacker)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(feedbacker)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(feedbacker)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(feedbacker)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(feedbacker)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.pushButton = QtWidgets.QPushButton(feedbacker)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(feedbacker)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textEdit = QtWidgets.QTextEdit(feedbacker)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(feedbacker)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.retranslateUi(feedbacker)
        self.radioButton_2.clicked['bool'].connect(self.pushButton.setEnabled)
        self.radioButton.clicked['bool'].connect(self.pushButton.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(feedbacker)

    def retranslateUi(self, feedbacker):
        _translate = QtCore.QCoreApplication.translate
        feedbacker.setWindowTitle(_translate("feedbacker", "反馈"))
        self.pushButton_2.setText(_translate("feedbacker", "发送反馈"))
        self.label.setText(_translate("feedbacker", "选择反馈方式"))
        self.radioButton.setText(_translate("feedbacker", "邮箱"))
        self.radioButton_2.setText(_translate("feedbacker", "Github Issue"))
        self.pushButton.setText(_translate("feedbacker", "登录Github"))
        self.label_3.setText(_translate("feedbacker", "反馈内容："))
        self.label_2.setText(_translate("feedbacker", "Github账号：未登录"))
