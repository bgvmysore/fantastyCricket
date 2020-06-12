# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saveteam.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pyFiles.classes import *

class Ui_SaveTeam(object):

    # def __init__(self, p_tupl):
        # self.p_tup = p_tupl
        # return

    def setupUi(self, SaveTeam):
        SaveTeam.setObjectName("SaveTeam")
        SaveTeam.resize(381, 240)
        self.gridLayout = QtWidgets.QGridLayout(SaveTeam)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(SaveTeam)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(SaveTeam)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.Dialog = QtWidgets.QLabel(SaveTeam)
        self.Dialog.setObjectName("Dialog")
        self.gridLayout.addWidget(self.Dialog, 3, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(SaveTeam)
        self.pushButton.setObjectName("pushButton")
        # #self.pushButton.clicked.connect(self.saveteamf)
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)

        self.retranslateUi(SaveTeam)
        QtCore.QMetaObject.connectSlotsByName(SaveTeam)

    # def saveteamf(self):
        #print("new")
        # try:
            # self.t1 = Team(self.p_tup)
            # self.name01 = self.lineEdit.text()
            # self.t1.saveTeam(self.name01)
            # self.Dialog.setText("\tSaved! You Can Close out this Window now")
            # self.lineEdit.setText("")
        # except Exception as e:
            # error = e
            # self.Dialog.setText(str(error))

    def retranslateUi(self, SaveTeam):
        _translate = QtCore.QCoreApplication.translate
        SaveTeam.setWindowTitle(_translate("SaveTeam", "Save"))
        self.label.setText(_translate("SaveTeam", "Enter Team Name : "))
        self.Dialog.setText(_translate("SaveTeam", " "))
        self.pushButton.setText(_translate("SaveTeam", "SAVE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SaveTeam = QtWidgets.QDialog()
    ui = Ui_SaveTeam()
    ui.setupUi(SaveTeam)
    SaveTeam.show()
    sys.exit(app.exec_())
