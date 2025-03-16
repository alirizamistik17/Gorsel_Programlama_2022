from PyQt5.QtWidgets import *
import sys

class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dialog penceresi")
        self.setFixedWidth(500)
 

        usernameLabel = QLabel("&Username", self)
        usernameTBox = QLineEdit(self) 
        usernameLabel.setBuddy(usernameTBox)

        passLabel = QLabel("&Password", self)
        passTBox = QLineEdit(self) 
        passLabel.setBuddy(passTBox)


        btnOK = QPushButton("&OK")

        btnCancel = QPushButton("&Cancel")

        gridlayout = QGridLayout(self)

        gridlayout.addWidget(usernameLabel,0,0)
        gridlayout.addWidget(usernameTBox,0,1,1,2)

        gridlayout.addWidget(passLabel,1,0)
        gridlayout.addWidget(passTBox,1,1,1,2)

        gridlayout.addWidget(btnOK,2,1)
        gridlayout.addWidget(btnCancel,2,2)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


