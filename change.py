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
import cmath as cm

import matplotlib.gridspec as gridspec
import numpy as np
from matplotlib import pyplot as plt

from stock import Stock


class ChangeRate:
    def __init__(self, st: Stock):


        self.plot_change_values(st)

    def plot_change_values(self, st: Stock):
        # Initialize Graph
        fig = plt.figure(tight_layout=True)
        gs = gridspec.GridSpec(2, 2)
        # Set Data
        x = st.df.index
        y_1_1 = st.df['Open']
        y_1_2 = st.df['Close']
        y_2 = st.chg['Change']
        nb = cm.log(st.df.shape[0], 2)
        # n2 = cm.log10(st.df.shape[0]) / cm.log10(2)
        # bins = 1 + int(nb.real)
        bins = (1 + int(nb.real)) * 2
        y_2_mu = y_2.mean()  # Mean
        y_2_sigma = y_2.std()  # Standard Deviation

        # Plot Data
        # Values of Open / Close (1)
        ax = fig.add_subplot(gs[0, :])
        ax.plot(x, y_1_1, label='Open', color='r')
        ax.plot(x, y_1_2, label='Close', color='g')
        ax.set_title('Stock Open/Close price by Date')
        ax.set_xlabel('Date')
        ax.set_ylabel('Stock Price')
        ax.grid(True)

        # Value / Date (2)
        ax = fig.add_subplot(gs[1, 0])
        ax.bar(x, y_2, label='Change Value', color='b')
        ax.set_title('Change Value by Date')
        ax.set_xlabel('Date')
        ax.set_ylabel('Change Value')
        ax.grid(True)

        # Percentage Histogram (3)
        ax = fig.add_subplot(gs[1, 1])
        # the histogram of the data
        n, bins, patches = ax.hist(y_2, bins, density=True)
        # add a 'best fit' line
        y = ((1 / (np.sqrt(2 * np.pi) * y_2_sigma)) *
             np.exp(-0.5 * (1 / y_2_sigma * (bins - y_2_mu)) ** 2))
        ax.plot(bins, y, '--')
        ax.set_title('Histogram of Change Value')
        ax.set_xlabel('Value mu= ' + str(y_2_mu) + ' / sigma= ' + str(y_2_sigma))
        ax.set_ylabel('Percentage')
        ax.grid(True)

        fig.legend()
        plt.show()
