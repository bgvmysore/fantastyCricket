# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpenTeam.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pyFiles.classes import *


class Ui_OpenTeam(object):
    def __init__(self):
        self.t1 = Team()
        self.listofallteams = Team.teams

    def setupUi(self, OpenTeam):
        OpenTeam.setObjectName("OpenTeam")
        OpenTeam.resize(314, 164)
        self.verticalLayout = QtWidgets.QVBoxLayout(OpenTeam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(OpenTeam)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(OpenTeam)
        self.listWidget.setObjectName("listWidget")
        #self.listWidget.itemDoubleClicked.connect(self.selection)
        self.verticalLayout.addWidget(self.listWidget)
        for i in self.listofallteams:
            self.listWidget.addItem(i)

        self.retranslateUi(OpenTeam)
        QtCore.QMetaObject.connectSlotsByName(OpenTeam)

    def retranslateUi(self, OpenTeam):
        _translate = QtCore.QCoreApplication.translate
        OpenTeam.setWindowTitle(_translate("OpenTeam", "Open"))
        self.label.setText(_translate("OpenTeam", "Double Click to Open:"))

    # def selection(self, item):
        # self.teamselected = item.text()
        # print(self.teamselected)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenTeam = QtWidgets.QDialog()
    ui = Ui_OpenTeam()
    ui.setupUi(OpenTeam)
    OpenTeam.show()
    sys.exit(app.exec_())
