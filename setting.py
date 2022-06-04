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
from ctypes.wintypes import MSG
from win32.lib import win32con
class Settinger(QWidget,Ui_setting):
    BORDER_WIDTH = 5
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("./effects/setting.png"))
        self.setup()
    def closeEvent(self,event):
        with open("settings.json","w+",encoding="utf-8") as f:
            json.dump(self.setting,f,sort_keys=True, indent=4, separators=(',', ':'))
        self.hide()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and event.y()<=25:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and event.y()<=25:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
    def nativeEvent(self, eventType, message):
        """ 处理 Windows 消息 """
        msg = MSG.from_address(message.__int__())
        if msg.message == win32con.WM_NCHITTEST:
            pos = QCursor.pos()
            xPos = pos.x() - self.x()
            yPos = pos.y() - self.y()
            w, h = self.width(), self.height()
            lx = xPos < self.BORDER_WIDTH
            rx = xPos > w - self.BORDER_WIDTH
            ty = yPos < self.BORDER_WIDTH
            by = yPos > h - self.BORDER_WIDTH
            if lx and ty:
                return True, win32con.HTTOPLEFT
            elif rx and by:
                return True, win32con.HTBOTTOMRIGHT
            elif rx and ty:
                return True, win32con.HTTOPRIGHT
            elif lx and by:
                return True, win32con.HTBOTTOMLEFT
            elif ty:
                return True, win32con.HTTOP
            elif by:
                return True, win32con.HTBOTTOM
            elif lx:
                return True, win32con.HTLEFT
            elif rx:
                return True, win32con.HTRIGHT
        # if msg.message == win32con.WM_NCCALCSIZE:
        #     if self.isWindowMaximized(msg.hWnd):
        #         self.monitorNCCALCSIZE(msg)
        #     return True, 0
        # elif msg.message == win32con.WM_GETMINMAXINFO:
        #     if self.isWindowMaximized(msg.hWnd):
        #         window_rect = win32gui.GetWindowRect(msg.hWnd)
        #         if not window_rect:
        #             return False, 0

        #         # 获取显示器句柄
        #         monitor = win32api.MonitorFromRect(window_rect)
        #         if not monitor:
        #             return False, 0

        #         # 获取显示器信息
        #         monitor_info = win32api.GetMonitorInfo(monitor)
        #         monitor_rect = monitor_info['Monitor']
        #         work_area = monitor_info['Work']

        #         # 将 lParam 转换为 MINMAXINFO 指针
        #         info = cast(msg.lParam, POINTER(MINMAXINFO)).contents

        #         # 调整窗口大小
        #         info.ptMaxSize.x = work_area[2] - work_area[0]
        #         info.ptMaxSize.y = work_area[3] - work_area[1]
        #         info.ptMaxTrackSize.x = info.ptMaxSize.x
        #         info.ptMaxTrackSize.y = info.ptMaxSize.y

        #         # 修改左上角坐标
        #         info.ptMaxPosition.x = abs(window_rect[0] - monitor_rect[0])
        #         info.ptMaxPosition.y = abs(window_rect[1] - monitor_rect[1])
        #         return True, 1
        return QWidget.nativeEvent(self, eventType, message)
    def setup(self):
        self.setWindowFlags(Qt.ToolTip)
        #self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setMouseTracking(True)
        with open("settings.json","r",encoding="utf-8") as f:
            self.setting=json.load(f)
        self.toolButton_4.clicked.connect(self.close)
        self.dateEdit.setMinimumDate(datetime.datetime.now())
        self.menu.setFrameShape(QListWidget.NoFrame)
        self.checkBox.toggled.connect(lambda:self.setCountdown(self.checkBox.isChecked()))
        self.dateEdit.dateChanged.connect(self.setCountdownDate)
        self.lineEdit_2.textChanged.connect(self.setCountdownThing)
        self.radioButton.toggled.connect(self.setEffect)
        self.radioButton_2.toggled.connect(self.setEffect)
        self.toolButton_2.clicked.connect(self.getPic)
        self.lineEdit_3.textChanged.connect(self.setPic)
        self.pushButton_2.clicked.connect(self.about)
        self.comboBox.currentIndexChanged[str].connect(self.onCom)
        self.toolButton.clicked.connect(self.getHtml)
        self.doubleSpinBox.valueChanged.connect(self.setZoomFactor)
        self.checkBox_3.stateChanged.connect(self.setError)
        self.dateEdit.setDate(datetime.datetime.strptime(self.setting["countdown"]["countdownDay"], '%Y-%m-%d'))
        self.checkBox.setChecked(self.setting["countdown"]["isCountdown"])
        self.lineEdit_2.setText(self.setting["countdown"]["countdownThing"])
        self.lineEdit_3.setText(self.setting["appearance"]["pic"])
        self.lineEdit.setText(self.setting["sidebar"]["html"])
        self.doubleSpinBox.setValue(self.setting["sidebar"]["zoom"])
        self.checkBox_3.setChecked(self.setting["network"]["doNotTraceback"])
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
        self.windowEffect = WindowEffect()
        # self.windowEffect.setShadowEffect(int(self.winId()))
        if self.setting["appearance"]["mode"]=="effect":
            if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.15063-SP0"):
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.windowEffect.setAcrylicEffect(int(self.winId()),gradientColor="FFFFFFC9")
            elif "linux" not in platform.platform().lower() and (platform.platform()=="Windows-7" and platform.platform()<"Windows-8"):
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.windowEffect.setAeroEffect(int(self.winId()))
        self.setStyleSheet(open("setting.qss",encoding="utf-8").read())
        #self.windowEffect.addWindowAnimation(int(self.winId()))
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
        QMessageBox.about(self,"关于uClock","UCLOCK By LYX\nv1.0\n基于Python3.8与PyQt5构建")
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