import sys
from PyQt5 import QtWidgets

from GUI.py.timer_widget import Ui_Form


class MainWindowQt(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = MainWindowQt()
window.show()
sys.exit(app.exec_())
