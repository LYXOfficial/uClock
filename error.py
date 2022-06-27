from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Ui_error import *
import spider
import datetime
import traceback
import feedback
class ErrorShower(QWidget,Ui_ErrorShower):
    def __init__(self,message):
        super().__init__()
        self.message=message
        self.setupUi(self)
        self.retranslateUi(self)
        self.setup()
    def setup(self):
        self.setWindowIcon(QIcon("effects/pics/uclock.ico"))
        self.pushButton_2.clicked.connect(lambda:feedback.start(self.message))
        self.pushButton.clicked.connect(self.close)
def start(message):
    global window
    window=ErrorShower(message)
    window.textBrowser.setText(message)
    window.show()
if __name__=="__main__":
    app = QApplication(sys.argv)
    window=ErrorShower("")
    window.show()
    sys.exit(app.exec_())