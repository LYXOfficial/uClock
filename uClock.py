from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from Ui_clock import *
import sys,time
from effects.QFramelessWindow import *
from effects.windowEffecter import WindowEffect
from zhdate import ZhDate as lunar_date
from Ui_setting import Ui_setting
import Ui_tool
from setting import Settinger
import spider
import datetime
import platform
import json
import error
import traceback
try:
    class Tool(NoIconFramelessWindow,Ui_tool.Ui_Form):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.retranslateUi(self)
            self.setup()
        def setup(self):
            with open("settings.json","r",encoding="utf-8") as f:
                self.settings=json.load(f)
            self.desktop = QApplication.desktop()
            self.screenRect = self.desktop.screenGeometry()
            self.height1 = self.screenRect.height()
            self.width1 = self.screenRect.width()
            self.setGeometry(int(self.width1*(1400/1920))+200,int(self.height1*(100/1080)),self.width(),self.height())
            self.windowEffect=WindowEffect()
            #self.setStyleSheet("background:transparent")
            # op=QGraphicsOpacityEffect()
            # op.setOpacity(0)
            # self.setGraphicsEffect(op)
            # self.setAutoFillBackground(True)
            #系统自适应特效
            self.pic=False
            if self.settings["appearance"]["mode"]=="effect":
                if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.19041-SP0") and (not "Windows-7" in platform.platform() and not "Windows-8" in platform.platform()):
                    self.setAttribute(Qt.WA_TranslucentBackground)
                    self.windowEffect.setAcrylicEffect(int(self.winId()),gradientColor="FFFFFFC9")
                    self.windowEffect.setAcrylicEffect(int(self.winId()))
                    self.windowEffect.setShadowEffect(int(self.winId()))
                elif "linux" not in platform.platform().lower() and ("Windows-7" in platform.platform()):
                    self.setAttribute(Qt.WA_TranslucentBackground)
                    self.windowEffect.setAeroEffect(int(self.winId()))
                    self.windowEffect.setShadowEffect(int(self.winId()))
                else:
                    self.windowEffect.setShadowEffect(int(self.winId()))
            elif self.settings["appearance"]["mode"]=="pic":
                self.pic=True
                self.windowEffect.setShadowEffect(int(self.winId()))
                try:
                    self.setStyleSheet("QMenu{color:#000000}\nQWidget{color:"+str(spider.getpjfs(self.settings["appearance"]["pic"]))+"}")
                except:
                    self.pic=False
            elif self.settings["appearance"]["mode"]=="no":
                self.windowEffect.setShadowEffect(int(self.winId()))
        def paintEvent(self,a0:QPaintEvent) -> None:
            if self.pic:
                painter = QPainter(self)
                pixmap = QPixmap(self.settings["appearance"]["pic"])
                painter.drawPixmap(self.rect(), pixmap)
        def mouseMoveEvent(self,event):
            self.windowEffect.moveWindow(self.winId())
    class ClockWindow(NoIconFramelessWindow,Ui_Form):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.retranslateUi(self)
            self.setup()
        def setup(self):
            self.desktop = QApplication.desktop()
            self.screenRect = self.desktop.screenGeometry()
            self.height1 = self.screenRect.height()
            self.width1 = self.screenRect.width()
            self.setGeometry(int(self.width1*(1400/1920)),int(self.height1*(100/1080)),self.width(),self.height())
            with open("settings.json","r",encoding="utf-8") as f:
                self.settings=json.load(f)
            self.settinged=Settinger()
            self.testInternet()
            self.uis()
            self.effects()
            self.dates()
            self.countdown()
            if self.settings["appearance"]["showMode"]=="Window":
                self.show()
            if self.settings["appearance"]["showMode"]=="Tool":
                self.tool=Tool()
                self.tool.show()
                self.tool.close()
                self.tool.show()
        def countdown(self):
            if self.settings["countdown"]["isCountdown"] and self.settings["countdown"]["countdownDay"]>=time.strftime("%Y-%m-%d"):
                date1 = datetime.datetime.strptime(self.settings["countdown"]["countdownDay"], "%Y-%m-%d").date()
                date2 = datetime.datetime.now().date()
                Days = (date1-date2).days
                self.djs.setText(f"""<html><head/><body><p>距离{self.settings["countdown"]["countdownThing"]}仅剩<span style=" color:#ff0000;">{Days}</span>天！</p></body></html>""")
        def testInternet(self):
            if not self.settings["network"]["doNotTraceback"]:
                try:
                    spider.test()
                except:
                    QMessageBox.warning(self,"错误","系统未联网，可能会影响功能使用")
        def uis(self):
            self.weatherIcon.setPixmap(QPixmap("weathers/未知").scaled(QSize(128,128)))
            self.setContextMenuPolicy(Qt.CustomContextMenu)  
            self.customContextMenuRequested.connect(lambda:self.contextMenu.exec_(QCursor.pos())) 
            self.contextMenu = QMenu(self)
            self.closeer = self.contextMenu.addAction('关闭')
            self.settinger = self.contextMenu.addAction('设置') 
            self.piner = self.contextMenu.addAction('置顶')
            self.piner.setCheckable(True)
            self.closeer.triggered.connect(self.close)
            self.settinger.triggered.connect(self.setting)
            self.piner.triggered.connect(self.pin)
            # self.view=QWebEngineView()
            self.view.page().setBackgroundColor(Qt.transparent)
            self.view.setAttribute(Qt.WA_TranslucentBackground)
            self.tray = QSystemTrayIcon()
            self.tray.setIcon(QIcon("effects/pics/uclock.ico"))
            self.tray.setContextMenu(self.contextMenu)
            self.tray.show()
            if self.settings["sidebar"]["type"]=="clock":
                #时钟
                self.view.setHtml(open("clock.html",encoding="utf-8").read())
                self.view.setZoomFactor(0.9)
            elif self.settings["sidebar"]["type"]=="calendar":
                #日历
                self.view.setHtml(open("date.html",encoding="utf-8").read())
                self.view.setZoomFactor(0.47)
            else:
                try:
                    self.view.setHtml(open(self.settings["sidebar"]["html"],encoding="utf-8").read())
                    self.view.setZoomFactor(self.settings["sidebar"]["zoom"])
                except:
                    pass
            self.view.settings().setAttribute(QWebEngineSettings.WebAttribute.ShowScrollBars,False)
            self.view.setContextMenuPolicy(Qt.NoContextMenu)
            #win11/7圆角
            # if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.21996-SP0" or (platform.platform()>"Windows-7" and platform.platform()<"Windows-8")):
            #     self.setWindowFlags(self.windowFlags() & ~Qt.FramelessWindowHint)
            #     self.setWindowFlags(Qt.CustomizeWindowHint)
            # else:
            #     self.setWindowFlags(Qt.SplashScreen)
            # # self.setWindowFlags(Qt.SplashScreen)
            self.settinged.setWindowFlags(Qt.WindowCloseButtonHint)
        def setting(self):
            self.settinged.show()
        #置顶bug终于TM修复了！！！！！！！！！！！！！！！
        def pin(self):
            if not (self.windowFlags() | Qt.WindowStaysOnTopHint) == self.windowFlags():
                self.setWindowFlags(Qt.WindowStaysOnTopHint|self.windowFlags())
                self.show()
            else:
                self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
                self.show()
        def dates(self):
            self.timer=timeReloadThread()
            self.timer.start()
            self.dater=allReloadThread()
            self.dater.start()
        def effects(self):
            self.windowEffect = WindowEffect()
            #self.setStyleSheet("background:transparent")
            # op=QGraphicsOpacityEffect()
            # op.setOpacity(0)
            # self.setGraphicsEffect(op)
            # self.setAutoFillBackground(True)
            #系统自适应特效
            self.pic=False
            if self.settings["appearance"]["mode"]=="effect":
                if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.19041-SP0") and (not "Windows-7" in platform.platform() and not "Windows-8" in platform.platform()):
                    self.setAttribute(Qt.WA_TranslucentBackground)
                    self.windowEffect.setAcrylicEffect(int(self.winId()),gradientColor="FFFFFFC9")
                    self.contextMenu.setStyleSheet("""background:transparent；
                    



    QMenu::item {
        /* padding-right: 20px;
        padding-left: 13px; */
        padding: 7px 20px 7px 13px;
    }

    QMenu::item:selected {

        background-color: rgba(0, 0, 0, 25);
        color: black;
    }

    QMenu::item {
        padding: 7px 20px 7px 14px;
    }
    QMenu::item:selected {
        background-color: rgba(0, 0, 0, 25);
    }
    QMenu::separator {
        background: rgba(0, 0, 0, 104);
        margin-right: 15px;
        margin-top: 5px;
        margin-bottom: 5px;
        margin-left: 15;
    }


                    """)
                    self.windowEffect.setAcrylicEffect(int(self.winId()))
                    self.windowEffect.setShadowEffect(int(self.winId()))
                elif "linux" not in platform.platform().lower() and ("Windows-7" in platform.platform()):
                    self.setAttribute(Qt.WA_TranslucentBackground)
                    self.windowEffect.setAeroEffect(int(self.winId()))
                    self.windowEffect.setShadowEffect(int(self.winId()))
                else:
                    self.windowEffect.setShadowEffect(int(self.winId()))
            elif self.settings["appearance"]["mode"]=="pic":
                self.pic=True
                self.windowEffect.setShadowEffect(int(self.winId()))
                try:
                    self.setStyleSheet("QMenu{color:#000000}\nQWidget{color:"+str(spider.getpjfs(self.settings["appearance"]["pic"]))+"}")
                except:
                    self.pic=False
            elif self.settings["appearance"]["mode"]=="no":
                self.windowEffect.setShadowEffect(int(self.winId()))
        #     if event.button()==Qt.LeftButton:
        #         self.m_flag=True
        #         self.m_Position=event.globalPos()-self.pos()
        #         event.accept()
        #         self.setCursor(QCursor(Qt.ClosedHandCursor))

        # def mouseMoveEvent(self, QMouseEvent):
        #     if Qt.LeftButton and self.m_flag:  
        #         self.move(QMouseEvent.globalPos()-self.m_Position)
        #         QMouseEvent.accept()
        # def mouseReleaseEvent(self, QMouseEvent):
        #     self.m_flag=False
        #     self.setCursor(QCursor(Qt.ArrowCursor))
        def closeEvent(self,event):
            self.timer.exit()
            sys.exit(0)
        def paintEvent(self,a0:QPaintEvent) -> None:
            if self.pic:
                painter = QPainter(self)
                pixmap = QPixmap(self.settings["appearance"]["pic"])
                painter.drawPixmap(self.rect(), pixmap)
    class timeReloadThread(QThread):
        def __init__(self):
            super().__init__()
        def run(self):
            time.sleep(0.3)
            while True:
                window.time.setText(time.strftime('%H:%M:%S'))
                time.sleep(0.01)
    class allReloadThread(QThread):
        def __init__(self):
            super().__init__()
        def run(self):
            global window
            window=None
            while not window:
                pass
            while True:
                window.date.setText(time.strftime('%Y-%m-%d %a').replace("Mon","周一").replace("Tue", "周二").replace("Wed","周三").replace("Thu", "周四").replace("Fri", "周五").replace("Sat", "周六").replace("Sun","周日"))
                a=datetime.date.today()
                dt_date = datetime.datetime(a.year,a.month,a.day)
                date = lunar_date.from_datetime(dt_date).chinese()
                window.chinese.setText(date[:-4]+spider.holiday())
                window.famous.setWordWrap(True)
                window.famous.setText(spider.famous())
                w=spider.weather()
                window.weather.setText(w[0]+" "+w[1])
                window.weatherIcon.setPixmap(QPixmap("weathers/"+w[0].split(" ")[1]))
                time.sleep(600)
    def main():
        global app,window 
        app = QApplication(sys.argv)
        window=ClockWindow()
        window.activateWindow()
        sys.exit(app.exec_())
    if __name__=="__main__":
        main()
except:
    if not "app" in vars():
        print(traceback.format_exc())
        app = QApplication(sys.argv)
        error.start(traceback.format_exc())
        sys.exit(app.exec_())
    else:
        print(traceback.format_exc())
        error.start(traceback.format_exc())