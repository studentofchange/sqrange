#!/usr/bin/env python
#python 2.7 or higher
# 2015-07-09
# Waiming Mok
#

from pandas import *
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
import numpy as np
from math import *


StartDate =	"2000-1-1"
DSource =	"yahoo"


def stock_history_and_actions(stocksym, technical):
    sDF = web.DataReader(name=stocksym, data_source=DSource, start=StartDate)
    resultDF = technical(sDF)
    return resultDF


def bollingerAction(above, below, price):
    if price > above :
        return "SELL"
    elif price < below :
        return "BUY"
    else:
        return ""
    

def bollinger(sDF, length=30, numsd=2):
    price = sDF[u'Close']
    ave = pd.stats.moments.rolling_mean(price, length)
    sd = pd.stats.moments.rolling_std(price, length)
    upband = ave + (sd * numsd)
    dnband = ave - (sd * numsd)

    sDF[u'Action'] = \
         map(lambda u,d,p : bollingerAction(u,d,p), upband, dnband, price)
    sDF[u'Above'] =  np.round(upband, 3)
    sDF[u'Center'] = np.round(ave, 3)
    sDF[u'Below'] =  np.round(dnband, 3)

    return sDF[[u'Close', u'Action', u'Above', u'Center', u'Below']]


def bollingerPlot(sDF, limit=200):

    sDF = sDF[-limit:]
    sDF.plot()

    plt.show()



INFILE = "stocklist.txt"

def main():

    stocklist = []
    f = open(INFILE)

    while ( 1 ):
        line = f.readline()
        if not line or line.isspace():
            break
        stock = line[0:-1]

        sDF = stock_history_and_actions(stock, bollinger)
	sp = sDF[-200:]               # latest 200 data points
        print sp[ sp[u'Action']!="" ] # print out the SELL/BUY recommendations

        bollingerPlot(sp)

    f.close()


main()



