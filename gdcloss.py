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
import pandas as pd
from numpy.distutils.fcompiler import none

from stock import Stock


class Span:

    def __init__(self):
        # super().__init__()
        self.span01 = 5
        self.span02 = 25
        self.span03 = 50


class CalcAvg:
    def __init__(self, st: Stock):
        self.sp = Span()
        self.price = []
        self.average = pd.DataFrame()

        if st.di.data_source == "yahoo":
            self.price = st.df['Adj Close']  # from yahoo
        elif st.di.data_source == "stooq":
            self.price = st.df['Close']  # from stooq
        else:
            self.price = st.df['Close']  # temporally


class Sma(CalcAvg):
    def __init__(self, st: Stock):
        super().__init__(st)

    def calcavg(self, st):
        # Simple Moving Average
        st.avg['avg05days'] = self.price.rolling(window=self.sp.span01).mean()
        st.avg['avg25days'] = self.price.rolling(window=self.sp.span02).mean()
        st.avg['avg50days'] = self.price.rolling(window=self.sp.span03).mean()


class Wma(CalcAvg):
    def __init__(self, st: Stock):
        super().__init__(st)

    def calcavg(self, st):
        # waited moving average
        st.avg['avg05days'] = self.price.rolling(window=self.sp.span01, center=False, win_type='triang').mean()
        st.avg['avg25days'] = self.price.rolling(window=self.sp.span02, center=False, win_type='triang').mean()
        st.avg['avg50days'] = self.price.rolling(window=self.sp.span03, center=False, win_type='triang').mean()


class Ewm(CalcAvg):
    def __init__(self, st: Stock):
        super().__init__(st)

    def calcavg(self, st):
        # Exponential smoothing moving average
        st.avg['avg05days'] = self.price.ewm(span=self.sp.span01).mean()
        st.avg['avg25days'] = self.price.ewm(span=self.sp.span02).mean()
        st.avg['avg50days'] = self.price.ewm(span=self.sp.span03).mean()


class Graph:
    def __init__(self, st: Stock):
        self.date = []
        self.price = []
        self.avg01 = []
        self.avg02 = []
        self.avg03 = []
        self.volume = []
        self.calc = none

        self.setavg(st)
        self.generate_graph(st)

    def setavg(self, st):
        md = st.di.method
        if md == "sma":
            self.calc = Sma(st)
        elif md == "wma":
            self.calc = Wma(st)
        elif md == "ewm":
            self.calc = Ewm(st)
        else:
            self.calc = Sma(st)
            print("Calc Method Error. Calc with Sma.")

        self.calc.calcavg(st)

    def generate_graph(self, st):
        self.date = st.df.index
        # set analysis values
        # set analysis values
        if st.di.data_source == "yahoo":
            self.price = st.df['Adj Close']  # from yahoo
        elif st.di.data_source == "stooq":
            self.price = st.df['Close']  # from stooq
        else:
            self.price = st.df['Close']  # other

        # set values for the graph
        self.avg01 = st.avg['avg05days']
        self.avg02 = st.avg['avg25days']
        self.avg03 = st.avg['avg50days']

        self.volume = st.df['Volume']

        # plot data
        fig, axes = plt.subplots(2, 1, figsize=(20, 12), sharex=True)
        # plt.subplot(2, 1, 1)

        axes[0].set_title("Stock Price Chart " + st.di.data_type + " - " + st.di.method)
        axes[0].set_xlabel('Date')
        axes[0].set_ylabel('Price (JPY)')

        # plot price data
        axes[0].plot(self.date, self.price, label='Price', color='pink')
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
