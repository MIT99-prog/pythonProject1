# -------------------------------------------------------------------------------
# Name:        widget
# Purpose:     to test functions of QtWidget of PyQt5
#
# Author:      tango
#
# Created:     26/10/2020
# Copyright:   (c) tango 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from stock import DataInfo, Stock, Graph


class Test(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi('form.ui', self)
        self.di = DataInfo()

        self.graphButton.clicked.connect(self.ongButtonclicked)

    def ongButtonclicked(self):

        self.di.data_type = self.dataType.toPlainText()
        self.di.data_source = self.dataSource.toPlainText()
        self.di.data_size = self.di.setsize(self.duration.value())
        if self.sma.isChecked():
            self.di.method = 1
        elif self.wma.isChecked():
            self.di.method = 2
        elif self.ewm.isChecked():
            self.di.method = 3
        else:
            self.di.method = 1  # temporally

        print("Graph Button was clicked!")

        # data set and calc average
        st = Stock(self.di)

        # generate graph
        Graph(st, self.di)

