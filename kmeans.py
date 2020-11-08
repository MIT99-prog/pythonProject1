# -------------------------------------------------------------------------------
# Name:        k-means
# Purpose:     to test the clastering function of scikit-learn
#
# Author:      tango
#
# Created:     07/11/2020
# Copyright:   (c) tango 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

from stock import Stock


class KMAnalysis:
    def __init__(self, st: Stock):
        # Calc Amount
        amountOpen = st.df['Open'] * st.df['Volume'] / 1000
        amountClose = st.df['Close'] * st.df['Volume'] / 1000
        amountHigh = st.df['High'] * st.df['Volume'] / 1000
        amountLow = st.df['Low'] * st.df['Volume'] / 1000

        # Pandasデータフレームをnumpy配列に変換
        data = np.array([amountOpen.tolist(), amountClose.tolist(), amountHigh.tolist(),
                         amountLow.tolist()], np.int32)
        # numpy配列を転置
        data = data.T
        # k-means法でクラスタ分析（クラスタ数は3）
        result = KMeans(n_clusters=3).fit_predict(data)
        # クラスタ番号を表示
        st.km = pd.Series(result, index=st.df.index)
        wg = pd.DataFrame()
        wg.insert(0, 'Close', st.df['Close'])
        wg.insert(1, 'Volume', st.df['Volume'])
        wg.insert(2, 'KMeans', st.km)

        wg0 = wg.query('KMeans == 0')
        wg0PriceAvg = wg0['Close'].mean()
        wg0VolumeAvg = wg0['Volume'].mean()
        wg1 = wg.query('KMeans == 1')
        wg1PriceAvg = wg1['Close'].mean()
        wg1VolumeAvg = wg1['Volume'].mean()
        wg2 = wg.query('KMeans == 2')
        wg2PriceAvg = wg2['Close'].mean()
        wg2VolumeAvg = wg2['Volume'].mean()

        labels = ['Group0 Avg= ' + str(wg0PriceAvg) + ' / ' + str(wg0VolumeAvg),
                  'Group1 Avg= ' + str(wg1PriceAvg) + ' / ' + str(wg1VolumeAvg),
                  'Group2 Avg= ' + str(wg2PriceAvg) + ' / ' + str(wg2VolumeAvg)]

        plt.title('K-Means Clustering Analysis')
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.axis([wg.index.min(), wg.index.max(), wg['Close'].min() - 100, wg['Close'].max() + 100])
        plt.bar(wg0.index, wg0['Close'], label=labels[0], color='Blue')
        plt.bar(wg1.index, wg1['Close'], label=labels[1], color='Green')
        plt.bar(wg2.index, wg2['Close'], label=labels[2], color='Red')
        plt.legend()

        plt.show()
        print(result)


