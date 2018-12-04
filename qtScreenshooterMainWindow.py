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
        qtScreenshooterMainWindow.resize(415, 233)
        qtScreenshooterMainWindow.setIconSize(QtCore.QSize(0, 0))
        qtScreenshooterMainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(qtScreenshooterMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 80, 121, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 2, 0, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.regionToCapLbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.regionToCapLbl.setObjectName("regionToCapLbl")
        self.verticalLayout.addWidget(self.regionToCapLbl)
        self.capEntireScreenbtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.capEntireScreenbtn.setObjectName("capEntireScreenbtn")
        self.verticalLayout.addWidget(self.capEntireScreenbtn)
        self.capActiveWindowBtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.capActiveWindowBtn.setObjectName("capActiveWindowBtn")
        self.verticalLayout.addWidget(self.capActiveWindowBtn)
        self.capSelectRegionBtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.capSelectRegionBtn.setObjectName("capSelectRegionBtn")
        self.verticalLayout.addWidget(self.capSelectRegionBtn)
        self.windowTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.windowTitleLabel.setGeometry(QtCore.QRect(0, 9, 411, 51))
        self.windowTitleLabel.setObjectName("windowTitleLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(320, 200, 85, 27))
        self.startBtn.setObjectName("startBtn")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(210, 200, 85, 27))
        self.cancelBtn.setObjectName("cancelBtn")
        self.delaySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.delaySpinBox.setGeometry(QtCore.QRect(295, 100, 71, 41))
        self.delaySpinBox.setReadOnly(True)
        self.delaySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.delaySpinBox.setMaximum(60)
        self.delaySpinBox.setObjectName("delaySpinBox")
        qtScreenshooterMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(qtScreenshooterMainWindow)
        QtCore.QMetaObject.connectSlotsByName(qtScreenshooterMainWindow)

    def retranslateUi(self, qtScreenshooterMainWindow):
        _translate = QtCore.QCoreApplication.translate
        qtScreenshooterMainWindow.setWindowTitle(_translate("qtScreenshooterMainWindow", "qtScreenshooter"))
        self.regionToCapLbl.setText(_translate("qtScreenshooterMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Region to capture</span></p></body></html>"))
        self.capEntireScreenbtn.setText(_translate("qtScreenshooterMainWindow", "Entire screen"))
        self.capActiveWindowBtn.setText(_translate("qtScreenshooterMainWindow", "Active window"))
        self.capSelectRegionBtn.setText(_translate("qtScreenshooterMainWindow", "Select a region"))
        self.windowTitleLabel.setText(_translate("qtScreenshooterMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">qtScreenshooter</span></p></body></html>"))
        self.startBtn.setText(_translate("qtScreenshooterMainWindow", "Start"))
        self.cancelBtn.setText(_translate("qtScreenshooterMainWindow", "Cancel"))

