import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from PyQt5.QtGui import QScreen, QPixmap
from qtScreenshooterMainWindow import Ui_qtScreenshooterMainWindow
from qtScreenshooterSaveWindow import Ui_qtScreenshooterSaveWindow

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
        self.saveWindow = SaveWin()
        
    def cancelBtnAction(self):
        """Close the window when cancel is pressed"""
        self.close()

    def startBtnAction(self):
        if self.capEntireScrnRadBtn.isChecked():
            self.hide()
            # Delay for 300 milliseconds and take screenshot
            self.windowTimer.singleShot(500, self.takeScreenshot)

    def takeScreenshot(self, xStart=0, yStart=0, xWidth=0, yHeight=0):
        print("I was called")
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(0)
        # screenshot.save('shot.jpg', 'jpg')
        self.saveWindow.showMediaPreview(screenshot)
        self.saveWindow.showWin()

class SaveWin(QDialog, Ui_qtScreenshooterSaveWindow):
    def __init__(self):
        QDialog.__init__(self)
        Ui_qtScreenshooterSaveWindow.__init__(self)
        self.setupUi(self)
        self.cancelBtn.clicked.connect(self.saveWinCancelBtn)

    def saveWinCancelBtn(self):
        self.close()    

    def showWin(self):
        self.show()

    def showMediaPreview(self, media):
        print("I was called as ewll")
        image = QPixmap(media)
        self.mediaPreviewLabel.setPixmap(image.scaled(301, 221))


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWin() 
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
