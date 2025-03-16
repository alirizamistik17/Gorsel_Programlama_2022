from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("One", self)
        btn1.move(30,50)

        btn2 = QPushButton("Two", self)
        btn2.move(150,50)

        btn1.clicked.connect(self.btn_Clicked)
        btn2.clicked.connect(self.btn_Clicked)

        
    def btn_Clicked(self):
        sender = self.sender()
        print(sender.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


