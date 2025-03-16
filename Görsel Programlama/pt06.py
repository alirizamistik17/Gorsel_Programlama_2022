from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Push Button Örneği")
        self.setGeometry(1200,200,400,400)

        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")
        self.closeButton.setIcon(QIcon("close.png"))
        self.closeButton.setShortcut("Ctrl+C")
        self.closeButton.setToolTip("Widget kapansın")
        self.closeButton.move(100,100)
        self.closeButton.resize(300,300)

        self.closeButton.clicked.connect(self.fnClose)

    def fnClose(self):
        print("close butonuna basıldı")
        self.close()
        print("diğer")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


