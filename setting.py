VERSION="2.0"
CHANGELOG="""1.0(2022/5/28)
    1.不用说，创建程序
1.1(2022/6/20)
    1.设置适配Fluent Design
    2.适配Win11 Mica
    3.细节优化（比如圆角）
    4.修复诸多bug
    5.release可以在大部分Windows7+系统里面运行（作者暂时没有适配Linux，可能会出bug
    6.天气图标修改
1.1.22621_fixed(2022/6/21)
    1.因为1.1有很多小问题（release都没发github），就发布了这个修订版
    2.修复诸如置顶等bug
    3.修复主题问题
    4.彻底不支持Linux（。。。太难适配了
1.2(2022/11/11)
    1.作为一个鸽子，这期间一直在搞博客，五个月过期uClock终于更新了！！！
    2.增加托盘功能
    3.修复部分bug，如进入软件计时器错误与设置关闭导致的闪退
    4.增加背景字体适配功能
    5.更换打包方式，增加开机自启和内置字体功能，修复1.1.22621_fixed因使用nuitka导致的联网bug
2.0(2023/12/3)
    1.修复大量bug
    2.增加透明度和阴影设置项
    3.缩减GeoLite数据库，采用api获取城市
    4.接入一言API
    5.修改UI"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,time,platform,os,subprocess,psutil
from effects.windowEffecter import WindowEffect
from effects.QFramelessWindow import *
from zhdate import ZhDate as lunar_date
# 其他系统ui测试
# class platform:#Win10
#     def platform():
#         return "Windows-10-10.0.19041-SP0"
# class platform:#Win7
#     def platform():
#         return "Windows-7-10.0.7601-SP1"
#否则就是Win11
if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.22000-SP0") and not ("Windows-7" in platform.platform() or "Windows-8" in platform.platform() or "Windows-Vista" in platform.platform()):
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
import feedback
from effects.windowEffecter import window_effect
class Settinger(QWidget,Ui_setting):
    windowEffect = window_effect.WindowEffect()
    BORDER_WIDTH=5
    if not ("linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.22000-SP0") and not ("Windows-7" in platform.platform() or "Windows-8" in platform.platform() or "Windows-Vista" in platform.platform())):
        def nativeEvent(self, eventType, message):
            """ Handle the Windows message """
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
            elif msg.message == win32con.WM_NCCALCSIZE:
                if self._isWindowMaximized(msg.hWnd):
                    self.__monitorNCCALCSIZE(msg)
                return True, 0
            elif msg.message == win32con.WM_GETMINMAXINFO:
                if self._isWindowMaximized(msg.hWnd):
                    window_rect = win32gui.GetWindowRect(msg.hWnd)
                    if not window_rect:
                        return False, 0

                    # get the monitor handle
                    monitor = win32api.MonitorFromRect(window_rect)
                    if not monitor:
                        return False, 0

                    # get the monitor info
                    __monitorInfo = win32api.GetMonitorInfo(monitor)
                    monitor_rect = __monitorInfo['Monitor']
                    work_area = __monitorInfo['Work']

                    # convert lParam to MINMAXINFO pointer
                    info = cast(msg.lParam, POINTER(MINMAXINFO)).contents

                    # adjust the size of window
                    info.ptMaxSize.x = work_area[2] - work_area[0]
                    info.ptMaxSize.y = work_area[3] - work_area[1]
                    info.ptMaxTrackSize.x = info.ptMaxSize.x
                    info.ptMaxTrackSize.y = info.ptMaxSize.y

                    # modify the upper left coordinate
                    info.ptMaxPosition.x = abs(window_rect[0] - monitor_rect[0])
                    info.ptMaxPosition.y = abs(window_rect[1] - monitor_rect[1])
                    return True, 1

            return QWidget.nativeEvent(self, eventType, message)
        def _isWindowMaximized(self, hWnd):
            # GetWindowPlacement() returns the display state of the window and the restored,
            # maximized and minimized window position. The return value is tuple
            windowPlacement = win32gui.GetWindowPlacement(hWnd)
            if not windowPlacement:
                return False

            return windowPlacement[1] == win32con.SW_MAXIMIZE

        def __monitorNCCALCSIZE(self, msg):
            """ Adjust the size of window """
            monitor = win32api.MonitorFromWindow(msg.hWnd)

            # If the display information is not saved, return directly
            if monitor is None and not self.__monitorInfo:
                return
            elif monitor is not None:
                self.__monitorInfo = win32api.GetMonitorInfo(monitor)

            # adjust the size of window
            params = cast(msg.lParam, POINTER(NCCALCSIZE_PARAMS)).contents
            params.rgrc[0].left = self.__monitorInfo['Work'][0]
            params.rgrc[0].top = self.__monitorInfo['Work'][1]
            params.rgrc[0].right = self.__monitorInfo['Work'][2]
            params.rgrc[0].bottom = self.__monitorInfo['Work'][3]

        def __onScreenChanged(self):
            hWnd = int(self.windowHandle().winId())
            win32gui.SetWindowPos(hWnd, None, 0, 0, 0, 0, win32con.SWP_NOMOVE |
                                win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)

    def __init__(self):
        super().__init__()
        self.__monitorInfo = None
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.setWindowIcon(QIcon("./effects/pics/uclock.png"))
        self.setup()
        if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.22000-SP0") and not ("Windows-7" in platform.platform() or "Windows-8" in platform.platform() or "Windows-Vista" in platform.platform()):
            self.setWindowFlags(Qt.Widget)
    def closeEvent(self,event):
        event.ignore()
        with open("settings.json","w+",encoding="utf-8") as f:
            json.dump(self.setting,f)
        self.hide()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and event.y()<=30:
            # self.move(event.globalPos() - self.dragPosition)
            # event.accept()
            self.windowEffect.moveWindow(int(self.winId()))
    def paintEvent(self,event):
        if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.22000-SP0") and not ("Windows-7" in platform.platform() or "Windows-8" in platform.platform() or "Windows-Vista" in platform.platform()):
            self.pa.begin(self)
            p=QPen()
            p.setStyle(Qt.SolidLine)
            p.setColor(QColor("#66CCFF"))
            p.setWidth(3)
            self.pa.setPen(p)
            self.pa.drawLine(self.menu.x()+4,(self.menu.y()+(self.menu.height()-15)//4*self.menu.row(self.menu.currentItem()))+28,self.menu.x()+4,(self.menu.y()+(self.menu.height()-15)//4*self.menu.row(self.menu.currentItem()))+12)
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
        # if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.22000-SP0") and not ("Windows-7" in platform.platform() or "Windows-8" in platform.platform() or "Windows-Vista" in platform.platform()):
        if self.setting["appearance"]["mode"]=="effect":
            if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.22000-SP0") and not ("Windows-7" in platform.platform() or "Windows-8" in platform.platform() or "Windows-Vista" in platform.platform()):
                self.view.currentWidget().setAttribute(Qt.WA_TranslucentBackground)
                self.view.currentWidget().setAutoFillBackground(True)
        for y in range(400,0,-10):
            op = QGraphicsOpacityEffect()
            op.setOpacity(1-y/400)
            self.view.currentWidget().setGraphicsEffect(op)
            QApplication.processEvents()
            self.view.currentWidget().setGeometry(0,y//10,self.view.currentWidget().width(),self.view.currentWidget().height())
        self.view.setCurrentIndex(s)
    def showLog(self):
        self.l.show()
    def f(self):
        feedback.start("")
    def setup(self):
        self.w1=self.width()
        # self.setWindowFlags(Qt.FramelessWindowHint |
        #         Qt.WindowMinMaxButtonsHint)
        self.qw=self.menu.width()
        self.pa=QPainter()
        self.l=logShower()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.toolButton_6.hide()
        # self.setWindowFlags(Qt.SplashScreen)
        self.setWindowFlags(Qt.CustomizeWindowHint|Qt.WindowMinMaxButtonsHint)
        self.setMouseTracking(True)
        try:
            with open("settings.json","r",encoding="utf-8") as f:
                self.setting=json.load(f)
        except:
            self.setting={"appearance": {"mode": "effect", "pic": "", "showMode": "Window","shadow":True,"opaticy":0.90}, "countdown": {"countdownDay": "2114-05-14", "countdownThing": "1145141919810", "isCountdown": False}, "network": {"doNotTraceback": False}, "other": {"startupOnLogin": False}, "sidebar": {"html": "", "type": "calendar", "zoom": 0.1}}
        self.label_18.setPixmap(QPixmap("effects/pics/uclock.png").scaled(QSize(128,128)))
        self.label_22.setText(self.label_22.text().format(VERSION))
        self.dateEdit.setMinimumDate(datetime.datetime.now())
        self.feed.clicked.connect(self.f)
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
        self.setting
        if self.setting["appearance"]["shadow"]:
            self.checkBox_4.setChecked(True)
        self.checkBox_4.clicked.connect(self.setShadow)
        self.horizontalSlider.setValue(int(self.setting["appearance"]["opaticy"]*100))
        self.horizontalSlider.valueChanged.connect(self.setOpaticy)
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
        self.pushButton_2.clicked.connect(self.restart)
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
            if "linux" not in platform.platform().lower() and ("Windows-7" in platform.platform() or "Windows-Vista" in platform.platform()):
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.windowEffect.setAeroEffect(int(self.winId()))
                self.setStyleSheet(open("effects/settingWin10.qss",encoding="utf-8").read())
                self.windowEffect.setShadowEffect(int(self.winId()))
            elif "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.22000-SP0" and not "Windows-8" in platform.platform()):
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.windowEffect.setMicaEffect(int(self.winId()))
                self.setStyleSheet(open("effects/settingWin11.qss",encoding="utf-8").read())
                self.label_10.setText("")
            elif "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.19041-SP0" and not "Windows-8" in platform.platform()):
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.windowEffect.setAcrylicEffect(int(self.winId()),gradientColor="FFFFFFC9")
                self.setStyleSheet(open("effects/settingWin10.qss",encoding="utf-8").read())
            elif "linux" not in platform.platform().lower() and ("Windows-8" in platform.platform()):
                self.setStyleSheet(open("effects/settingWin10.qss",encoding="utf-8").read())
                self.windowEffect.setShadowEffect(int(self.winId()))
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
            self.windowEffect.setShadowEffect(int(self.winId()))
        if self.setting["appearance"]["showMode"]=="Window":
            self.radioButton_4.setChecked(True)
        if self.setting["appearance"]["showMode"]=="Tool":
            self.radioButton_5.setChecked(True)
        self.radioButton_4.clicked.connect(self.setM)
        self.radioButton_5.clicked.connect(self.setM)
        self.windowEffect.addWindowAnimation(int(self.winId()))
    def restart(self):
        self.close()
        subprocess.Popen(" ".join(psutil.Process(os.getpid()).cmdline()),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        os._exit(0)
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
    def setM(self):
        if self.radioButton_4.isChecked():
            self.setting["appearance"]["showMode"]="Window"
        elif self.radioButton_5.isChecked():
            self.setting["appearance"]["showMode"]="Tool"
    def setEffect(self):
        if self.radioButton.isChecked():
            self.setting["appearance"]["mode"]="effect"
        elif self.radioButton_2.isChecked():
            self.setting["appearance"]["mode"]="pic"
        elif self.radioButton_3.isChecked():
            self.setting["appearance"]["mode"]="no"
    def resizeEvent(self, event):
        if self.menu.width()<self.qw:
            self.menu.setGeometry(self.menu.x(),self.menu.y(),40,self.menu.height())
            for i in range(4):
                self.menu.item(i).setText("")
            self.w1=self.width()
        elif self.width()>=self.w1:
            self.menu.item(0).setText("外观")
            self.menu.item(1).setText("倒计时")
            self.menu.item(2).setText("其它")
            self.menu.item(3).setText("关于")
            self.menu.setGeometry(self.menu.x(),self.menu.y(),self.qw,self.menu.height())
    def setCountdown(self,state):
        self.setting["countdown"]["isCountdown"]=state
    def setCountdownDate(self):
        self.setting["countdown"]["countdownDay"]=self.dateEdit.dateTime().toString("yyyy-MM-dd")
    def setCountdownThing(self):
        self.setting["countdown"]["countdownThing"]=self.lineEdit_2.text()
    def setShadow(self):
        self.setting["appearance"]["shadow"]=self.checkBox_4.isChecked()
    def setOpaticy(self):
        self.setting["appearance"]["opaticy"]=self.horizontalSlider.value()/100
class logShower(QDialog,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setup()
    def setup(self):
        self.setWindowFlags(Qt.SubWindow)
        self.textBrowser.setText(CHANGELOG)
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
