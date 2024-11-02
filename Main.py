from PyQt5.QtWidgets import *

from CodeGen import Ui_MainWindow
from GenCode import *

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super(MyMainWindow, self).__init__(*args,**kwargs)
        self.setupUi(self)
        self.initButtons()

    def initButtons(self):
        self.pushButtonGen.clicked.connect(self.clikpushButtonGen)
        pass
    def clikpushButtonGen(self):
        print("clikpushButtonGen")
        codesig = self.lineEditSignature.text()
        ret = GenCode(codesig)
        self.plainTextEditCode.setPlainText(ret)
        pass


if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()