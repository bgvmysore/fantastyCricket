# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pyFiles.classes import *

class myitems(QtWidgets.QListWidgetItem):
    def p_tupleitem(self, tup):
        self.p_tuple = tup
        return

class Ui_Evaluate(object):
    def __init__(self, p_tupl):
        self.p_tup = p_tupl
        self.t1 = Team(p_tupl)
        conn = ConDB()
        self.listofMatches = conn.listofmatches()

    def setupUi(self, Evaluate):
        Evaluate.setObjectName("Evaluate")
        Evaluate.resize(526, 458)
        self.gridLayout = QtWidgets.QGridLayout(Evaluate)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Evaluate)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Evaluate)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(Evaluate)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 2, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(Evaluate)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Evaluate)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Evaluate)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Evaluate)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(Evaluate)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnstate)
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 3)

        for i in self.listofMatches:
            self.comboBox.addItem(i)

        for i in self.p_tup:
            x = myitems(i[0]+f"\t{i[-2]}P\t{i[-1]}")
            x.p_tupleitem(i)
            self.listWidget.addItem(x)

        self.retranslateUi(Evaluate)
        QtCore.QMetaObject.connectSlotsByName(Evaluate)

    def btnstate(self):
            self.listWidget_2.clear()
            match = self.comboBox.currentText()
            self.m1 = Matches(match)
            self.m1.teamscores(self.t1)
            self.label_4.setText(str(self.m1.teammatchscore))
            for i in self.m1.teamscores_list:
                self.listWidget_2.addItem(str(i[-1]))
            return

    def retranslateUi(self, Evaluate):
        _translate = QtCore.QCoreApplication.translate
        Evaluate.setWindowTitle(_translate("Evaluate", "Evaluate"))
        self.label_2.setText(_translate("Evaluate", "Players:"))
        self.label_3.setText(_translate("Evaluate", "Scores:"))
        self.label_4.setText(_translate("Evaluate", "###"))
        self.label.setText(_translate("Evaluate", "Select Match:"))
        self.pushButton.setText(_translate("Evaluate", "Evaluate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Evaluate = QtWidgets.QWidget()
    ui = Ui_Evaluate()
    ui.setupUi(Evaluate)
    Evaluate.show()
    sys.exit(app.exec_())
