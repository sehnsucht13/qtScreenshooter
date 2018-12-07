import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtGui import QScreen, QPixmap
from qtScreenshooterMainWindow import Ui_qtScreenshooterMainWindow

class MainWin(QMainWindow, Ui_qtScreenshooterMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_qtScreenshooterMainWindow.__init__(self)
        self.setupUi(self)
        self.cancelBtn.clicked.connect(self.cancelBtnAction)
        self.startBtn.clicked.connect(self.startBtnAction)
        # Need to keep a reference to QTimer or it will be garbage collected!!!
        # This means that your callback is not called and you will lose
        # 30 minutes troubleshooting it!!!!!!!!!!!!!!
        self.windowTimer = QTimer()
        
    def cancelBtnAction(self):
        """Close the window when cancel is pressed"""
        self.close()

    def startBtnAction(self):
        self.hide()
        if self.capEntireScreenbtn.isChecked():
            # Wait for half a second for window to hide before taking shot
            self.windowTimer.timeout.connect(self.takeScreenshot)
            # Delay for 300 milliseconds
            self.windowTimer.start(300)

    def takeScreenshot(self):
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(0)
        screenshot.save('shot.jpg', 'jpg')
        self.close()



def main():
    app = QApplication(sys.argv)
    mainWindow = MainWin() 
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
