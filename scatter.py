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

        self.x.index.append(st.df.index)
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
        fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True, sharey=True)
        one_dimension_axes = axes.ravel()

        for i, axes in enumerate(one_dimension_axes):
            self.val.insert(i, 'R-' + labels[i], self.x.values[:, i] * ra.a[i] + ra.b[i])
            self.z = self.val.values[:, i]
            # plt.subplot(2, 2, i+1)
            axes.plot(self.x.values[:, i], self.y, 'o', label=labels[i])
            axes.plot(self.x.values[:, i], self.z, '-', label="R_" + labels[i])

            # Set Attributes
            axes.set_title("a= " + str(ra.a[i]) + " b= " + str(ra.b[i]) + " s= " + str(ra.s[i]),
                      loc='Left')
            axes.set_xlabel("Price")
            axes.set_ylabel("Volume")
            axes.grid(True)
            axes.legend()

        # plt.tight_layout()
        plt.show()
