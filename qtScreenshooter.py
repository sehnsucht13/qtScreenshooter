import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from qtScreenshooterMainWindow import Ui_qtScreenshooterMainWindow

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_qtScreenshooterMainWindow()
        self.ui.setupUi(self)


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWin()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
