# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\uClock\settingWin11.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setting(object):
    def setupUi(self, setting):
        setting.setObjectName("setting")
        setting.setWindowModality(QtCore.Qt.ApplicationModal)
        setting.resize(1049, 811)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        setting.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(setting)
        self.gridLayout.setContentsMargins(12, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 0, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(self.page)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout_5.addWidget(self.toolButton_4, 0, 4, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self.page)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout_5.addWidget(self.toolButton_3, 0, 2, 1, 1)
        self.toolButton_5 = QtWidgets.QToolButton(self.page)
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout_5.addWidget(self.toolButton_5, 0, 1, 1, 1)
        self.toolButton_6 = QtWidgets.QToolButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_6.sizePolicy().hasHeightForWidth())
        self.toolButton_6.setSizePolicy(sizePolicy)
        self.toolButton_6.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:\\uClock\\effects/pics/max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon)
        self.toolButton_6.setIconSize(QtCore.QSize(10, 10))
        self.toolButton_6.setObjectName("toolButton_6")
        self.gridLayout_5.addWidget(self.toolButton_6, 0, 3, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 3)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(setting)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.page_9)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.stackedWidget_2.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_10)
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.page_10)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.stackedWidget_2.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_11)
        self.horizontalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.page_11)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.stackedWidget_2.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_12)
        self.horizontalLayout_3.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.page_12)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.stackedWidget_2.addWidget(self.page_12)
        self.gridLayout.addWidget(self.stackedWidget_2, 3, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 16, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 9, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(setting)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 12, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 15, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 10, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 13, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(setting)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.menu = QtWidgets.QListWidget(setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("e:\\uClock\\effects/pics/theme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("e:\\uClock\\effects/pics/time.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("e:\\uClock\\effects/pics/other.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("e:\\uClock\\effects/pics/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.menu.addItem(item)
        self.gridLayout.addWidget(self.menu, 6, 0, 3, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 11, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 14, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 5, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 17, 0, 1, 1)
        self.view = QtWidgets.QStackedWidget(setting)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.view.setFont(font)
        self.view.setObjectName("view")
        self.page_3 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.page_3.setFont(font)
        self.page_3.setObjectName("page_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_2.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_2.setVerticalSpacing(14)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_8 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_14.addWidget(self.radioButton_4, 0, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_5.setEnabled(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_14.addWidget(self.radioButton_5, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_8, 8, 1, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_29 = QtWidgets.QLabel(self.groupBox_9)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_4.addWidget(self.label_29)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.checkBox_4 = SwitchButton(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_4.addWidget(self.checkBox_4)
        self.gridLayout_2.addWidget(self.groupBox_9, 6, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.page_3)
        font = QtGui.QFont()
        font.setFamily("萍方0")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setContentsMargins(10, -1, -1, -1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.toolButton = QtWidgets.QToolButton(self.groupBox)
        self.toolButton.setEnabled(False)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_7.addWidget(self.toolButton, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_7.addWidget(self.comboBox, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_7.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 1, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.doubleSpinBox.setMinimum(0.01)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_7.addWidget(self.doubleSpinBox, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 2, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 7, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem12, 9, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 11, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_2.setEnabled(False)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_8.addWidget(self.toolButton_2, 1, 4, 3, 1)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_8.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_8.addWidget(self.radioButton_3, 5, 0, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_8.addWidget(self.lineEdit_3, 1, 2, 3, 2)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_8.addWidget(self.radioButton_2, 2, 0, 1, 2)
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setObjectName("label_28")
        self.gridLayout_8.addWidget(self.label_28, 0, 2, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setMinimum(20)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_8.addWidget(self.horizontalSlider, 0, 3, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_2, 5, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 10, 1, 1, 1)
        self.view.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_3.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_3.addWidget(self.label_34, 1, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(255, 170, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem13, 4, 0, 1, 2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_4)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_11.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_11.addWidget(self.label_3, 1, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_5)
        self.dateEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_11.addWidget(self.dateEdit, 2, 2, 1, 3)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem14, 0, 2, 1, 2)
        self.checkBox = SwitchButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_11.addWidget(self.checkBox, 0, 4, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_11.addWidget(self.lineEdit_2, 1, 2, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_11.addWidget(self.label_4, 2, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem15, 1, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_11.addWidget(self.label_33, 0, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox_5, 3, 0, 1, 2)
        self.label_35 = QtWidgets.QLabel(self.page_4)
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.gridLayout_3.addWidget(self.label_35, 2, 0, 1, 1)
        self.view.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_4.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_9.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_30 = QtWidgets.QLabel(self.groupBox_3)
        self.label_30.setEnabled(False)
        self.label_30.setObjectName("label_30")
        self.gridLayout_9.addWidget(self.label_30, 0, 0, 1, 1)
        self.checkBox_2 = SwitchButton(self.groupBox_3)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_9.addWidget(self.checkBox_2, 0, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem16, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_10.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_31 = QtWidgets.QLabel(self.groupBox_4)
        self.label_31.setObjectName("label_31")
        self.gridLayout_10.addWidget(self.label_31, 0, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem17, 0, 1, 1, 1)
        self.checkBox_3 = SwitchButton(self.groupBox_4)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_10.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_4, 3, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 5, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(255, 139, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem18, 7, 0, 1, 2)
        self.label_32 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout_4.addWidget(self.label_32, 1, 0, 1, 1)
        self.view.addWidget(self.page_2)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_6.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_20 = QtWidgets.QLabel(self.page_6)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.page_6)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 0, 0, 2, 1)
        self.label_21 = QtWidgets.QLabel(self.page_6)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 2, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem19, 5, 1, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.page_6)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.feed = QtWidgets.QPushButton(self.groupBox_6)
        self.feed.setObjectName("feed")
        self.gridLayout_12.addWidget(self.feed, 0, 4, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_12.addWidget(self.label_22, 0, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem20, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_12.addWidget(self.pushButton, 0, 3, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox_6)
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.gridLayout_12.addWidget(self.label_36, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_6, 3, 0, 1, 4)
        self.label_19 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 0, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.page_6)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 1, 2, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem21, 0, 3, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.page_6)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_25 = QtWidgets.QLabel(self.groupBox_7)
        self.label_25.setObjectName("label_25")
        self.gridLayout_13.addWidget(self.label_25, 1, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_7)
        self.label_26.setObjectName("label_26")
        self.gridLayout_13.addWidget(self.label_26, 1, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_7)
        self.label_27.setObjectName("label_27")
        self.gridLayout_13.addWidget(self.label_27, 1, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_13.addWidget(self.label_23, 0, 0, 1, 3)
        self.gridLayout_6.addWidget(self.groupBox_7, 4, 0, 1, 4)
        self.view.addWidget(self.page_6)
        self.gridLayout.addWidget(self.view, 4, 1, 15, 3)

        self.retranslateUi(setting)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.menu.setCurrentRow(0)
        self.view.setCurrentIndex(0)
        self.menu.currentRowChanged['int'].connect(self.view.setCurrentIndex) # type: ignore
        self.checkBox.clicked['bool'].connect(self.label_3.setEnabled) # type: ignore
        self.checkBox.clicked['bool'].connect(self.lineEdit_2.setEnabled) # type: ignore
        self.checkBox.clicked['bool'].connect(self.label_4.setEnabled) # type: ignore
        self.checkBox.clicked['bool'].connect(self.dateEdit.setEnabled) # type: ignore
        self.menu.currentRowChanged['int'].connect(self.stackedWidget_2.setCurrentIndex) # type: ignore
        self.toolButton_4.clicked['bool'].connect(setting.close) # type: ignore
        self.toolButton_5.clicked.connect(setting.showMinimized) # type: ignore
        self.toolButton_3.clicked['bool'].connect(setting.showMaximized) # type: ignore
        self.toolButton_3.clicked.connect(self.toolButton_3.hide) # type: ignore
        self.toolButton_3.clicked.connect(self.toolButton_6.show) # type: ignore
        self.toolButton_6.clicked.connect(self.toolButton_3.show) # type: ignore
        self.toolButton_6.clicked.connect(setting.showNormal) # type: ignore
        self.toolButton_6.clicked.connect(self.toolButton_6.hide) # type: ignore
        self.radioButton_2.clicked['bool'].connect(self.lineEdit_3.setEnabled) # type: ignore
        self.radioButton_2.clicked['bool'].connect(self.toolButton_2.setEnabled) # type: ignore
        self.radioButton_3.clicked['bool'].connect(self.lineEdit_3.setDisabled) # type: ignore
        self.radioButton_3.clicked['bool'].connect(self.toolButton_2.setDisabled) # type: ignore
        self.radioButton.clicked['bool'].connect(self.lineEdit_3.setDisabled) # type: ignore
        self.radioButton.clicked['bool'].connect(self.toolButton_2.setDisabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(setting)

    def retranslateUi(self, setting):
        _translate = QtCore.QCoreApplication.translate
        setting.setWindowTitle(_translate("setting", "uClock 设置"))
        self.toolButton_4.setText(_translate("setting", "✕"))
        self.toolButton_3.setText(_translate("setting", "□"))
        self.toolButton_5.setText(_translate("setting", "–"))
        self.label_5.setText(_translate("setting", "外观"))
        self.label_7.setText(_translate("setting", "倒计时"))
        self.label_8.setText(_translate("setting", "其它"))
        self.label_17.setText(_translate("setting", "关于"))
        self.label_10.setText(_translate("setting", "   菜单"))
        __sortingEnabled = self.menu.isSortingEnabled()
        self.menu.setSortingEnabled(False)
        item = self.menu.item(0)
        item.setText(_translate("setting", "外观"))
        item = self.menu.item(1)
        item.setText(_translate("setting", "倒计时"))
        item = self.menu.item(2)
        item.setText(_translate("setting", "其它"))
        item = self.menu.item(3)
        item.setText(_translate("setting", "关于"))
        self.menu.setSortingEnabled(__sortingEnabled)
        self.radioButton_4.setText(_translate("setting", "窗口"))
        self.radioButton_5.setText(_translate("setting", "小工具"))
        self.label_29.setText(_translate("setting", "使用厚阴影/圆角"))
        self.toolButton.setText(_translate("setting", "..."))
        self.label_2.setText(_translate("setting", "       自定义:(html路径、缩放比例)"))
        self.comboBox.setItemText(0, _translate("setting", "时钟"))
        self.comboBox.setItemText(1, _translate("setting", "日历"))
        self.comboBox.setItemText(2, _translate("setting", "其它"))
        self.label.setText(_translate("setting", "侧边栏显示内容："))
        self.label_37.setText(_translate("setting", "控件显示方式设置"))
        self.label_14.setText(_translate("setting", "侧边栏设置"))
        self.label_6.setText(_translate("setting", "背景效果设置"))
        self.label_15.setText(_translate("setting", "注意：设置重启后生效！"))
        self.toolButton_2.setText(_translate("setting", "..."))
        self.radioButton.setText(_translate("setting", "使用透明效果（Mica、亚克力或Aero）"))
        self.radioButton_3.setText(_translate("setting", "不使用任何效果"))
        self.radioButton_2.setText(_translate("setting", "设置背景图片"))
        self.label_28.setText(_translate("setting", "透明度"))
        self.pushButton_2.setText(_translate("setting", "重启并应用设置"))
        self.label_34.setText(_translate("setting", "倒计时"))
        self.label_3.setText(_translate("setting", "倒计时项目："))
        self.dateEdit.setDisplayFormat(_translate("setting", "yyyy-M-d"))
        self.label_4.setText(_translate("setting", "日期设置："))
        self.label_33.setText(_translate("setting", "启用倒计时"))
        self.label_30.setText(_translate("setting", "开机自启（仅Release支持）"))
        self.label_31.setText(_translate("setting", "不测试网络"))
        self.label_32.setText(_translate("setting", "没啥用的设置"))
        self.label_20.setText(_translate("setting", "By LYX&&TYM stC2025.3"))
        self.label_18.setText(_translate("setting", "Logo"))
        self.feed.setText(_translate("setting", "反馈"))
        self.label_22.setText(_translate("setting", "Version {}"))
        self.pushButton.setText(_translate("setting", "更新日志"))
        self.label_19.setText(_translate("setting", "uClock"))
        self.label_24.setText(_translate("setting", "Build on 2023.12.3"))
        self.label_25.setText(_translate("setting", "<a href=\"https://qoj.fzoi.top/st20250310\">LYX stC2025.3</a>&amp;&amp;<a href=\"https://qoj.fzoi.top/st20250317\">TYM stC2025.3</a><br><a href=\"https://cnblogs.com/zhiyiyo\">ZhiYiYo</a><br><a href=\"https://luogu.com.cn\">Luogu</a><br>FZOIers&amp;&amp;QYC&amp;&amp;WX&amp;&amp;HZL&amp;&amp;CZC&amp;&amp;PYB<br><a href=\"https://www.cqmetro.cn\">重庆轨道交通</a><br><a href=\"https://cnblogs.com\">博客园</a>&amp;&amp;<a href=\"https://google.com\">Google</a>"))
        self.label_26.setText(_translate("setting", "Python 3.8.0 32bit\n"
"PyQt5\n"
"pywin32api\n"
"Requests\n"
"nuitka\n"
"zhdate"))
        self.label_27.setText(_translate("setting", "<a href=\"https://timor.tech\">timor.tech</a><br><a href=\"https://www.ipify.org/\">ipify.org</a><br><a href=\"https://www.seniverse.com\">心知天气</a><br><a href=\"https://hitokoto.cn\">Hitokoto（一言）</a><br><a href=\"https://yisous.xyz\">这个蒟蒻的博客</a>"))
        self.label_23.setText(_translate("setting", "友情赞助及第三方库"))
from switchButton import SwitchButton
