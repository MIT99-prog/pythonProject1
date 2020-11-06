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
import numpy as np
import pandas as pd
from sklearn import linear_model

from stock import Stock


class RegAnalysis:
    def __init__(self, st: Stock):
        # self.clf = linear_model.LinearRegression(fit_intercept=True, normalize=True, copy_X=True, n_jobs=None)
        # self.x = st.df.loc[:, ['Open']].values
        self.clf = linear_model.LinearRegression()
        self.x = pd.DataFrame()
        self.y = st.df['Volume']
        self.a = []
        self.b = []
        self.s = []

        self.execanalysis(st)

    def execanalysis(self, st: Stock):
        column_name = ['Open', 'Close', 'High', 'Low']
        # Multi-Regression Analysis
        for i in range(4):
            self.x = st.df.loc[:, [column_name[i]]].values
            # self.clf.fit(self.x.astype, self.y)
            self.clf.fit(self.x.astype(np.float32), self.y)  # the problem of sitkit-learn?
            # try:
                # self.clf.fit(self.x.astype(np.float32), self.y)
            # except:
                # self.clf.fit(self.x.astype(np.float32), self.y)

            self.a.append(self.clf.coef_)
            self.b.append(self.clf.intercept_)

            self.s.append(self.clf.score(self.x, self.y))

        print("Regression Analysis is completed!")
