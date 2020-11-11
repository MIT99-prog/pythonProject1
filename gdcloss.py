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
from numpy.distutils.fcompiler import none

from stock import Stock

"""
class Span:

    def __init__(self):
        # super().__init__()
        self.span01 = 3
        self.span02 = 14
        self.span03 = 30
"""


class Graph:
    def __init__(self, st: Stock):
        self.date = []
        self.price = []
        self.avg01 = []
        self.avg02 = []
        self.avg03 = []
        self.volume = []
        self.calc = none

        # self.setavg(st)
        self.generate_graph(st)

    def generate_graph(self, st):

        # set analysis values

        """
        if st.di.data_source == "yahoo":
            self.price = st.df['Adj Close']  # from yahoo
        elif st.di.data_source == "stooq":
            self.price = st.df['Close']  # from stooq
        else:
            self.price = st.df['Close']  # other
        """
        # set values for the graph
        self.date = st.df.index  # Axis x
        self.price = st.df['Close']  # Axis y1-1
        self.avg01 = st.avg[st.di.method + '1']  # Axis y1-2
        self.avg02 = st.avg[st.di.method + '2']  # Axis y1-3
        self.avg03 = st.avg[st.di.method + '3']  # Axis y1-4

        self.volume = st.df['Volume']  # Axis y2-1

        # plot data
        fig, axes = plt.subplots(2, 1, figsize=(20, 12), sharex=True)
        # plt.subplot(2, 1, 1)

        axes[0].set_title("Stock Price Chart " + st.di.data_type + " - " + st.di.method)
        axes[0].set_xlabel('Date')
        axes[0].set_ylabel('Price (JPY)')

        # plot price data
        axes[0].plot(self.date, self.price, label='Price', color='Red')
        axes[0].plot(self.date, self.avg01, label='Avg05days', color='blue')
        axes[0].plot(self.date, self.avg02, label='Avg25days', color='green')
        axes[0].plot(self.date, self.avg03, label='Avg50days', color='purple')

        axes[0].legend()

        # plt.subplot(2, 1, 2)
        axes[1].set_title('Stock Volume Chart')
        axes[1].set_xlabel('Date')
        axes[1].set_ylabel('Volume (Unit)')

        axes[1].bar(self.date, self.volume, label='Volume', color='grey')
        axes[1].legend()

        # display
        plt.show()
