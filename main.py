import sys
from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    print('main start')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    app.exec_()
