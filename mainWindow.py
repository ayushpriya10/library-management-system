import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from UI_Files.startScreen import Ui_LoginScreen
from UI_Files.mainScreen import Ui_mainScreen

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)

    def login(self):
        uname = self.ui.unameText.text()
        passwd = self.ui.passText.text()
        print(uname)
        print(passwd)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
