from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from Ui_clock import *
import sys,time
from effects.windowEffecter import WindowEffect
from zhdate import ZhDate as lunar_date
from Ui_setting import Ui_setting
from setting import Settinger
import spider
import datetime
import platform
import json
class clockWindow(QSplashScreen,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(1400,100,self.width(),self.height(),)
        self.setup()
    def setup(self):
        with open("settings.json","r",encoding="utf-8") as f:
            self.settings=json.load(f)
        self.settinged=Settinger()
        self.testInternet()
        self.uis()
        self.effects()
        self.dates()
        self.countdown()
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
        self.setContextMenuPolicy(Qt.CustomContextMenu)  
        self.customContextMenuRequested.connect(lambda:self.contextMenu.exec_(QCursor.pos())) 
        self.contextMenu = QMenu(self)
        self.closeer = self.contextMenu.addAction('关闭')
        self.settinger = self.contextMenu.addAction('设置') 
        self.piner = self.contextMenu.addAction('置顶(有bug）')
        self.piner.setCheckable(True)
        self.closeer.triggered.connect(self.close)
        self.settinger.triggered.connect(self.setting)
        self.piner.triggered.connect(self.pin)
        # self.view=QWebEngineView()
        self.view.page().setBackgroundColor(Qt.transparent)
        self.view.setAttribute(Qt.WA_TranslucentBackground)
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
    def pin(self):
        if not self.isActiveWindow():
            self.activateWindow()
            self.showNormal()
        else:
            self.inactivateWindow()
    def inactivateWindow(self):
        pass
    def dates(self):
        self.weatherIcon.setPixmap(QPixmap("weathers/未知").scaled(128,128))
        self.date.setText(time.strftime('%Y-%m-%d %a').replace("Mon","周一").replace("Thu", "周二").replace("Wed","周三").replace("Thu", "周四").replace("Fri", "周五").replace("Sat", "周六").replace("Sun","周日"))
        a=datetime.date.today()
        dt_date = datetime.datetime(a.year,a.month,a.day)
        date = lunar_date.from_datetime(dt_date).chinese()
        self.chinese.setText(date[:-4]+spider.holiday())
        self.famous.setWordWrap(True)
        self.famous.setText(spider.famous())
        w=spider.weather()
        self.weather.setText(w[0]+" "+w[1])
        self.weatherIcon.setPixmap(QPixmap("weathers/"+w[0]).scaled(128,128))
        self.timer=timeReloadThread()
        self.timer.start()
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
            if "linux" not in platform.platform().lower() and (platform.platform()>="Windows-10-10.0.15063-SP0"):
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.contextMenu.setAttribute(Qt.WA_TranslucentBackground)
                self.contextMenu.setStyleSheet("""background:transparent；
                

 QMenu {
    background: transparent;
    border: 0px;
}

QMenu::item {
    /* padding-right: 20px;
    padding-left: 13px; */
    padding: 7px 20px 7px 13px;
    background-color: transparent;
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
                self.windowEffect.setAcrylicEffect(int(self.contextMenu.winId()),gradientColor="FFFFFF99")
                self.windowEffect.setShadowEffect(int(self.winId()))
            elif "linux" not in platform.platform().lower() and (platform.platform()=="Windows-7" and platform.platform()<"Windows-8"):
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.windowEffect.setAeroEffect(int(self.winId()))
                self.windowEffect.setShadowEffect(int(self.winId()))
            else:
                self.setWindowOpacity(0.8)
                self.windowEffect.setShadowEffect(int(self.winId()))
        elif self.settings["appearance"]["mode"]=="pic":
            self.pic=True
            self.windowEffect.setShadowEffect(int(self.winId()))
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
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
        time.sleep(0.1)
        while True:
            window.time.setText(time.strftime('%H:%M:%S'))
            time.sleep(0.01)
            
if __name__=="__main__":
    app = QApplication(sys.argv)
    window=clockWindow()
    window.show()
    sys.exit(app.exec_())