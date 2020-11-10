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
        metricItems = ['braycurtis', 'canberra', 'chebyshev', 'cityblock', 'correlation', 'cosine', 'euclidean', 'hamming',
                  'jaccard']
        methodItems = ['single', 'average', 'complete', 'weighted']

        # Load form file(.ui)
        uic.loadUi('form.ui', self)

        #Set items to these QComboBoxes
        for i in range(9):
            self.metric.addItem(metricItems[i])
        for i in range(4):
            self.method.addItem(methodItems[i])
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

        self.st.di.data_type = self.dataType.toPlainText()
        self.st.di.data_source = self.dataSource.toPlainText()
        self.st.di.setsize(self.duration.value())

        self.st.data_read()
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
            selectMetric = self.metric.currentText()
            selectMethod = self.method.currentText()
            cls2 = Cluster()
            cls2.disply_graph(st=self.st, metric=selectMetric, method=selectMethod)

        print("Cluster Button was clicked!")

    def onchangebutton(self):
        if self.st.df.shape[0] == 0:
            self.msgText.setText("先にデータを取得してください。")
            print("GetData is mandatory")
        else:
            ChangeRate(self.st)

        print("Show Change Data Button was clicked!")