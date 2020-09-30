from PyQt5 import QtCore
import typing


class Model (QtCore.QAbstractItemModel):
    def __init__(self, datain=None, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.myTable = datain or [[]]

#  Дописать условие если данных нет
    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int:
        return len(self.myTable)

    def columnCount(self, parent: QtCore.QModelIndex = ...) -> int:
        return 3

    def parent(self, child: QtCore.QModelIndex) -> QtCore.QModelIndex:
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

    def setData(self, value: typing.Any, role: int = 2, index=QtCore.QModelIndex()) -> bool:
        print('setData works')
        if index.isValid() & role == QtCore.Qt.DisplayRole:
            self.myTable[index.row()][index.column()] = value
            return True
        else:
            return False

    def insertRows(self, row: int, count: int, parent=QtCore.QModelIndex()) -> bool:
        print("insertRows on")

        self.beginInsertRows(parent, row, count + row - 1,)

        for i in range(count):
            self.myTable.insert(row, ["", "", ""])

        self.endInsertRows()
        return True

    def insertRow(self, row: int, parent=QtCore.QModelIndex()) -> bool:
        print("insertRow on")

        self.myTable.insert(row, "")

    def removeRows(self, row: int, count: int, parent=QtCore.QModelIndex()) -> bool:
        print("removeRows on")

        self.beginRemoveRows(parent, row, count + row - 1)

        for i in range(count):
            self.myTable.pop(row)

        self.endRemoveRows()

        return True

    def removeRow(self, row: int, parent=QtCore.QModelIndex()) -> bool:
        print('removeRow on')

        self.removeRows(row, 1)

        return True
