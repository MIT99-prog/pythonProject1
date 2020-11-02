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


import mplfinance as mpf

from stock import Stock


class StockGraph:
    def __init__(self, st: Stock):

        mpf.plot(st.df, type='candle', mav=(5, 25, 50))






