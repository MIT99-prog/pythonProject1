# -------------------------------------------------------------------------------
# Name:        change
# Purpose:     analysis with change rate of the stock
#
# Author:      tango
#
# Created:     26/10/2020
# Copyright:   (c) tango 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import matplotlib.gridspec as gridspec
from matplotlib import pyplot as plt

from stock import Stock


class ChangeRate:
    def __init__(self, st: Stock):
        # Calc Change of Rate in the day
        st.chg['Change'] = st.df['Close'] - st.df['Open']
        st.chg['ChgRate'] = (st.chg['Change'] / st.df['Open']) * 100  # percentage

        self.plot_change_values(st)

    def plot_change_values(self, st: Stock):
        fig = plt.figure(tight_layout=True)
        gs = gridspec.GridSpec(2, 2)

        x = st.df.index
        y_1 = st.chg['Change']
        y_2 = st.chg['ChgRate']

        ax = fig.add_subplot(gs[0, :])
        ax.bar(x, y_1, label='Change', color='r')
        ax.set_xlabel('Date')
        ax.set_ylabel('Change Value')
        ax.grid(True)

        ax = fig.add_subplot(gs[1, 0])
        ax.plot(x, y_2, label='ChgRate', color='g')
        ax.set_xlabel('Date')
        ax.set_ylabel('Change Percentage')
        ax.grid(True)

        ax = fig.add_subplot(gs[1, 1])
        ax.hist(y_2, 50, density=True)
        ax.set_xlabel('Change Percentage')
        ax.set_ylabel('Number of Days')
        ax.grid(True)

        fig.legend()
        plt.show()
