from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,time,platform
from effects.windowEffecter import WindowEffect
from effects.QFramelessWindow import *
from zhdate import ZhDate as lunar_date
if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.22000-SP0"):
    from Ui_settingWin11 import Ui_setting
else:
    from Ui_settingWin10 import Ui_setting
from Ui_log import Ui_Dialog
import spider
import datetime
import json
from ctypes.wintypes import *
from ctypes import *
from win32.lib import win32con
from win32 import win32gui,win32api
class Settinger(FramelessWindow,Ui_setting):
    BORDER_WIDTH = 5
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("./effects/pics/uclock.png"))
        self.setup()
    def closeEvent(self,event):
        with open("settings.json","w+",encoding="utf-8") as f:
            json.dump(self.setting,f,sort_keys=True, indent=4, separators=(',', ':'))
        self.hide()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and event.y()<=30:
            # self.move(event.globalPos() - self.dragPosition)
            # event.accept()
            self.windowEffect.moveWindow(int(self.winId()))
    def paintEvent(self,event):
        self.pa.begin(self)
        p=QPen()
        p.setStyle(Qt.SolidLine)
        p.setColor(QColor("#66CCFF"))
        p.setWidth(3)
        self.pa.setPen(p)
        self.pa.drawLine(self.menu.x()+4,(self.menu.y()+(self.menu.height()-20)//4*self.menu.row(self.menu.currentItem()))+32,self.menu.x()+4,(self.menu.y()+(self.menu.height()-20)//4*self.menu.row(self.menu.currentItem()))+16)
        self.update()
        self.pa.end()
    #右上角鼠标点不了，这个也不行
    # def mouseReleaseEvent(self,event):
    #     if event.button()==Qt.LeftButton:
    #         desktop = QApplication.desktop()
    #         screenRect = desktop.screenGeometry()
    #         height = screenRect.height()
    #         width = screenRect.width()
    #         print(event.pos())
    #         if event.pos().x()==width and event.pos().y()==height():
    #             self.close()
    def onItem(self,s):
        if self.setting["appearance"]["mode"]=="effect":
            if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.22000-SP0"):
                self.view.currentWidget().setAttribute(Qt.WA_TranslucentBackground)
        self.view.currentWidget().setAutoFillBackground(True)
        for y in range(1000,0,-5):
            op = QGraphicsOpacityEffect()
            op.setOpacity(1-y/1000)
            self.view.currentWidget().setGraphicsEffect(op)
            QApplication.processEvents()
            self.view.currentWidget().setGeometry(0,y//10,self.view.currentWidget().width(),self.view.currentWidget().height())
        self.view.setCurrentIndex(s)
    def showLog(self):
        self.l.show()
    def setup(self):
        self.pa=QPainter()
        self.l=logShower()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.toolButton_6.hide()
        # self.setWindowFlags(Qt.SplashScreen)
        self.setWindowFlags(Qt.CustomizeWindowHint|Qt.WindowMinMaxButtonsHint)
        self.setMouseTracking(True)
        with open("settings.json","r",encoding="utf-8") as f:
            self.setting=json.load(f)
        self.label_18.setPixmap(QPixmap("effects/pics/uclock.png").scaled(QSize(128,128)))
        self.label_22.setText(self.label_22.text().format("1.1"))
        self.dateEdit.setMinimumDate(datetime.datetime.now())
        self.menu.setFrameShape(QListWidget.NoFrame)
        self.checkBox.clicked.connect(lambda:self.setCountdown(self.checkBox.isChecked()))
        self.dateEdit.dateChanged.connect(self.setCountdownDate)
        self.lineEdit_2.textChanged.connect(self.setCountdownThing)
        self.radioButton.toggled.connect(self.setEffect)
        self.radioButton_2.toggled.connect(self.setEffect)
        self.radioButton_3.toggled.connect(self.setEffect)
        self.toolButton_2.clicked.connect(self.getPic)
        self.lineEdit_3.textChanged.connect(self.setPic)
        self.comboBox.currentIndexChanged[str].connect(self.onCom)
        self.toolButton.clicked.connect(self.getHtml)
        self.menu.currentRowChanged[int].connect(self.onItem)
        self.doubleSpinBox.valueChanged.connect(self.setZoomFactor)
        self.checkBox_3.clicked.connect(self.setError)
        self.dateEdit.setDate(datetime.datetime.strptime(self.setting["countdown"]["countdownDay"], '%Y-%m-%d'))
        self.checkBox.setChecked(self.setting["countdown"]["isCountdown"])
        self.lineEdit_2.setText(self.setting["countdown"]["countdownThing"])
        self.lineEdit_3.setText(self.setting["appearance"]["pic"])
        self.lineEdit.setText(self.setting["sidebar"]["html"])
        self.doubleSpinBox.setValue(self.setting["sidebar"]["zoom"])
        self.checkBox_3.setChecked(self.setting["network"]["doNotTraceback"])
        self.pushButton.clicked.connect(self.showLog)
        self.src=QPixmap("effects/pics/avatar.jpg").scaled(64,64)
        radius = min(self.src.width(),self.src.height())
        self.size=QSize(self.src.width(), self.src.height())
        size2=QSize(radius * 2, radius * 2)
        self.mask=QBitmap(self.size)
        self.painter=QPainter(self.mask)
        self.painter.setRenderHints(QPainter.SmoothPixmapTransform)
        self.painter.setRenderHints(QPainter.Antialiasing)
        self.painter.setRenderHints(QPainter.TextAntialiasing)
        self.painter.translate(0, 0)
        self.painter.fillRect(0, 0, self.size.width(), self.size.height(), Qt.white)
        self.painter.setBrush(QColor(0, 0, 0))
        self.painter.drawEllipse(0, 0, self.size.width(), self.size.height())
        self.src.setMask(self.mask)
        self.label_36.setPixmap(self.src)
        if self.setting["sidebar"]["type"]=="clock":
            self.comboBox.setCurrentIndex(0)
        elif self.setting["sidebar"]["type"]=="calendar":
            self.comboBox.setCurrentIndex(1)
        elif self.setting["sidebar"]["type"]=="self":
            self.comboBox.setCurrentIndex(2)
        if self.setting["appearance"]["mode"]=="effect":
            self.radioButton.setChecked(True)
        elif self.setting["appearance"]["mode"]=="pic":
            self.radioButton_2.setChecked(True)
        elif self.setting["appearance"]["mode"]=="no":
            self.radioButton_3.setChecked(True)
        if self.checkBox.isChecked():
            self.label_3.setEnabled(True)
            self.label_4.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.dateEdit.setEnabled(True)
        if self.setting["appearance"]["mode"]=="effect":
            if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.22000-SP0"):
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.windowEffect.setMicaEffect(int(self.winId()))
                self.setStyleSheet(open("effects/settingWin11.qss",encoding="utf-8").read())
                self.label_10.setText("")
            elif "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.19041-SP0"):
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.windowEffect.setAcrylicEffect(int(self.winId()),gradientColor="FFFFFFC9")
                self.setStyleSheet(open("effects/settingWin10.qss",encoding="utf-8").read())
            elif "linux" not in platform.platform().lower() and ("Windows-7" in platform.platform() or "Windows-Vista" in platform.platform()):
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.windowEffect.setAeroEffect(int(self.winId()))
                self.setStyleSheet(open("effects/settingWin10.qss",encoding="utf-8").read())
                self.windowEffect.addShadowEffect(int(self.winId()))
            elif "linux" not in platform.platform().lower() and ("Windows-8" in platform.platform()):
                self.setStyleSheet(open("effects/settingWin10.qss",encoding="utf-8").read())
                self.windowEffect.addShadowEffect(int(self.winId()))
        else:
            if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.22000-SP0"):
                self.setStyleSheet(open("effects/settingWin11.qss",encoding="utf-8").read())
                self.label_10.setText("")
            elif "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.19041-SP0"):
                self.setStyleSheet(open("effects/settingWin10.qss",encoding="utf-8").read())
            elif "linux" not in platform.platform().lower() and ("Windows-7" in platform.platform() or "Windows-Vista" in platform.platform()):
                self.setStyleSheet(open("effects/settingWin10.qss",encoding="utf-8").read())
            elif "linux" not in platform.platform().lower() and ("Windows-8" in platform.platform()):
                self.setStyleSheet(open("effects/settingWin10.qss",encoding="utf-8").read())
            self.windowEffect.addShadowEffect(int(self.winId()))
        self.windowEffect.addWindowAnimation(int(self.winId()))
    def setError(self):
        self.setting["network"]["doNotTraceback"]=self.checkBox_3.isChecked()
    def setZoomFactor(self):
        self.setting["sidebar"]["zoom"]=self.doubleSpinBox.value()
    def onCom(self,text):
        if text=="其它":
            self.label_2.setEnabled(True)
            self.lineEdit.setEnabled(True)
            self.doubleSpinBox.setEnabled(True)
            self.toolButton.setEnabled(True)
            self.setting["sidebar"]["type"]="self"
        elif text=="日历":
            self.label_2.setDisabled(True)
            self.lineEdit.setDisabled(True)
            self.doubleSpinBox.setDisabled(True)
            self.toolButton.setDisabled(True)
            self.setting["sidebar"]["type"]="calendar"
        elif text=="时钟":
            self.label_2.setDisabled(True)
            self.lineEdit.setDisabled(True)
            self.doubleSpinBox.setDisabled(True)
            self.toolButton.setDisabled(True)
            self.setting["sidebar"]["type"]="clock"
    def about(self):
        QMessageBox.about(self,"关于uClock","UCLOCK By LYX\nv1.1\n基于Python3.8与PyQt5构建")
    def setPic(self):
        self.setting["appearance"]["pic"]=self.lineEdit_3.text()
    def getPic(self):
        a,_=QFileDialog.getOpenFileName(self,"选择背景图片","%userprofile%","图片文件(*.png *.jpg *.jpeg)")
        self.lineEdit_3.setText(a)
    def getHtml(self):
        a,_=QFileDialog.getOpenFileName(self,"选择Html","%userprofile%","网页(*.html *.htm)")
        self.lineEdit.setText(a)
        self.setting["sidebar"]["html"]=a

    def setEffect(self):
        if self.radioButton.isChecked():
            self.setting["appearance"]["mode"]="effect"
        elif self.radioButton_2.isChecked():
            self.setting["appearance"]["mode"]="pic"
        elif self.radioButton_3.isChecked():
            self.setting["appearance"]["mode"]="no"
    def setCountdown(self,state):
        self.setting["countdown"]["isCountdown"]=state
    def setCountdownDate(self):
        self.setting["countdown"]["countdownDay"]=self.dateEdit.dateTime().toString("yyyy-MM-dd")
    def setCountdownThing(self):
        self.setting["countdown"]["countdownThing"]=self.lineEdit_2.text()
class logShower(QDialog,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setup()
    def setup(self):
        self.setWindowFlags(Qt.SubWindow)
        self.textBrowser.setText(open("versionLog.txt",encoding="utf-8").read())
        if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.22000-SP0"):
            self.setWindowTitle(" ")
            self.setStyleSheet(open("effects/logWin11.qss",encoding="utf-8").read())
        else:
            self.setWindowTitle("更新日志")
            self.setStyleSheet(open("effects/logWin10.qss",encoding="utf-8").read())
if __name__=="__main__":
    app = QApplication(sys.argv)
    settinged=Settinger()
    settinged.show()
    sys.exit(app.exec_())
