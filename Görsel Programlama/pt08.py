from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        le1 = QLineEdit()
        le1.setValidator(QIntValidator())
        le1.setMaxLength(4)
        le1.setAlignment(Qt.AlignRight)
        le1.setFont(QFont("Arial", 20))


        le2 = QLineEdit()
        le2.setValidator(QDoubleValidator(0.99,99.99,2))

        le3 = QLineEdit()
        le3.setInputMask("999_999_99_99")
        le3.setFont(QFont("Arial", 20))


        le4 = QLineEdit()
        le4.textChanged.connect(self.texchanged)
        le4.editingFinished.connect(self.enterpressed)

        le5 = QLineEdit()
        le5.setReadOnly(True)


        le6 = QLineEdit()
        le6.setEchoMode(QLineEdit.Password)
        le6.textChanged.connect(self.texchanged)


        flo = QFormLayout()

        flo.addRow("integer validator", le1)
        flo.addRow("double validator", le2)
        flo.addRow("input mask", le3)
        flo.addRow("Text changed event", le4)
        flo.addRow("readonly", le5)
        flo.addRow("password", le6)

        self.setLayout(flo)

    def texchanged(self,text):
        print(text)

    def enterpressed(self):
        print("enter pressed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


