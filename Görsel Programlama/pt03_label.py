from PyQt5.QtWidgets import *
import sys

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QLabelDemo()
    w.show()
    sys.exit(app.exec_())
