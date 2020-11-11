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
from datetime import date as dt  # datetime functions
from datetime import timedelta as delta  # difference between two dates

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from change import ChangeRate
from cluster import Cluster
from gdcloss import Graph
from kmeans import KMAnalysis
from scatter import Scatter
from stock import DataInfo, Stock
from stockchart import StockGraph
from svm import Svm


class Test(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # Set initial data for these QComboBoxes of the widget
        # Start Date and End Date for Get Data
        end_date = dt.today()
        differ = delta(days=365)
        start_date = end_date - differ

        # metric and method for Clustering
        metric_items = ['braycurtis', 'canberra', 'chebyshev', 'cityblock', 'correlation', 'cosine', 'euclidean',
                        'hamming', 'jaccard']
        method_items = ['single', 'average', 'complete', 'weighted']

        # Load form file(.ui)
        uic.loadUi('form.ui', self)
        # Set start and end date to QDateEdit
        self.startDate.setDate(start_date)
        self.endDate.setDate(end_date)

        # Set items to these QComboBoxes
        for i in range(9):
            self.metric.addItem(metric_items[i])

        for i in range(4):
            self.method.addItem(method_items[i])

        # construct DataInfo, Stock Classes
        self.wdi = DataInfo()
        self.st = Stock(self.wdi)

        self.getDataButton.clicked.connect(self.ongetdata)
        self.graphButton.clicked.connect(self.ongdbutton)
        self.candleButton.clicked.connect(self.oncandlebutton)
        self.scatterButton.clicked.connect(self.onscatterbutton)
        self.kmButton.clicked.connect(self.onkmbutton)
        self.svmButton.clicked.connect(self.onsvmbutton)
        self.dataButton.clicked.connect(self.ondataButton)
        self.clusterButton.clicked.connect(self.onclusterbutton)
        self.changeButton.clicked.connect(self.onchangebutton)

    def ongetdata(self):
        # Get info from screen widget
        self.st.di.data_type = self.dataType.toPlainText()
        self.st.di.data_source = self.dataSource.toPlainText()
        tuple_start = self.startDate.date().getDate()
        tuple_end = self.endDate.date().getDate()
        self.st.di.start = dt(tuple_start[0], tuple_start[1], tuple_start[2])
        self.st.di.end = dt(tuple_end[0], tuple_end[1], tuple_end[2])
        # self.st.di.setsize(self.duration.value())
        self.st.di.span1 = int(self.span1.value())
        self.st.di.span2 = int(self.span2.value())
        self.st.di.span3 = int(self.span3.value())

        # Stock Data from internet
        self.st.data_read()

        # Post process
        number_record = self.st.df.shape[0]
        self.msgText.setText("データが " + str(number_record) + "件　取得できました！")

        print("GetData process is completed!")

    def ongdbutton(self):

        # Check Stock Data
        if self.st.df.shape[0] == 0:
            self.msgText.setText("先にデータを取得してください。")
            print("GetData is mandatory")
        else:
            # Select Average Method
            if self.sma.isChecked():
                self.wdi.method = "sma"
            elif self.wma.isChecked():
                self.wdi.method = "wma"
            elif self.ewm.isChecked():
                self.wdi.method = "ewm"
            self.st.di.method = self.wdi.method

            # Generate Graph
            Graph(self.st)

        print("GDCross Button was clicked!")

    def oncandlebutton(self):
        if self.st.df.shape[0] == 0:
            self.msgText.setText("先にデータを取得してください。")
            print("GetData is mandatory")
        else:
            StockGraph(self.st)
            print("CandleChart was clicked!")

    def onscatterbutton(self):
        if self.st.df.shape[0] == 0:
            self.msgText.setText("先にデータを取得してください。")
            print("GetData is mandatory")
        else:
            Scatter(self.st)
        print("Scatter Button was clicked!")

    def onkmbutton(self):
        if self.st.df.shape[0] == 0:
            self.msgText.setText("先にデータを取得してください。")
            print("GetData is mandatory")
        else:
            KMAnalysis(self.st)
        print("K-means Button was clicked!")

    def onsvmbutton(self):
        if self.st.df.shape[0] == 0:
            self.msgText.setText("先にデータを取得してください。")
            print("GetData is mandatory")
        else:
            Svm(self.st)
        print("SVM Button was clicked!")

    def ondataButton(self):
        if self.st.df.shape[0] == 0:
            self.msgText.setText("先にデータを取得してください。")
            print("GetData is mandatory")
        else:
            cls1 = Cluster()
            cls1.check_data(self.st)

        print("Data Button was clicked!")

    def onclusterbutton(self):
        if self.st.df.shape[0] == 0:
            self.msgText.setText("先にデータを取得してください。")
            print("GetData is mandatory")
        else:
            select_metric = self.metric.currentText()
            select_method = self.method.currentText()
            cls2 = Cluster()
            cls2.disply_graph(st=self.st, metric=select_metric, method=select_method)

        print("Cluster Button was clicked!")

    def onchangebutton(self):
        if self.st.df.shape[0] == 0:
            self.msgText.setText("先にデータを取得してください。")
            print("GetData is mandatory")
        else:
            ChangeRate(self.st)

        print("Show Change Data Button was clicked!")
