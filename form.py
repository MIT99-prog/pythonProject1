# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUi

from widget import Test

"""
class Test(QWidget):
    def __init__(self):
        # super(Test, self).__init__()
        QWidget.__init__(self)
        loadUi('form.ui', self)
        # self.slot1
        self.graphButton.clicked.connect(self.ongraphButtonClicked())

    def ongraphButtonClicked(self):
        print("graphButton was pressed!")
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Test()
    widget.show()

    sys.exit(app.exec_())
