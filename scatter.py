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

from regression import RegAnalysis
from stock import Stock


class Scatter:
    def __init__(self, st: Stock):
        self.x = pd.DataFrame()

        self.x.insert(loc=0, column="Open", value=st.df['Open'])
        self.x.insert(loc=1, column="Close", value=st.df['Close'])
        self.x.insert(loc=2, column="High", value=st.df['High'])
        self.x.insert(loc=3, column="Low", value=st.df['Low'])
        self.y = st.df['Volume']
        self.z = pd.Series
        self.val = pd.DataFrame()

        # Execute Regression Analysis
        ra = RegAnalysis(st)

        # Generate Regression Data
        labels = ['Open', 'Close', 'High', 'Low']
        for i in range(4):
            self.val.insert(i, 'R-' + labels[i], self.x.values[:, i] * ra.a[i] + ra.b[i])
            self.z = self.val.values[:, i]
            plt.subplot(2, 2, i+1)
            plt.plot(self.x.values[:, i], self.y, 'o', label=labels[i])
            plt.plot(self.x.values[:, i], self.z, '-', label="R_" + labels[i])

            # Set Attributes
            plt.title("Scatter Graph", loc='Left')
            plt.xlabel("Price")
            plt.ylabel("Volume")
            plt.grid(True)
            plt.legend()
        plt.show()
