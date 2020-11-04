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


class Span:

    def __init__(self):
        # super().__init__()
        self.span01 = 5
        self.span02 = 25
        self.span03 = 50


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

        self.setavg(st, di)
        self.generate_graph(st, di)

    def setavg(self, st, di):
        md = di.method
        if md == 1:
            calc = Sma(st, di)
        elif md == 2:
            calc = Wma(st, di)
        elif md == 3:
            calc = Ewm(st, di)
        else:
            calc = Sma(st, di)
            print("Calc Method Error. Calc with Sma.")

        calc.calcavg(st)

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
