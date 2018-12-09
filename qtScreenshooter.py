import sys
from PyQt5.QtCore import QTimer 
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog, QFileDialog, QShortcut
from PyQt5.QtGui import QScreen, QPixmap, QKeySequence 
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

        # Keyboard shortcuts
        # Exit
        self.exitShortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.exitShortcut.activated.connect(self.close)

        # Radio Button access
        self.capEntireScreenShortcut = QShortcut(QKeySequence("Ctrl+E"), self)
        self.capEntireScreenShortcut.activated.connect(self.capEntireScrnRadBtn.nextCheckState)
        self.capRgnShortcut = QShortcut(QKeySequence("Ctrl+R"), self)
        self.capRgnShortcut.activated.connect(self.capSelectRgnRadBtn.nextCheckState)
        self.capActiveWinShortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        self.capActiveWinShortcut.activated.connect(self.capActiveWndRadBtn.nextCheckState)

        # Start Button
        self.startBtnShortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.startBtnShortcut.activated.connect(self.startBtnAction)

        
    def cancelBtnAction(self):
        """Close the window when cancel is pressed"""
        self.close()

    def startBtnAction(self):
        if self.capEntireScrnRadBtn.isChecked():
            self.hide()
            # Delay for 300 milliseconds and take screenshot
            self.windowTimer.singleShot(500, self.takeScreenshot)

    def takeScreenshot(self, xStart=0, yStart=0, xWidth=0, yHeight=0):
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(0)
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
        image = QPixmap(media)
        self.mediaPreviewLabel.setPixmap(image.scaled(300, 230))
        ff = QFileDialog(self, "Save", "/home")
        ff.exec()


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWin() 
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
