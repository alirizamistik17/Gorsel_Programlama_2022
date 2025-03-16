from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Text Edit Örneği")
        self.resize(300,300)

        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("Button 1")
        self.btnPress2 = QPushButton("Button 2")
        self.btnPress3 = QPushButton("Button 3")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        layout.addWidget(self.btnPress3)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        self.btnPress3.clicked.connect(self.btnPress3_Clicked)


        self.setLayout(layout)
    
    def btnPress1_Clicked(self):
        self.textEdit.setPlainText("Hello\nHello world");

    def btnPress2_Clicked(self):
        self.textEdit.setHtml("<p><strong style='color:red;'>Hello</strong> world</p>")

    def btnPress3_Clicked(self):
        self.textEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


