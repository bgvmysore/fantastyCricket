# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pyFiles.openteam import *
from pyFiles.save import *
from pyFiles.eval import *
from pyFiles.classes import *

class myitems(QtWidgets.QListWidgetItem):
    def p_tupleitem(self, tup):
        self.p_tuple = tup
        return

class Ui_MainWindow(object):
    def __init__(self):
        self.p_tupl = []
        self.windowo = QtWidgets.QWidget()
        self.uio = Ui_OpenTeam()
        self.uio.setupUi(self.windowo)
        self.windows = QtWidgets.QWidget()
        self.uis = Ui_SaveTeam()
        self.uis.setupUi(self.windows)
        self.tp = 0
        self.btc = 0
        self.bwc = 0
        self.arc = 0
        self.wkc = 0
        #self.newteamf()
        return
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.p_selc_list = QtWidgets.QListWidget(self.centralwidget)
        self.p_selc_list.setObjectName("p_selc_list")
        self.p_selc_list.itemDoubleClicked.connect(self.removelist2)
        self.gridLayout.addWidget(self.p_selc_list, 7, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.p_list = QtWidgets.QListWidget(self.centralwidget)
        self.p_list.setObjectName("p_list")
        self.p_list.itemDoubleClicked.connect(self.removelist1)
        self.gridLayout.addWidget(self.p_list, 7, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bat_rd = QtWidgets.QRadioButton(self.centralwidget)
        self.bat_rd.setObjectName("bat_rd")
        self.bat_rd.clicked.connect(self.Radiobuttons)
        self.horizontalLayout_3.addWidget(self.bat_rd)
        self.ball_rd = QtWidgets.QRadioButton(self.centralwidget)
        self.ball_rd.setObjectName("ball_rd")
        self.ball_rd.clicked.connect(self.Radiobuttons)
        self.horizontalLayout_3.addWidget(self.ball_rd)
        self.ar_rd = QtWidgets.QRadioButton(self.centralwidget)
        self.ar_rd.setObjectName("ar_rd")
        self.ar_rd.clicked.connect(self.Radiobuttons)
        self.horizontalLayout_3.addWidget(self.ar_rd)
        self.wkt_rd = QtWidgets.QRadioButton(self.centralwidget)
        self.wkt_rd.setObjectName("wkt_rd")
        self.wkt_rd.clicked.connect(self.Radiobuttons)
        self.horizontalLayout_3.addWidget(self.wkt_rd)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.teampoints = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.teampoints.setFont(font)
        self.teampoints.setObjectName("teampoints")
        self.horizontalLayout_2.addWidget(self.teampoints)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.bat_cnt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bat_cnt.setFont(font)
        self.bat_cnt.setObjectName("bat_cnt")
        self.horizontalLayout.addWidget(self.bat_cnt)
        self.ball_cnt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ball_cnt.setFont(font)
        self.ball_cnt.setObjectName("ball_cnt")
        self.horizontalLayout.addWidget(self.ball_cnt)
        self.bat_cnt_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bat_cnt_2.setFont(font)
        self.bat_cnt_2.setObjectName("bat_cnt_2")
        self.horizontalLayout.addWidget(self.bat_cnt_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.bat_cnt_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bat_cnt_3.setFont(font)
        self.bat_cnt_3.setObjectName("bat_cnt_3")
        self.horizontalLayout.addWidget(self.bat_cnt_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.bat_cnt_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bat_cnt_4.setFont(font)
        self.bat_cnt_4.setObjectName("bat_cnt_4")
        self.horizontalLayout.addWidget(self.bat_cnt_4)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionEvaluate_team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_team.setObjectName("actionEvaluate_team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEvaluate_team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)
        self.uio.listWidget.itemDoubleClicked.connect(self.selectionop)
        self.uis.pushButton.clicked.connect(self.thisis)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def thisis(self):
        print("mainwindow")
        try:
            self.t1 = Team(self.p_tupl)
            self.name01 = self.uis.lineEdit.text()
            self.t1.saveTeam(self.name01)
            self.uis.Dialog.setText("\tSaved! You Can Close out this Window now")
            self.uis.lineEdit.setText("")
            self.label_6.setText(f"Team Name: {self.name01}")
        except Exception as e:
            error = e
            self.uis.Dialog.setText(str(error))
    def selectionop(self, item):
        self.uio.teamselected = item.text()
        self.tp = 0
        self.btc = 0
        self.bwc = 0
        self.arc = 0
        self.wkc = 0
        print(self.uio.teamselected)
        self.loadt1 = Team()
        self.loadt1.LoadTeam(self.uio.teamselected)
        self.p_list.clear()
        self.p_selc_list.clear()
        self.ar_tup = []
        self.bat_tup = []
        self.bwl_tup = []
        self.wk_tup = []
        for i in self.loadt1.teamlist:
            xx = myitems(i[0]+f"  ({i[-2]}P)")
            xx.p_tupleitem(i)
            self.p_selc_list.addItem(xx)
            self.tp += i[-2]
            if i[-1] == 'BAT':
                self.btc += 1
                self.bat_cnt.setText(str(self.btc))
            if i[-1] == 'BWL':
                self.bwc += 1
                self.bat_cnt_2.setText(str(self.bwc))
            if i[-1] == 'AR':
                self.arc += 1
                self.bat_cnt_3.setText(str(self.arc))
            if i[-1] == 'WK':
                self.wkc += 1
                self.bat_cnt_4.setText(str(self.wkc))
        self.teampoints.setText(str(self.tp))
        self.label_6.setText("Team Name: "+str(self.uio.teamselected))
        self.windowo.close()
    
    def load_selec(self):
        self.p_tupl = []
        for i in range( self.p_selc_list.count() ):
            xx = self.p_selc_list.item(i)
            self.p_tupl += [xx.p_tuple]
    
    def removelist1(self,item):
        self.p_list.takeItem(self.p_list.row(item))
        self.p_selc_list.addItem(item)
        self.tp += item.p_tuple[-2]
        self.teampoints.setText(str(self.tp))
        if item.p_tuple[-1] == 'BAT':
            self.btc += 1
            self.bat_cnt.setText(str(self.btc))
        if item.p_tuple[-1] == 'BWL':
            self.bwc += 1
            self.bat_cnt_2.setText(str(self.bwc))
        if item.p_tuple[-1] == 'AR':
            self.arc += 1
            self.bat_cnt_3.setText(str(self.arc))
        if item.p_tuple[-1] == 'WK':
            self.wkc += 1
            self.bat_cnt_4.setText(str(self.wkc))
        
    
    def removelist2(self,item):
        self.p_selc_list.takeItem(self.p_selc_list.row(item))
        self.p_list.addItem(item)
        self.tp = self.tp - item.p_tuple[-2]
        self.teampoints.setText(str(self.tp))
        if item.p_tuple[-1] == 'BAT':
            self.btc -= 1
            self.bat_cnt.setText(str(self.btc))
        if item.p_tuple[-1] == 'BWL':
            self.bwc -= 1
            self.bat_cnt_2.setText(str(self.bwc))
        if item.p_tuple[-1] == 'AR':
            self.arc -= 1
            self.bat_cnt_3.setText(str(self.arc))
        if item.p_tuple[-1] == 'WK':
            self.wkc -= 1
            self.bat_cnt_4.setText(str(self.wkc))
        
    def get_p_list(self):
        self.bat_tup = []
        self.bwl_tup = []
        self.ar_tup = []
        self.wk_tup = []
        self.p_tuple_show = []
        self.p_tuple_hidden = []
        for i in self.p1.p_tuple:
            if i[-1] == 'BAT':
                x = myitems(i[0]+f"  ({i[-2]}P)")
                x.p_tupleitem(i)
                self.bat_tup += [x] 
                pass
            if i[-1] == 'BWL':
                x = myitems(i[0]+f"  ({i[-2]}P)")
                x.p_tupleitem(i)
                self.bwl_tup += [x]
                pass
            if i[-1] == 'AR':
                x = myitems(i[0]+f"  ({i[-2]}P)")
                x.p_tupleitem(i)
                self.ar_tup += [x]
                pass
            if i[-1] == 'WK':
                x = myitems(i[0]+f"  ({i[-2]}P)")
                x.p_tupleitem(i)
                self.wk_tup += [x]
      
            # x = myitems(i[0]+f"  ({i[-2]}P)")
            # x.p_tupleitem(i)
            # self.p_list.addItem(x)
        return
    
    def newteamf(self):
        self.tp = 0
        self.btc = 0
        self.bwc = 0
        self.arc = 0
        self.wkc = 0
        self.label_6.setText("Team Name : New Team")
        self.p_list.clear()
        self.p_selc_list.clear()
        self.p1 = Players()
        self.get_p_list()
        self.teampoints.setText(str(self.tp))
        self.bat_cnt.setText(str(self.btc))
        self.bat_cnt_2.setText(str(self.bwc))
        self.bat_cnt_3.setText(str(self.arc))
        self.bat_cnt_4.setText(str(self.wkc))
    
    def showpop(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Team should have:\n1) 11 players\n2) 1 Wicket Keeper\n3) Teampoints <= 1000")
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()
    
    def savteamf(self):
        self.load_selec()
        dummy = 0
        for i in self.p_tupl:
            if i[-1] == 'WK':
                dummy += 1
        
        if not len(self.p_tupl) == 11:
            self.showpop()
        elif not(dummy == 1):
            self.showpop()
        elif self.tp > 1000:
            self.showpop()
        else:
            # self.windows = QtWidgets.QWidget()
            # self.uis = Ui_SaveTeam(self.p_tupl)
            # self.uis.setupUi(self.windows)
            self.windows.show()

    def openteamf(self):
        
        # self.windowo = QtWidgets.QWidget()
        # self.uio = Ui_OpenTeam()
        # self.uio.setupUi(self.windowo)
        self.openwindow = True
        # print(self.uis.name01)
        self.windowo.show()
        
    def evalteamf(self):
        self.load_selec()
        dummy = 0
        for i in self.p_tupl:
            if i[-1] == 'WK':
                dummy += 1
        if not len(self.p_tupl) == 11:
            self.showpop()
        elif not(dummy == 1):
            self.showpop()
        elif self.tp > 1000:
            self.showpop()
        else:
            self.window = QtWidgets.QWidget()
            self.ui = Ui_Evaluate(self.p_tupl)
            self.ui.setupUi(self.window)
            self.window.show()
        
    def menufunction(self, action):
        txt = (action.text())
        if txt == 'New Team':
            self.newteamf()
        if txt == 'Save Team':
            self.savteamf()
        if txt == 'Open Team':
            self.openteamf()
        if txt == 'Evaluate team':
            self.evalteamf()
        return
    
    def Radiobuttons(self):
     for i in range(4):
        self.Radiobuttons1()
     return
  
    def Radiobuttons1(self):
        
        if self.bat_rd.isChecked() == True:
            for i in range( self.p_list.count() ):
                self.p_list.takeItem(i)
            for i in self.bat_tup :
                self.p_list.addItem(i)
            self.ball_rd.setChecked(False)
            self.ar_rd.setChecked(False)
            self.wkt_rd.setChecked(False)            
        
        if self.ball_rd.isChecked() == True:
            for i in range( self.p_list.count() ):
                self.p_list.takeItem(i)
            for i in self.bwl_tup :
                self.p_list.addItem(i)
            self.ar_rd.setChecked(False)
            self.wkt_rd.setChecked(False)
            self.bat_rd.setChecked(False)

        if self.ar_rd.isChecked() == True:
            for i in range( self.p_list.count() ):
                self.p_list.takeItem(i)
            for i in self.ar_tup :
                self.p_list.addItem(i)
            self.wkt_rd.setChecked(False)
            self.bat_rd.setChecked(False)
            self.ball_rd.setChecked(False)
                
        if self.wkt_rd.isChecked() == True:
            for i in range( self.p_list.count() ):
                self.p_list.takeItem(i)
            for i in self.wk_tup :
                self.p_list.addItem(i)
            self.bat_rd.setChecked(False)
            self.ball_rd.setChecked(False)
            self.ar_rd.setChecked(False)
        
        return
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Your Selection:"))
        self.bat_rd.setText(_translate("MainWindow", "BAT"))
        self.ball_rd.setText(_translate("MainWindow", "BOWL"))
        self.ar_rd.setText(_translate("MainWindow", "AR"))
        self.wkt_rd.setText(_translate("MainWindow", "WKT"))
        self.label_5.setText(_translate("MainWindow", "Total Points:"))
        self.teampoints.setText(_translate("MainWindow", "###"))
        self.label_7.setText(_translate("MainWindow", "Max Points: 1000"))
        self.label.setText(_translate("MainWindow", "BAT:"))
        self.bat_cnt.setText(_translate("MainWindow", "##"))
        self.ball_cnt.setText(_translate("MainWindow", "BOWL:"))
        self.bat_cnt_2.setText(_translate("MainWindow", "##"))
        self.label_3.setText(_translate("MainWindow", "AR:"))
        self.bat_cnt_3.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "WK:"))
        self.bat_cnt_4.setText(_translate("MainWindow", "##"))
        self.label_8.setText(_translate("MainWindow", "Available Players:"))
        self.label_6.setText(_translate("MainWindow", "Team Name : New Team"))
        self.label_9.setText(_translate("MainWindow", "Selected Players:"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionEvaluate_team.setText(_translate("MainWindow", "Evaluate team"))
        self.newteamf()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
