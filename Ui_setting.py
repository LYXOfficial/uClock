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
        setting.resize(1049, 811)
        font = QtGui.QFont()
        font.setFamily("萍方0")
        font.setPointSize(10)
        setting.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(setting)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 16, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 12, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 17, 0, 1, 1)
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
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 0, 0, 1, 1)
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
        icon.addPixmap(QtGui.QPixmap("e:\\项目\\uClock\\effects/pics/max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon)
        self.toolButton_6.setIconSize(QtCore.QSize(10, 10))
        self.toolButton_6.setObjectName("toolButton_6")
        self.gridLayout_5.addWidget(self.toolButton_6, 0, 3, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 11, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 15, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(setting)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 5, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 14, 0, 1, 1)
        self.menu = QtWidgets.QListWidget(setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("e:\\项目\\uClock\\effects/pics/theme.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("e:\\项目\\uClock\\effects/pics/time.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("e:\\项目\\uClock\\effects/pics/other.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("e:\\项目\\uClock\\effects/pics/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.menu.addItem(item)
        self.gridLayout.addWidget(self.menu, 6, 0, 3, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 13, 0, 1, 1)
        self.view = QtWidgets.QStackedWidget(setting)
        self.view.setObjectName("view")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_2.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 12, 0, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.page_3)
        self.toolButton.setEnabled(False)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 3, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 7, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.page_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 3, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem11, 11, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setEnabled(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.page_3)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 5, 0, 1, 4)
        self.toolButton_2 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_2.setEnabled(False)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_2.addWidget(self.toolButton_2, 7, 3, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.page_3)
        self.doubleSpinBox.setEnabled(False)
        self.doubleSpinBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.doubleSpinBox.setMinimum(0.01)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_2.addWidget(self.doubleSpinBox, 3, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 7, 1, 1, 2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_2.addWidget(self.radioButton_3, 8, 0, 1, 1)
        self.view.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_3.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 2, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setEnabled(False)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.page_4)
        self.dateEdit.setEnabled(False)
        self.dateEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_3.addWidget(self.dateEdit, 3, 1, 2, 3)
        self.label_3 = QtWidgets.QLabel(self.page_4)
        self.label_3.setEnabled(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 2, 1)
        spacerItem12 = QtWidgets.QSpacerItem(255, 170, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem12, 5, 0, 1, 4)
        self.checkBox = SwitchButton(self.page_4)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 1, 0, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.view.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_4.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(255, 139, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem13, 5, 0, 1, 2)
        self.checkBox_2 = SwitchButton(self.page_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_4.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 2, 0, 1, 1)
        self.checkBox_3 = SwitchButton(self.page_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_4.addWidget(self.checkBox_3, 4, 0, 1, 2)
        self.view.addWidget(self.page_2)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_6.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_28 = QtWidgets.QLabel(self.page_6)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 7, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 3, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem14, 8, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.page_6)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 2, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        font.setPointSize(18)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.page_6)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 0, 0, 2, 1)
        self.label_23 = QtWidgets.QLabel(self.page_6)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.gridLayout_6.addWidget(self.label_23, 4, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.page_6)
        self.label_26.setOpenExternalLinks(True)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 5, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.page_6)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 7, 1, 1, 3)
        self.label_27 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_6.addWidget(self.label_27, 6, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.page_6)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 3, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.page_6)
        self.label_24.setOpenExternalLinks(True)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 5, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.page_6)
        self.label_25.setOpenExternalLinks(True)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 5, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.page_6)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 1, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem15, 0, 3, 1, 1)
        self.view.addWidget(self.page_6)
        self.gridLayout.addWidget(self.view, 4, 1, 15, 3)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(setting)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.page_9)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        font.setPointSize(24)
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
        font.setFamily("萍方粗")
        font.setPointSize(24)
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
        font.setFamily("萍方粗")
        font.setPointSize(24)
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
        font.setFamily("萍方粗")
        font.setPointSize(24)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.stackedWidget_2.addWidget(self.page_12)
        self.gridLayout.addWidget(self.stackedWidget_2, 3, 1, 1, 3)
        self.label_10 = QtWidgets.QLabel(setting)
        font = QtGui.QFont()
        font.setFamily("萍方粗")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
    
        self.retranslateUi(setting)
        self.stackedWidget.setCurrentIndex(0)
        self.menu.setCurrentRow(0)
        self.view.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.menu.currentRowChanged['int'].connect(self.view.setCurrentIndex)
        self.radioButton_2.toggled['bool'].connect(self.lineEdit_3.setEnabled)
        self.radioButton_2.toggled['bool'].connect(self.toolButton_2.setEnabled)
        self.checkBox.clicked['bool'].connect(self.label_3.setEnabled)
        self.checkBox.clicked['bool'].connect(self.lineEdit_2.setEnabled)
        self.checkBox.clicked['bool'].connect(self.label_4.setEnabled)
        self.checkBox.clicked['bool'].connect(self.dateEdit.setEnabled)
        self.menu.currentRowChanged['int'].connect(self.stackedWidget_2.setCurrentIndex)
        self.toolButton_4.clicked['bool'].connect(setting.close)
        self.toolButton_5.clicked.connect(setting.showMinimized)
        self.toolButton_3.clicked['bool'].connect(setting.showMaximized)
        self.toolButton_3.clicked.connect(self.toolButton_3.hide)
        self.toolButton_3.clicked.connect(self.toolButton_6.show)
        self.toolButton_6.clicked.connect(self.toolButton_3.show)
        self.toolButton_6.clicked.connect(setting.showNormal)
        self.toolButton_6.clicked.connect(self.toolButton_6.hide)
        QtCore.QMetaObject.connectSlotsByName(setting)

    def retranslateUi(self, setting):
        _translate = QtCore.QCoreApplication.translate
        setting.setWindowTitle(_translate("setting", "设置"))
        self.toolButton_4.setText(_translate("setting", "✕"))
        self.toolButton_3.setText(_translate("setting", "□"))
        self.toolButton_5.setText(_translate("setting", "–"))
        self.label_9.setText(_translate("setting", "   uClock设置"))
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
        self.label_6.setText(_translate("setting", "背景效果设置"))
        self.label_15.setText(_translate("setting", "注意：设置重启后生效！"))
        self.toolButton.setText(_translate("setting", "..."))
        self.radioButton_2.setText(_translate("setting", "设置背景图片"))
        self.comboBox.setItemText(0, _translate("setting", "时钟"))
        self.comboBox.setItemText(1, _translate("setting", "日历"))
        self.comboBox.setItemText(2, _translate("setting", "其它"))
        self.label.setText(_translate("setting", "侧边栏显示内容："))
        self.label_2.setText(_translate("setting", "自定义:(html路径、缩放比例)"))
        self.radioButton.setText(_translate("setting", "使用透明效果（Mica、亚克力或Aero）"))
        self.toolButton_2.setText(_translate("setting", "..."))
        self.radioButton_3.setText(_translate("setting", "不使用任何效果"))
        self.label_4.setText(_translate("setting", "日期设置："))
        self.dateEdit.setDisplayFormat(_translate("setting", "yyyy-M-d"))
        self.label_3.setText(_translate("setting", "倒计时项目："))
        self.checkBox.setText(_translate("setting", "启用倒计时"))
        self.checkBox_2.setText(_translate("setting", "开机自启"))
        self.checkBox_3.setText(_translate("setting", "不测试网络"))
        self.label_28.setText(_translate("setting", "PyQt5\n"
"zhdate\n"
"PyWin32API\n"
"requests"))
        self.label_22.setText(_translate("setting", "Version {}"))
        self.label_19.setText(_translate("setting", "uClock"))
        self.label_18.setText(_translate("setting", "Logo"))
        self.label_26.setText(_translate("setting", "<a href=\"https://space.bilibili.com/369280472\">Bilibili</a href>"))
        self.label_29.setText(_translate("setting", "感谢大佬@之一Yo的众多Fluent解决方案！"))
        self.label_27.setText(_translate("setting", "参考资料及使用第三方库："))
        self.pushButton.setText(_translate("setting", "更新日志"))
        self.label_24.setText(_translate("setting", "<a href=\"https://github.com/lyxofficial\">Github</a href>"))
        self.label_25.setText(_translate("setting", "<a href=\"https://lyxofficial.github.io\">个人博客</a href>"))
        self.label_20.setText(_translate("setting", "By github@lyxofficial"))
        self.label_5.setText(_translate("setting", "外观"))
        self.label_7.setText(_translate("setting", "倒计时"))
        self.label_8.setText(_translate("setting", "其它"))
        self.label_17.setText(_translate("setting", "关于"))
        self.label_10.setText(_translate("setting", "   菜单"))
from switchButton import SwitchButton
