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
        self.wdi = DataInfo()
        self.st = Stock(self.wdi)

        self.getDataButton.clicked.connect(self.ongetdata)
        self.graphButton.clicked.connect(self.ongdbutton)
        self.candleButton.clicked.connect(self.oncandlebutton)
        self.scatterButton.clicked.connect(self.onscatterbutton)

    def ongetdata(self):

        self.st.di.data_type = self.dataType.toPlainText()
        self.st.di.data_source = self.dataSource.toPlainText()
        self.st.di.setsize(self.duration.value())

        self.st.data_read()
        print("GetData is completed!")

    def ongdbutton(self):

        # Select Average Method
        if self.sma.isChecked():
            self.wdi.method = "sma"
        elif self.wma.isChecked():
            self.wdi.method = "wma"
        elif self.ewm.isChecked():
            self.wdi.method = "ewm"
        else:
            self.wdi.method = "sma"  # temporally

        # generate graph
        if self.st == none:
            print("GetData is mandatory")
        else:
            self.st.di.method = self.wdi.method
            Graph(self.st)
        print("GDCross Button was clicked!")

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
