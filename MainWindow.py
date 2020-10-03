# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Model import Model


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(371, 382)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(371, 382))
        MainWindow.setMaximumSize(QtCore.QSize(371, 382))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 0, 0, 1, 1)
        self.change_button = QtWidgets.QPushButton(self.centralwidget)
        self.change_button.setObjectName("change_button")
        self.gridLayout.addWidget(self.change_button, 0, 1, 1, 1)
        self.de_button = QtWidgets.QPushButton(self.centralwidget)
        self.de_button.setObjectName("de_button")
        self.gridLayout.addWidget(self.de_button, 0, 2, 1, 1)
        self.tableview = QtWidgets.QTableView(self.centralwidget)
        self.tableview.setObjectName("tableview")
        self.gridLayout.addWidget(self.tableview, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_action = QtWidgets.QAction(MainWindow)
        self.open_action.setEnabled(True)
        self.open_action.setWhatsThis("")
        self.open_action.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.open_action.setObjectName("open_action")
        self.save_action = QtWidgets.QAction(MainWindow)
        self.save_action.setObjectName("save_action")
        self.exit_action = QtWidgets.QAction(MainWindow)
        self.exit_action.setObjectName("exit_action")
        self.menu.addAction(self.open_action)
        self.menu.addAction(self.save_action)
        self.menu.addAction(self.exit_action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task1_Var5"))
        self.add_button.setStatusTip(_translate("MainWindow", "\"Add new string\""))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.change_button.setStatusTip(_translate("MainWindow", "\"Change selected string\""))
        self.change_button.setText(_translate("MainWindow", "Change"))
        self.de_button.setStatusTip(_translate("MainWindow", "\"Delete selected string\""))
        self.de_button.setText(_translate("MainWindow", "Delete"))
        self.menu.setStatusTip(_translate("MainWindow", "\"File menu\""))
        self.menu.setWhatsThis(_translate("MainWindow", "Menu for working with file"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.open_action.setText(_translate("MainWindow", "Open"))
        self.open_action.setStatusTip(_translate("MainWindow", "\"Open existing  file\""))
        self.save_action.setText(_translate("MainWindow", "Save"))
        self.save_action.setStatusTip(_translate("MainWindow", "\"Save current file\""))
        self.exit_action.setText(_translate("MainWindow", "Exit"))
        self.exit_action.setStatusTip(_translate("MainWindow", "\"exit\""))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.model = Model([['ass', 'dddd', 'asd']])
        self.tableview.setModel(self.model)
        self.model.setData(['my', 'back', 'hurts'])
        #self.model.insertRows(1, 1)

        #self.model.removeRow(1)

    def writeToFile (self, fileName: str):
        file = QtCore.QFile(fileName)

        if not file.open(QtCore.QIODevice.WriteOnly):
            QtWidgets.QMessageBox.information("Unable to open file", file.errorString())
            return

        data = self.model.getTable()
        out = QtCore.QDataStream(file)

        out << data

    def readFromFile(self, fileName: str):
        file = QtCore.QFile(fileName)

        if not file.open(QtCore.QIODevice.ReadOnly):
            QtWidgets.QMessageBox.information("Unable to open file")
            file.errorString()
            return

        data = self.model.getTable()
        dataIn = QtCore.QDataStream(file)

        dataIn >> data

        #if len(data) == 0:
        #    QtWidgets.QMessageBox.information("No Names in file")



