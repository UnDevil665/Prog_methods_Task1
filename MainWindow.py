# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import xml.etree.ElementTree as ET
from PyQt5 import QtCore, QtGui, QtWidgets
from Model import Model


class Ui_MainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(371, 382)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(371, 382))
        mainWindow.setMaximumSize(QtCore.QSize(10000, 10000))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
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
        self.listview = QtWidgets.QListView(self.centralwidget)
        self.listview.setObjectName("listview")
        self.gridLayout.addWidget(self.listview, 1, 0, 1, 3)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.open_action = QtWidgets.QAction(mainWindow)
        self.open_action.setEnabled(True)
        self.open_action.setWhatsThis("")
        self.open_action.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.open_action.setObjectName("open_action")
        self.save_action = QtWidgets.QAction(mainWindow)
        self.save_action.setObjectName("saveAs_action")
        self.saveAs_action = QtWidgets.QAction(mainWindow)
        self.saveAs_action.setObjectName("saveAs_action")
        self.exit_action = QtWidgets.QAction(mainWindow)
        self.exit_action.setObjectName("exit_action")
        self.menu.addAction(self.open_action)
        self.menu.addAction(self.save_action)
        self.menu.addAction(self.saveAs_action)
        self.menu.addAction(self.exit_action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Task1_Var5"))
        self.add_button.setStatusTip(_translate("mainWindow", "\"Add new string\""))
        self.add_button.setText(_translate("mainWindow", "Add"))
        self.change_button.setStatusTip(_translate("mainWindow", "\"Change selected string\""))
        self.change_button.setText(_translate("mainWindow", "Change"))
        self.de_button.setStatusTip(_translate("mainWindow", "\"Delete selected string\""))
        self.de_button.setText(_translate("mainWindow", "Delete"))
        self.menu.setStatusTip(_translate("mainWindow", "\"File menu\""))
        self.menu.setWhatsThis(_translate("mainWindow", "Menu for working with file"))
        self.menu.setTitle(_translate("mainWindow", "File"))
        self.open_action.setText(_translate("mainWindow", "Open"))
        self.open_action.setStatusTip(_translate("mainWindow", "\"Open existing  file\""))
        self.save_action.setText(_translate("mainWindow", "Save"))
        self.save_action.setStatusTip(_translate("mainWindow", "\"Save current file\""))
        self.saveAs_action.setText(_translate("mainWindow", "Save as ..."))
        self.saveAs_action.setStatusTip(_translate("mainWindow", "\"Save current file as ...\""))
        self.exit_action.setText(_translate("mainWindow", "Exit"))
        self.exit_action.setStatusTip(_translate("mainWindow", "\"exit\""))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.model = Model()
        self.listview.setModel(self.model)

        self.open_action.triggered.connect(self.readFromFile)
        self.save_action.triggered.connect(self.writeToFile)
        self.add_button.pressed.connect(self.addElement)
        #self.change_button.pressed.connect(self.changeElement)

    def insertItem(self, row: int, newitem, column: int = 0):
        self.model.insertRows()
        index = self.model.index(row, column)

        self.model.setData(index, newitem)

    def addItem(self, newitem):
        row = self.model.rowCount()
        column = 0

        print(row, " ", column)
        self.model.insertRows()
        index = self.model.index(row, column)

        self.model.setData(index, newitem)

    def writeToFile(self, filename: str):
        savedialog = QtWidgets.QFileDialog(self)
        savedialog.setFileMode(savedialog.AnyFile)
        savedialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)

        filename, sfilter = savedialog.getOpenFileName(self, "Выбор файла для сохранения")
        file = QtCore.QFile(filename)

        if not file.open(QtCore.QIODevice.Append):
            QtWidgets.QMessageBox.information(self, "Unable to save file", file.errorString())
            return

        data = self.model.getList()

        for i in data:
            for j in i:
                file.write()

    def readFromFile(self, filename: str):
        opendialog = QtWidgets.QFileDialog(self)
        opendialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)

        filename, sfilter = opendialog.getOpenFileName(self, "Выбор файла для открытия")
        file = QtCore.QFile(filename)

        if not file.open(QtCore.QIODevice.ReadOnly) and filename is True:
            QtWidgets.QMessageBox.information(self, "Unable to open file", file.errorString())
            file.errorString()
            return

        xfile = QtCore.QFile(filename)
        if xfile.open(QtCore.QFile.ReadOnly or QtCore.QFile.Text):
            fxml = ET.parse(filename).getroot()
            persons = fxml.findall('person')

            for p in persons:
                input = p.text()

                print(self.model.myList)
                self.addItem(input)
        xfile.close()

        return filename

    def addElement(self):
        row = self.model.rowCount()
        self.model.insertRows()

        index = self.model.index(row)

        self.model.setData(index, 'my ass fuu', 0)

        # edit = QtWidgets.QItemDelegate(self)
        #
        # edit.createEditor(self, QtWidgets)
        # edit.setEditorData()

    def changeElement(self):
        print("change_element works")
        # delegate = Delegate(self)
        # self.listview.setItemDelegate(delegate)


        row = 0
        column = 0

        index = self.model.index(row, column)
        # editor = delegate.createEditor(self.listview, index)
        # delegate.setEditorData(index, editor)
        #
        # delegate.setModelData(editor, self.model, index)
        #
        # print(self.model.flags(index))


class Delegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        print("init works")
        super().__init__(parent)

    def createEditor(self, parent: QtWidgets.QWidget, index: QtCore.QModelIndex,
                     option: QtWidgets.QStyleOptionViewItem = None) -> QtWidgets.QWidget:
        print("createworks")
        self.dlineedit = QtWidgets.QLineEdit(parent)
        return self.dlineedit

    # Передача данных в редактор
    def setEditorData(self, index: QtCore.QModelIndex, editor: QtWidgets.QWidget) -> None:
        value = index.model().data(index, QtCore.Qt.EditRole)

        print(value)
        self.dlineedit.setText(value)
        print(self.dlineedit.text())
        print("seteditor works")

    def setModelData(self, editor: QtWidgets.QWidget, model: QtCore.QAbstractItemModel,
                     index: QtCore.QModelIndex) -> None:
        if not editor.hasFocus():
            model.setData(index, self.dlineedit.text())
            print("setmodel works")
