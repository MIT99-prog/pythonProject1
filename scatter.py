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

from stock import Stock


class Scatter:
    def __init__(self, st: Stock):
        self.x = pd.DataFrame()

        self.x.insert(loc=0, column="Open", value=st.df['Open'])
        self.x.insert(loc=1, column="Close", value=st.df['Close'])
        self.x.insert(loc=2, column="High", value=st.df['High'])
        self.x.insert(loc=3, column="Low", value=st.df['Low'])
        self.y = st.df['Volume']

        plt.plot(self.x['Open'], self.y, 'o', label="Open")
        plt.plot(self.x['Close'], self.y, 'x', label="Close")
        plt.plot(self.x['High'], self.y, '+', label="High")
        plt.plot(self.x['Low'], self.y, '*', label="Low")

        plt.title("Scatter Graph")
        plt.xlabel("Price")
        plt.ylabel("Volume")
        plt.grid(True)
        plt.legend()
        plt.show()
