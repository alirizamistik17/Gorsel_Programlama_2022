import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(300,300)

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>Python</font>")
        label1.setAlignment(Qt.AlignCenter)
        label1.setAutoFillBackground(True)
        
        palette  = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)

        label1.setPalette(palette)

        label2.setText("<a href='#'>Link</a>")
        label2.setAlignment(Qt.AlignCenter)

        label3.setText("label3")
        label3.setAlignment(Qt.AlignCenter)
        
        label3.setAutoFillBackground(True)
        label3.setPalette(palette)


        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://biruni.edu.tr'>Biruni</a>")
        label4.setAlignment(Qt.AlignCenter)
        label4.setToolTip("Biruni website")
        label4.setPixmap(QPixmap("logo.svg"))


        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkHovered.connect(self.linkHovered)
        label1.linkHovered.connect(self.linkHovered)

        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
    
    def linkHovered(self):
        print("Link hovered")

    def linkClicked(self):
        print("Link clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QLabelDemo()
    w.show()
    sys.exit(app.exec_())
