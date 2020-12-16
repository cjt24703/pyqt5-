import sys
from PyQt5.QtWidgets import QApplication

from TMainWindow import TMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    TMainWindow = TMainWindow()
    TMainWindow.show()
    app.exec_()

