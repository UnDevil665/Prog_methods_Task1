from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
import typing
import PyQt5


class Model (QtCore.QAbstractItemModel):
    def __init__(self, datain=None, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.myList = []

#  Дописать условие если данных нет
    def rowCount(self, parent=QtCore.QModelIndex()) -> int:
        return len(self.myList)

    def columnCount(self, parent=QtCore.QModelIndex()) -> int:
        return 1

    def parent(self, child: QtCore.QModelIndex) -> QtCore.QModelIndex:
        return QtCore.QModelIndex()

    def index(self, row: int, column: int = 0, parent=QtCore.QModelIndex()) -> QtCore.QModelIndex:
        if self.hasIndex(row, column):
            return self.createIndex(row, column)
        else:
            return QtCore.QModelIndex()

    def data(self, index: QtCore.QModelIndex, role: int = ...) -> typing.Any:
        if not index.isValid():
            return QtCore.QVariant()

        if (index.row() >= len(self.myList)) or (index.row() < 0):
            return QtCore.QVariant()

        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            datas = self.myList[index.row()]

            return datas

    def setData(self, index: QtCore.QModelIndex, value, role: int = 0) -> bool:
        print('setData works')

        if index.isValid():
            row = index.row()

            self.myList[row] = value
            return True
        else:
            return False

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if not role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if Qt.Orientation == Qt.Horizontal:
            if section == 0:
                return 'Data'
            else:
                return None
        return None

    def insertRows(self, row: int = None, count: int = 1, parent=QtCore.QModelIndex()) -> bool:
        print("insertRows on")
        if row is None:
            row = self.rowCount()

        self.beginInsertRows(parent, row, count + row - 1,)

        for i in range(count):
            self.myList.insert(row, "")

        self.endInsertRows()
        return True

    def insertRow(self, row: int, parent=QtCore.QModelIndex()) -> bool:
        print("insertRow on")

        self.myList.insert(row, "")

        return True

    def removeRows(self, row: int, count: int = 1, parent=QtCore.QModelIndex()) -> bool:
        print("removeRows on")

        self.beginRemoveRows(parent, row, count + row - 1)

        for i in range(count):
            self.myList.pop(row - 1)

        self.endRemoveRows()
        print(self.myList)
        return True

    def removeRow(self, row: int, parent=QtCore.QModelIndex()) -> bool:
        print('removeRow on')

        self.removeRows(row, 1)

        return True

    def flags(self, index: QtCore.QModelIndex):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable

    def getList(self):
        return self.myList

