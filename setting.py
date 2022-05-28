from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,time
from effects.windowEffecter import WindowEffect
from zhdate import ZhDate as lunar_date
from Ui_setting import Ui_setting
import spider
import datetime
import platform
import json
class Settinger(QWidget,Ui_setting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("./setting.png"))
        self.setup()
    def closeEvent(self,event):
        with open("settings.json","w+",encoding="utf-8") as f:
            json.dump(self.setting,f)
        self.hide()
    def setup(self):
        with open("settings.json","r",encoding="utf-8") as f:
            self.setting=json.load(f)
        self.dateEdit.setMinimumDate(datetime.datetime.now())
        self.checkBox.toggled.connect(lambda:self.setCountdown(self.checkBox.isChecked()))
        self.dateEdit.dateChanged.connect(self.setCountdownDate)
        self.lineEdit_2.textChanged.connect(self.setCountdownThing)
        self.radioButton.toggled.connect(self.setEffect)
        self.radioButton_2.toggled.connect(self.setEffect)
        self.toolButton_2.clicked.connect(self.getPic)
        self.lineEdit_3.textChanged.connect(self.setPic)
        self.pushButton_2.clicked.connect(self.about)
        self.dateEdit.setDate(datetime.datetime.strptime(self.setting["countdown"]["countdownDay"], '%Y-%m-%d'))
        self.checkBox.setChecked(self.setting["countdown"]["isCountdown"])
        self.lineEdit_2.setText(self.setting["countdown"]["countdownThing"])
        self.lineEdit_3.setText(self.setting["appearance"]["pic"])
        if self.setting["appearance"]["mode"]=="effect":
            self.radioButton.setChecked(True)
        elif self.setting["appearance"]["mode"]=="pic":
            self.radioButton_2.setChecked(True)
        self.windowEffect = WindowEffect()
        if self.setting["appearance"]["mode"]=="effect":
            if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.15063-SP0"):
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.windowEffect.setAcrylicEffect(int(self.winId()))  
                self.menu.setFrameShape(QListWidget.NoFrame)
                self.menu.setStyleSheet("""
QListView {
    outline: none;
}

#menu::item {
    background-color: #ffffff;
    color: #000000;
    border: transparent;
    border-bottom: 1px solid #dbdbdb;
    padding: 8px;
}

#menu::item:hover {
    background-color: #f5f5f5;
}

#menu::item:selected {
    border-left: 5px solid #777777;
}
}""")
                self.windowEffect.setAcrylicEffect(int(self.menu.winId()))
    def about(self):
        QMessageBox.about(self,"关于uClock","UCLOCK By LYX\nv0.3\n基于Python3.8与PyQt5构建")
    def setPic(self):
        self.setting["appearance"]["pic"]=self.lineEdit_3.text()
    def getPic(self):
        a,_=QFileDialog.getOpenFileName(self,"选择背景图片","%userprofile%","图片文件(*.png *.jpg *.jpeg)")
        self.lineEdit_3.setText(a)
    def setEffect(self):
        if self.radioButton.isChecked():
            self.setting["appearance"]["mode"]="effect"
        elif self.radioButton_2.isChecked():
            self.setting["appearance"]["mode"]="pic"
    def setCountdown(self,state):
        self.setting["countdown"]["isCountdown"]=state
    def setCountdownDate(self):
        self.setting["countdown"]["countdownDay"]=self.dateEdit.dateTime().toString("yyyy-MM-dd")
    def setCountdownThing(self):
        self.setting["countdown"]["countdownThing"]=self.lineEdit_2.text()
if __name__=="__main__":
    app = QApplication(sys.argv)
    settinged=Settinger()
    settinged.show()
    sys.exit(app.exec_())