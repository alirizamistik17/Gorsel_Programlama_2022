from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tool Button Örneği")
        self.setGeometry(400,200,400,400)


        self.toolbar = self.addToolBar("toolBar")
        self.statusBar()

        self.toolButton = QToolButton()
        self.toolButton.setCheckable(True)
        self.toolButton.setChecked(True)

        self.toolButton.clicked.connect(self.showSth)
        self.toolButton.setArrowType(Qt.RightArrow)


        self.toolbar.addWidget(self.toolButton)

    def showSth(self):
        if self.toolButton.isChecked():
            self.statusBar().showMessage("Show details")
        else:
            self.statusBar().showMessage("Close details")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


