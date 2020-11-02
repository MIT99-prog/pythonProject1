# -------------------------------------------------------------------------------
# Name:        company_stock
# Purpose:     to test functions about stock analysis
#
# Author:      tango
#
# Created:     26/10/2020
# Copyright:   (c) tango 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import matplotlib.pyplot as plt

from stock import Stock, DataInfo


class Graph:
    def __init__(self, st: Stock, di: DataInfo):
        self.date = []
        self.price = []
        self.avg01 = []
        self.avg02 = []
        self.avg03 = []
        self.volume = []
        self.generate_graph(st, di)

    def generate_graph(self, st, di):
        self.date = st.df.index
        # set analysis values
        # set analysis values
        if di.data_source == "yahoo":
            self.price = st.df['Adj Close']  # from yahoo
        elif di.data_source == "stooq":
            self.price = st.df['Close']  # from stooq
        else:
            self.price = st.df['Close']  # other

        # set values for the graph
        self.avg01 = st.df['avg05days']
        self.avg02 = st.df['avg25days']
        self.avg03 = st.df['avg50days']

        self.volume = st.df['Volume']

        # plot data
        plt.figure(figsize=(20, 10))
        plt.subplot(2, 1, 1)

        plt.title("Stock Price Chart " + di.data_type + " - " + str(di.method), loc='left')
        plt.xlabel('Date')
        plt.ylabel('Price (JPY)')

        # plot price data
        plt.plot(self.date, self.price, label='Price', color='pink')
        plt.plot(self.date, self.avg01, label='Avg05days', color='blue')
        plt.plot(self.date, self.avg02, label='Avg25days', color='green')
        plt.plot(self.date, self.avg03, label='Avg50days', color='purple')

        plt.legend()

        plt.subplot(2, 1, 2)
        plt.title('Stock Volume Chart', loc='left')
        plt.xlabel('Date')
        plt.ylabel('Volume (Unit)')

        plt.bar(self.date, self.volume, label='Volume', color='grey')
        plt.legend()

        # display
        plt.show()
