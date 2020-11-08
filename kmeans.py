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
        result = KMeans(n_clusters=6).fit_predict(data)
        # クラスタ番号を表示
        st.km = pd.Series(result, index=st.df.index)
        # 分析結果をデータと照合
        wg = pd.DataFrame()
        wg.insert(0, 'Open', st.df['Open'])
        wg.insert(1, 'Close', st.df['Close'])
        wg.insert(2, 'High', st.df['High'])
        wg.insert(3, 'Low', st.df['Low'])
        wg.insert(4, 'Volume', st.df['Volume'])
        wg.insert(5, 'KMeans', st.km)
        # Group 0
        wg0 = wg.query('KMeans == 0')
        wg0OpenAvg = int(wg0['Open'].mean())
        wg0CloseAvg = int(wg0['Close'].mean())
        wg0HighAvg = int(wg0['High'].mean())
        wg0LowAvg = int(wg0['Low'].mean())
        wg0VolumeAvg = int(wg0['Volume'].mean())
        # Group 1
        wg1 = wg.query('KMeans == 1')
        wg1OpenAvg = int(wg1['Open'].mean())
        wg1CloseAvg = int(wg1['Close'].mean())
        wg1HighAvg = int(wg1['High'].mean())
        wg1LowAvg = int(wg1['Low'].mean())
        wg1VolumeAvg = int(wg1['Volume'].mean())
        # Group 2
        wg2 = wg.query('KMeans == 2')
        wg2OpenAvg = int(wg2['Open'].mean())
        wg2CloseAvg = int(wg2['Close'].mean())
        wg2HighAvg = int(wg2['High'].mean())
        wg2LowAvg = int(wg2['Low'].mean())
        wg2VolumeAvg = int(wg2['Volume'].mean())
        # Group 3
        wg3 = wg.query('KMeans == 3')
        wg3OpenAvg = int(wg3['Open'].mean())
        wg3CloseAvg = int(wg3['Close'].mean())
        wg3HighAvg = int(wg3['High'].mean())
        wg3LowAvg = int(wg3['Low'].mean())
        wg3VolumeAvg = int(wg3['Volume'].mean())
        # Group 4
        wg4 = wg.query('KMeans == 4')
        wg4OpenAvg = int(wg4['Open'].mean())
        wg4CloseAvg = int(wg4['Close'].mean())
        wg4HighAvg = int(wg4['High'].mean())
        wg4LowAvg = int(wg4['Low'].mean())
        wg4VolumeAvg = int(wg4['Volume'].mean())
        # Group 5
        wg5 = wg.query('KMeans == 5')
        wg5OpenAvg = int(wg5['Open'].mean())
        wg5CloseAvg = int(wg5['Close'].mean())
        wg5HighAvg = int(wg5['High'].mean())
        wg5LowAvg = int(wg5['Low'].mean())
        wg5VolumeAvg = int(wg5['Volume'].mean())

        labels = ['Group0 Avg= ' + str(wg0OpenAvg) + ':' + str(wg0CloseAvg) + ':' + str(wg0HighAvg) + ':'
                  + str(wg0LowAvg) + ' / ' + str(wg0VolumeAvg),
                  'Group1 Avg= ' + str(wg1OpenAvg) + ':' + str(wg1CloseAvg) + ':' + str(wg1HighAvg) + ':'
                  + str(wg1LowAvg) + ' / ' + str(wg1VolumeAvg),
                  'Group2 Avg= ' + str(wg2OpenAvg) + ':' + str(wg2CloseAvg) + ':' + str(wg2HighAvg) + ':'
                  + str(wg2LowAvg) + ' / ' + str(wg2VolumeAvg),
                  'Group3 Avg= ' + str(wg3OpenAvg) + ':' + str(wg3CloseAvg) + ':' + str(wg3HighAvg) + ':'
                  + str(wg3LowAvg) + ' / ' + str(wg3VolumeAvg),
                  'Group4 Avg= ' + str(wg4OpenAvg) + ':' + str(wg4CloseAvg) + ':' + str(wg4HighAvg) + ':'
                  + str(wg4LowAvg) + ' / ' + str(wg4VolumeAvg),
                  'Group5 Avg= ' + str(wg5OpenAvg) + ':' + str(wg5CloseAvg) + ':' + str(wg5HighAvg) + ':'
                  + str(wg5LowAvg) + ' / ' + str(wg5VolumeAvg)]

        plt.title('K-Means Clustering Analysis')
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.axis([wg.index.min(), wg.index.max(), wg['Close'].min() - 100, wg['Close'].max() + 100])
        plt.bar(wg0.index, wg0['Close'], label=labels[0], color='Blue')
        plt.bar(wg1.index, wg1['Close'], label=labels[1], color='Green')
        plt.bar(wg2.index, wg2['Close'], label=labels[2], color='Red')
        plt.bar(wg3.index, wg3['Close'], label=labels[3], color='Yellow')
        plt.bar(wg4.index, wg4['Close'], label=labels[4], color='Pink')
        plt.bar(wg5.index, wg5['Close'], label=labels[5], color='Purple')
        plt.legend()

        plt.show()
        print(result)


