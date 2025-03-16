from PyQt5.QtWidgets import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label1.setText("Label1")

        label2 = QLabel(self)
        label2.setText("Label2")

        vbox  = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)

        self.setLayout(vbox)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


