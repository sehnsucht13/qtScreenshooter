# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtScreenshooterMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_qtScreenshooterMainWindow(object):
    def setupUi(self, qtScreenshooterMainWindow):
        qtScreenshooterMainWindow.setObjectName("qtScreenshooterMainWindow")
        qtScreenshooterMainWindow.resize(511, 265)
        qtScreenshooterMainWindow.setIconSize(QtCore.QSize(0, 0))
        qtScreenshooterMainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(qtScreenshooterMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.windowTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.windowTitleLabel.setGeometry(QtCore.QRect(150, 10, 215, 31))
        self.windowTitleLabel.setObjectName("windowTitleLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 40, 511, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(420, 230, 85, 26))
        self.startBtn.setObjectName("startBtn")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(320, 230, 85, 26))
        self.cancelBtn.setObjectName("cancelBtn")
        self.delaySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.delaySpinBox.setGeometry(QtCore.QRect(390, 120, 101, 41))
        self.delaySpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.delaySpinBox.setToolTipDuration(3)
        self.delaySpinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.delaySpinBox.setReadOnly(True)
        self.delaySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.delaySpinBox.setMaximum(60)
        self.delaySpinBox.setObjectName("delaySpinBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 160, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.regionToCapLbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.regionToCapLbl.setObjectName("regionToCapLbl")
        self.verticalLayout.addWidget(self.regionToCapLbl)
        self.capEntireScrnRadBtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.capEntireScrnRadBtn.setObjectName("capEntireScrnRadBtn")
        self.verticalLayout.addWidget(self.capEntireScrnRadBtn)
        self.capSelectRgnRadBtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.capSelectRgnRadBtn.setObjectName("capSelectRgnRadBtn")
        self.verticalLayout.addWidget(self.capSelectRgnRadBtn)
        self.capActiveWndRadBtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.capActiveWndRadBtn.setObjectName("capActiveWndRadBtn")
        self.verticalLayout.addWidget(self.capActiveWndRadBtn)
        qtScreenshooterMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(qtScreenshooterMainWindow)
        QtCore.QMetaObject.connectSlotsByName(qtScreenshooterMainWindow)

    def retranslateUi(self, qtScreenshooterMainWindow):
        _translate = QtCore.QCoreApplication.translate
        qtScreenshooterMainWindow.setWindowTitle(_translate("qtScreenshooterMainWindow", "qtScreenshooter"))
        self.windowTitleLabel.setText(_translate("qtScreenshooterMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">qtScreenshooter</span></p></body></html>"))
        self.startBtn.setText(_translate("qtScreenshooterMainWindow", "Start"))
        self.cancelBtn.setText(_translate("qtScreenshooterMainWindow", "Cancel"))
        self.delaySpinBox.setToolTip(_translate("qtScreenshooterMainWindow", "Select the delay before taking the screenshot or beginning screencast"))
        self.regionToCapLbl.setText(_translate("qtScreenshooterMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Region to capture</span></p></body></html>"))
        self.capEntireScrnRadBtn.setText(_translate("qtScreenshooterMainWindow", "Entire screen"))
        self.capSelectRgnRadBtn.setText(_translate("qtScreenshooterMainWindow", "Select a region"))
        self.capActiveWndRadBtn.setText(_translate("qtScreenshooterMainWindow", "Active window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qtScreenshooterMainWindow = QtWidgets.QMainWindow()
    ui = Ui_qtScreenshooterMainWindow()
    ui.setupUi(qtScreenshooterMainWindow)
    qtScreenshooterMainWindow.show()
    sys.exit(app.exec_())

