# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\项目\uClock\setting.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setting(object):
    def setupUi(self, setting):
        setting.setObjectName("setting")
        setting.resize(415, 300)
        font = QtGui.QFont()
        font.setFamily("萍方0")
        setting.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(setting)
        self.gridLayout.setObjectName("gridLayout")
        self.menu = QtWidgets.QListWidget(setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("萍方0")
        font.setPointSize(10)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        item = QtWidgets.QListWidgetItem()
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.menu.addItem(item)
        self.gridLayout.addWidget(self.menu, 0, 0, 3, 1)
        self.view = QtWidgets.QStackedWidget(setting)
        self.view.setObjectName("view")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolButton = QtWidgets.QToolButton(self.page_3)
        self.toolButton.setEnabled(False)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 3, 3, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.page_3)
        self.doubleSpinBox.setEnabled(False)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_2.addWidget(self.doubleSpinBox, 3, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.page_3)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_5.addWidget(self.radioButton, 0, 0, 1, 3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_5.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_2.setEnabled(False)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_5.addWidget(self.toolButton_2, 1, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_5.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 4, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 3, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.page_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 8, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setEnabled(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.view.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.page_4)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 3)
        self.dateEdit = QtWidgets.QDateEdit(self.page_4)
        self.dateEdit.setEnabled(False)
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_3.addWidget(self.dateEdit, 2, 1, 2, 3)
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setEnabled(False)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(255, 170, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 4, 0, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.page_4)
        self.label_3.setEnabled(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 2, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 3)
        self.view.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 4, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 5, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(255, 139, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 3, 0, 1, 3)
        self.checkBox_3 = QtWidgets.QCheckBox(self.page_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_4.addWidget(self.checkBox_3, 1, 0, 1, 3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.page_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_4.addWidget(self.checkBox_2, 0, 0, 1, 3)
        self.view.addWidget(self.page_2)
        self.gridLayout.addWidget(self.view, 2, 2, 1, 1)

        self.retranslateUi(setting)
        self.menu.setCurrentRow(0)
        self.view.setCurrentIndex(0)
        self.menu.currentRowChanged['int'].connect(self.view.setCurrentIndex)
        self.radioButton_2.toggled['bool'].connect(self.lineEdit_3.setEnabled)
        self.radioButton_2.toggled['bool'].connect(self.toolButton_2.setEnabled)
        self.checkBox.toggled['bool'].connect(self.label_3.setEnabled)
        self.checkBox.toggled['bool'].connect(self.lineEdit_2.setEnabled)
        self.checkBox.toggled['bool'].connect(self.label_4.setEnabled)
        self.checkBox.toggled['bool'].connect(self.dateEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(setting)

    def retranslateUi(self, setting):
        _translate = QtCore.QCoreApplication.translate
        setting.setWindowTitle(_translate("setting", "设置"))
        __sortingEnabled = self.menu.isSortingEnabled()
        self.menu.setSortingEnabled(False)
        item = self.menu.item(0)
        item.setText(_translate("setting", "外观"))
        item = self.menu.item(1)
        item.setText(_translate("setting", "倒计时"))
        item = self.menu.item(2)
        item.setText(_translate("setting", "其它"))
        self.menu.setSortingEnabled(__sortingEnabled)
        self.toolButton.setText(_translate("setting", "..."))
        self.groupBox.setTitle(_translate("setting", "背景效果设置"))
        self.radioButton.setText(_translate("setting", "使用透明效果（亚克力或Aero或单纯透明）"))
        self.radioButton_2.setText(_translate("setting", "设置背景图片"))
        self.toolButton_2.setText(_translate("setting", "..."))
        self.label.setText(_translate("setting", "侧边栏显示内容："))
        self.comboBox.setItemText(0, _translate("setting", "时钟"))
        self.comboBox.setItemText(1, _translate("setting", "日历"))
        self.comboBox.setItemText(2, _translate("setting", "其它"))
        self.label_2.setText(_translate("setting", "自定义:(html路径、缩放比例)"))
        self.checkBox.setText(_translate("setting", "启用倒计时"))
        self.dateEdit.setDisplayFormat(_translate("setting", "yyyy-M-d"))
        self.label_4.setText(_translate("setting", "日期设置："))
        self.label_3.setText(_translate("setting", "倒计时项目："))
        self.pushButton_2.setText(_translate("setting", "关于软件"))
        self.pushButton_3.setText(_translate("setting", "更新日志"))
        self.pushButton.setText(_translate("setting", "捐助作者！"))
        self.checkBox_3.setText(_translate("setting", "忽略无网络报错"))
        self.checkBox_2.setText(_translate("setting", "开机自启"))
