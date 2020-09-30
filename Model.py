from PyQt5 import QtCore
import typing


class Model (QtCore.QAbstractItemModel):
    def __init__(self, datain=None, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.myTable = datain or []

#  Дописать условие если данных нет
    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int:
        return len(self.myTable)

    def columnCount(self, parent: QtCore.QModelIndex = ...) -> int:
        return 3

    def parent(self, child:QtCore.QModelIndex) -> QtCore.QModelIndex:
        return QtCore.QModelIndex()

    def index(self, row: int, column: int, parent: QtCore.QModelIndex = ...) -> QtCore.QModelIndex:
        if self.hasIndex(row, column):
            return self.createIndex(row, column)
        else:
            return QtCore.QModelIndex()

    def data(self, index: QtCore.QModelIndex, role: int = ...) -> typing.Any:
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return QtCore.QVariant(self.myTable[index.row()][index.column()])

    def setData(self, index: QtCore.QModelIndex, value: typing.Any, role: int = ...) -> bool:
        print('setData works')
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                self.myTable[index.row()][index.column()] = value
                return self.myTable[index.row()][index.column()]

    def insertRows(self, row: int, count: int, parent: QtCore.QModelIndex = ...) -> bool:
        print("insertRows on")
