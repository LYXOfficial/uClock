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
        self.label_3 = QtWidgets.QLabel(feedbacker)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textEdit = QtWidgets.QTextEdit(feedbacker)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(feedbacker)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.retranslateUi(feedbacker)
        QtCore.QMetaObject.connectSlotsByName(feedbacker)

    def retranslateUi(self, feedbacker):
        _translate = QtCore.QCoreApplication.translate
        feedbacker.setWindowTitle(_translate("feedbacker", "反馈"))
        self.pushButton_2.setText(_translate("feedbacker", "发送反馈"))
        self.label_3.setText(_translate("feedbacker", "反馈内容："))
        self.textEdit.setPlaceholderText(_translate("feedbacker", "作者建议你去github issue上提交呢..."))
        self.label_2.setText(_translate("feedbacker", "<a href=\"https://github.com/LYXOfficial/uClock/issues\">去Github提交Issue</a href>"))
