# -------------------------------------------------------------------------------
# Name:        SVM
# Purpose:     to test functions of SVM of Scikit-learn
#
# Author:      tango
#
# Created:     26/10/2020
# Copyright:   (c) tango 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------
from sklearn import svm

from stock import Stock


class Svm:

    def __init__(self, st: Stock):
        # Set learning data
        x = st.df.loc[:, ['Close']].values
        y = st.df['Volume']
        # Definition learning model
        clf = svm.SVC()
        # Fitting
        clf.fit(x, y)
        score = clf.score(x, y)
        # Test
        x = [[24923], ]
        test_y = clf.predict(x)
        print("Score = " + str(score) + "Result x= " + str(x) + " y= " + str(test_y))
"""
        # 境界線プロット用の格子状データを生成
        x1 = np.linspace(int(st.df['Close'].min()), int(st.df['Close'].max()),
                         int(st.df['Close'].max() - st.df['Close'].min()))
        x2 = np.linspace(int(st.df['Volume'].min()), int(st.df['Volume'].max()),
                         int(st.df['Volume'].max() - st.df['Volume'].min()))
        X1, X2 = np.meshgrid(x1, x2)
        plot_X = np.c_[X1.ravel(), X2.ravel()]
        plot_y = clf.predict(plot_X)
        # 検証結果の表示
        print("plot X：", plot_X)
        print("plot y：", plot_y)
"""
