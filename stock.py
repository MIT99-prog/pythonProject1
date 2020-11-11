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

from datetime import date as dt  # datetime functions

import pandas as pd


# from gdcloss import Graph


class DataInfo:
    def __init__(self):
        self.data_type = "^N225"
        self.data_source = "yahoo"
        self.data_size = 365
        self.start = dt.today()
        self.end = dt.today()
        self.method = ""
        self.span1 = 5
        self.span2 = 25
        self.span3 = 50

    """
    def calcstart(self):
        differ = delta(days=self.data_size)
        self.start = self.end - differ

    def setsize(self, input_size):
        self.data_size = input_size
        self.calcstart()
    """


class Stock:
    def __init__(self, di: DataInfo):
        self.df = pd.DataFrame()
        self.avg = pd.DataFrame()
        self.chg = pd.DataFrame()
        self.di = di
        self.km = pd.Series()

    def data_read(self):  # import row data from internet

        # import packages
        from pandas_datareader import data  # Stock data

        # set stock data from internet to dataframe
        self.df = data.DataReader(self.di.data_type, self.di.data_source, self.di.start, self.di.end)

        # post process
        self.df = self.df.sort_index()  # data sort
        self.set_average()  # Calc Average Data
        self.calc_change_data()  # Calc Change Data

    def set_average(self):
        # clear Average Data
        self.avg = pd.DataFrame()
        # Set Average Data
        Sma(self)
        Wma(self)
        Ewm(self)

        print("Average Calculation is completed!")

    def calc_change_data(self):
        # Clear Change Data
        self.chg = pd.DataFrame()
        # Calc Change of Rate of the day
        self.chg['Change'] = self.df['Close'] - self.df['Open']
        self.chg['ChgRate'] = (self.chg['Change'] / self.df['Open']) * 100  # percentage

        print("Change Calculation is completed!")


class CalcAvg:
    def __init__(self, st: Stock):
        # self.sp = Span()
        # self.price = []
        self.price = st.df['Close']
        # self.average = pd.DataFrame()
        """
        if st.di.data_source == "yahoo":
            self.price = st.df['Adj Close']  # from yahoo
        elif st.di.data_source == "stooq":
            self.price = st.df['Close']  # from stooq
        else:
            self.price = st.df['Close']  # temporally
        """


class Sma(CalcAvg):
    def __init__(self, st: Stock):
        super().__init__(st)

        # Simple Moving Average
        st.avg['sma1'] = self.price.rolling(window=st.di.span1, min_periods=1, center=True).mean()
        st.avg['sma2'] = self.price.rolling(window=st.di.span2, min_periods=1, center=True).mean()
        st.avg['sma3'] = self.price.rolling(window=st.di.span3, min_periods=1, center=True).mean()


class Wma(CalcAvg):
    def __init__(self, st: Stock):
        super().__init__(st)

        # waited moving average
        st.avg['wma1'] = self.price.rolling(window=st.di.span1, min_periods=1, center=True,
                                            win_type='triang').mean()
        st.avg['wma2'] = self.price.rolling(window=st.di.span2, min_periods=1, center=True,
                                            win_type='triang').mean()
        st.avg['wma3'] = self.price.rolling(window=st.di.span3, min_periods=1, center=True,
                                            win_type='triang').mean()


class Ewm(CalcAvg):
    def __init__(self, st: Stock):
        super().__init__(st)

        # Exponential smoothing moving average
        st.avg['ewm1'] = self.price.ewm(min_periods=1, span=st.di.span1).mean()
        st.avg['ewm2'] = self.price.ewm(min_periods=1, span=st.di.span2).mean()
        st.avg['ewm3'] = self.price.ewm(min_periods=1, span=st.di.span3).mean()


"""
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
    di.setsize(data_size)
    di.method = method

    # data set and calc average
    #st = Stock(di)

    # generate graph
    # Graph(st, di)

    sys.exit()


if __name__ == '__main__':
    main()
"""
