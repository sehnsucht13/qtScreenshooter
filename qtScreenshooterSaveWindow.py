# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtScreenshooterSaveWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_qtScreenshooterSaveWindow(object):
    def setupUi(self, qtScreenshooterSaveWindow):
        qtScreenshooterSaveWindow.setObjectName("qtScreenshooterSaveWindow")
        qtScreenshooterSaveWindow.resize(622, 362)
        self.verticalLayoutWidget = QtWidgets.QWidget(qtScreenshooterSaveWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 105, 160, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.optnVertLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.optnVertLayout.setContentsMargins(0, 0, 0, 0)
        self.optnVertLayout.setObjectName("optnVertLayout")
        self.optnLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.optnLabel.setObjectName("optnLabel")
        self.optnVertLayout.addWidget(self.optnLabel)
        self.saveCheckbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.saveCheckbox.setObjectName("saveCheckbox")
        self.optnVertLayout.addWidget(self.saveCheckbox)
        self.cpyToClpBrdCheckbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cpyToClpBrdCheckbox.setObjectName("cpyToClpBrdCheckbox")
        self.optnVertLayout.addWidget(self.cpyToClpBrdCheckbox)
        self.uploadToImgurCheckbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.uploadToImgurCheckbox.setObjectName("uploadToImgurCheckbox")
        self.optnVertLayout.addWidget(self.uploadToImgurCheckbox)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.optnVertLayout.addWidget(self.checkBox)
        self.line = QtWidgets.QFrame(qtScreenshooterSaveWindow)
        self.line.setGeometry(QtCore.QRect(-10, 50, 641, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.qtScreenshooterLabel = QtWidgets.QLabel(qtScreenshooterSaveWindow)
        self.qtScreenshooterLabel.setGeometry(QtCore.QRect(180, 10, 271, 41))
        self.qtScreenshooterLabel.setObjectName("qtScreenshooterLabel")
        self.acceptBtn = QtWidgets.QPushButton(qtScreenshooterSaveWindow)
        self.acceptBtn.setGeometry(QtCore.QRect(510, 316, 91, 31))
        self.acceptBtn.setObjectName("acceptBtn")
        self.cancelBtn = QtWidgets.QPushButton(qtScreenshooterSaveWindow)
        self.cancelBtn.setGeometry(QtCore.QRect(410, 316, 91, 31))
        self.cancelBtn.setObjectName("cancelBtn")
        self.mediaPreviewLabel = QtWidgets.QLabel(qtScreenshooterSaveWindow)
        self.mediaPreviewLabel.setGeometry(QtCore.QRect(310, 70, 301, 221))
        self.mediaPreviewLabel.setText("")
        self.mediaPreviewLabel.setObjectName("mediaPreviewLabel")

        self.retranslateUi(qtScreenshooterSaveWindow)
        QtCore.QMetaObject.connectSlotsByName(qtScreenshooterSaveWindow)

    def retranslateUi(self, qtScreenshooterSaveWindow):
        _translate = QtCore.QCoreApplication.translate
        qtScreenshooterSaveWindow.setWindowTitle(_translate("qtScreenshooterSaveWindow", "qtScreenshooter"))
        self.optnLabel.setText(_translate("qtScreenshooterSaveWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Actions</span></p></body></html>"))
        self.saveCheckbox.setText(_translate("qtScreenshooterSaveWindow", "Save"))
        self.cpyToClpBrdCheckbox.setText(_translate("qtScreenshooterSaveWindow", "Copy to clipboard"))
        self.uploadToImgurCheckbox.setText(_translate("qtScreenshooterSaveWindow", "Upload to imgur"))
        self.checkBox.setText(_translate("qtScreenshooterSaveWindow", "CheckBox"))
        self.qtScreenshooterLabel.setText(_translate("qtScreenshooterSaveWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">qtScreenshooter</span></p></body></html>"))
        self.acceptBtn.setText(_translate("qtScreenshooterSaveWindow", "Accept"))
        self.cancelBtn.setText(_translate("qtScreenshooterSaveWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qtScreenshooterSaveWindow = QtWidgets.QDialog()
    ui = Ui_qtScreenshooterSaveWindow()
    ui.setupUi(qtScreenshooterSaveWindow)
    qtScreenshooterSaveWindow.show()
    sys.exit(app.exec_())

