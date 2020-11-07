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
# import sys
from datetime import date as dt  # datetime functions
from datetime import timedelta as delta  # difference between two dates

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

    def calcstart(self):
        differ = delta(days=self.data_size)
        self.start = self.end - differ

    def setsize(self, input_size):
        self.data_size = input_size
        self.calcstart()


class Stock:
    def __init__(self, di: DataInfo):

        self.df = pd.DataFrame()
        self.avg = pd.DataFrame()
        self.di = di
        # self.data_read()

    def data_read(self):  # import row data from internet

        # import packages
        from pandas_datareader import data  # Stock data

        # set stock data from internet to dataframe
        self.df = data.DataReader(self.di.data_type, self.di.data_source, self.di.start, self.di.end)

        # sort by index
        self.df = self.df.sort_index()


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
