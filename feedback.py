from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Ui_feedback import *
import spider
import datetime
import mail
class Feedbacker(QWidget,Ui_feedbacker):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setup()
    def setup(self):
        self.setWindowIcon(QIcon("effects/pics/uclock.ico"))
        self.pushButton_2.clicked.connect(self.send)
        self.textEdit.textChanged.connect(self.sete)
    def sete(self):
        if self.textEdit.toPlainText().replace(" ","")=="":
            self.pushButton_2.setDisabled(True)
        else:
            self.pushButton_2.setEnabled(True)
    def send(self):
        mail.mail(c=self.textEdit.toPlainText(),t="A new uClock Issue")
        QMessageBox.information(self,"提示","发送成功，感谢您的反馈！")
        self.close()
def start(message):
    global window
    window=Feedbacker()
    window.textEdit.setText("我在使用uClock时，遇到了如下这个bug：\n"+message+"\n希望修复！！！")
    window.show()
if __name__=="__main__":
    app = QApplication(sys.argv)
    window=Feedbacker()
    window.show()
    sys.exit(app.exec_())
#测试邮箱密码：1145141919810ifyouusethisaccountyouare250
#账号:lyxprogramstest@hotmail.com
#生日1919.8.10
#臭死人的账号你想要吗？！