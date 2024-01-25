# -- coding:utf-8 --
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from ui2py.SudokuSolverWidget import Ui_SolverWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    Ui = Ui_SolverWidget()
    Ui.setupUi(MainWindow)

    MainWindow.setWindowIcon(QIcon('./static/icon.png'))
    MainWindow.show()
    sys.exit(app.exec_())
