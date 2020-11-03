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
from numpy.distutils.fcompiler import none

from gdcloss import Graph
from scatter import Scatter
from stock import DataInfo, Stock
from stockchart import StockGraph


class Test(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi('form.ui', self)
        self.di = DataInfo()
        self.st = none

        self.getDataButton.clicked.connect(self.ongetdata)
        self.graphButton.clicked.connect(self.ongraphbutton)
        self.candleButton.clicked.connect(self.oncandlebutton)
        self.scatterButton.clicked.connect(self.onscatterbutton)

    def ongetdata(self):

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

        self.st = Stock(self.di)
        print("GetData is completed!")

    def ongraphbutton(self):

        # generate graph
        if self.st == none:
            print("GetData is mandatory")
        else:
            Graph(self.st, self.di)
        print("Graph Button was clicked!")

    def oncandlebutton(self):
        if self.st == none:
            print("GetData is mandatory")
        else:
            StockGraph(self.st)
            print("CandleChart was clicked!")

    def onscatterbutton(self):
        if self.st == none:
            print("GetData is mandatory")
        else:
            Scatter(self.st)
        print("Scatter Button was clicked!")