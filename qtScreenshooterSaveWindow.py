# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtScreenshooterSaveWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_qtScreenshooter(object):
    def setupUi(self, qtScreenshooter):
        qtScreenshooter.setObjectName("qtScreenshooter")
        qtScreenshooter.resize(622, 362)
        self.mediaPreviewArea = QtWidgets.QGraphicsView(qtScreenshooter)
        self.mediaPreviewArea.setGeometry(QtCore.QRect(300, 70, 291, 221))
        self.mediaPreviewArea.setObjectName("mediaPreviewArea")
        self.verticalLayoutWidget = QtWidgets.QWidget(qtScreenshooter)
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
        self.line = QtWidgets.QFrame(qtScreenshooter)
        self.line.setGeometry(QtCore.QRect(-10, 50, 641, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.qtScreenshooterLabel = QtWidgets.QLabel(qtScreenshooter)
        self.qtScreenshooterLabel.setGeometry(QtCore.QRect(180, 10, 271, 41))
        self.qtScreenshooterLabel.setObjectName("qtScreenshooterLabel")
        self.acceptBtn = QtWidgets.QPushButton(qtScreenshooter)
        self.acceptBtn.setGeometry(QtCore.QRect(510, 316, 91, 31))
        self.acceptBtn.setObjectName("acceptBtn")
        self.cancelBtn = QtWidgets.QPushButton(qtScreenshooter)
        self.cancelBtn.setGeometry(QtCore.QRect(410, 316, 91, 31))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(qtScreenshooter)
        QtCore.QMetaObject.connectSlotsByName(qtScreenshooter)

    def retranslateUi(self, qtScreenshooter):
        _translate = QtCore.QCoreApplication.translate
        qtScreenshooter.setWindowTitle(_translate("qtScreenshooter", "qtScreenshooter"))
        self.optnLabel.setText(_translate("qtScreenshooter", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Actions</span></p></body></html>"))
        self.saveCheckbox.setText(_translate("qtScreenshooter", "Save"))
        self.cpyToClpBrdCheckbox.setText(_translate("qtScreenshooter", "Copy to clipboard"))
        self.uploadToImgurCheckbox.setText(_translate("qtScreenshooter", "Upload to imgur"))
        self.checkBox.setText(_translate("qtScreenshooter", "CheckBox"))
        self.qtScreenshooterLabel.setText(_translate("qtScreenshooter", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">qtScreenshooter</span></p></body></html>"))
        self.acceptBtn.setText(_translate("qtScreenshooter", "Accept"))
        self.cancelBtn.setText(_translate("qtScreenshooter", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qtScreenshooter = QtWidgets.QDialog()
    ui = Ui_qtScreenshooter()
    ui.setupUi(qtScreenshooter)
    qtScreenshooter.show()
    sys.exit(app.exec_())

