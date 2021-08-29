from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic
import math
import os

os.environ['QT_MAC_WANTS_LAYER'] = '1'

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# CalUI = "./calculator_ui.ui"
CalUI = resource_path("./calculator.ui")

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)

        self.equalbutton.clicked.connect(self.calculate)

    def calculate(self):
        foo = self.inputbox.text()
        result = eval(foo)
        result_for_history = "{}\n= {}\n".format(foo, result)
        self.history.append(result_for_history)
        self.inputbox.clear()


QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())

