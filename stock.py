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
import sys
from datetime import date as dt  # datetime functions
from datetime import timedelta as delta  # difference between two dates

import matplotlib.pyplot as plt
import numpy as np


class Span:

    def __init__(self):
        # super().__init__()
        self.span01 = 5
        self.span02 = 25
        self.span03 = 50


class DataInfo:
    def __init__(self):
        super().__init__()
        self.data_type = "^N225"
        self.data_source = "yahoo"
        self.data_size = 365
        self.start = dt.today()
        self.end = dt.today()
        self.method = 1

    def calcstart(self):
        differ = delta(days=self.data_size)
        self.start = self.end - differ

    def setsize(self, input_size):
        self.data_size = input_size
        self.calcstart()


class Stock:
    def __init__(self, di: DataInfo):
        self.df = None
        self.data_read(di)
        self.setavg(di)

    def data_read(self, di):  # import row data from internet

        # import packages
        from pandas_datareader import data  # Stock data

        # set stock data from internet to dataframe
        self.df = data.DataReader(di.data_type, di.data_source, di.start, di.end)

        # sort by index
        self.df = self.df.sort_index()

    def setavg(self, di):
        md = di.method
        if md == 1:
            calc = Sma(self, di)
        elif md == 2:
            calc = Wma(self, di)
        elif md == 3:
            calc = Ewm(self, di)
        else:
            calc = Sma(self, di)
            print("Calc Method Error. Calc with Sma.")

        calc.calcavg(self)


class CalcAvg:
    def __init__(self, st: Stock, di: DataInfo):
        self.sp = Span()
        self.price = []

        if di.data_source == "yahoo":
            self.price = st.df['Adj Close']  # from yahoo
        elif di.data_source == "stooq":
            self.price = st.df['Close']  # from stooq
        else:
            self.price = st.df['Close']  # temporally


class Sma(CalcAvg):
    def __init__(self, st: Stock, di: DataInfo):
        super().__init__(st, di)

    def calcavg(self, st: Stock):
        # Simple Moving Average
        st.df['avg05days'] = self.price.rolling(window=self.sp.span01).mean()
        st.df['avg25days'] = self.price.rolling(window=self.sp.span02).mean()
        st.df['avg50days'] = self.price.rolling(window=self.sp.span03).mean()


class Wma(CalcAvg):
    def __init__(self, st: Stock, di: DataInfo):
        super().__init__(st, di)

    def calcavg(self, st):
        # waited moving average
        st.df['avg05days'] = self.price.rolling(window=self.sp.span01, center=False, win_type='triang').mean()
        st.df['avg25days'] = self.price.rolling(window=self.sp.span02, center=False, win_type='triang').mean()
        st.df['avg50days'] = self.price.rolling(window=self.sp.span03, center=False, win_type='triang').mean()


class Ewm(CalcAvg):
    def __init__(self, st: Stock, di: DataInfo):
        super().__init__(st, di)

    def calcavg(self, st):
        # Exponential smoothing moving average
        st.df['avg05days'] = self.price.ewm(span=self.sp.span01).mean()
        st.df['avg25days'] = self.price.ewm(span=self.sp.span02).mean()
        st.df['avg50days'] = self.price.ewm(span=self.sp.span03).mean()


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


def main():
    # ask detail of the data
    data_type = input("取り込むデータの種類を入力してください。（日経平均は、＾N225、企業は、証券コードに.JP）")
    data_source = input("データソースを入力してください。（yahoo/stooq）")
    data_size = np.int(input("取得するデータの期間を日数で入力してください。"))
    method = int(input("1:単純移動平均 2:加重移動平均 3:指数平滑移動平均"))

    # Instance of DataInfo, Stock Class
    di = DataInfo()
    di.data_type = data_type
    di.data_source = data_source
    di.data_size = di.setsize(data_size)
    di.method = method

    # data set and calc average
    st = Stock(di)

    # generate graph
    Graph(st, di)

    sys.exit()


if __name__ == '__main__':
    main()
