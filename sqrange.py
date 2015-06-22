#!/usr/bin/env python
#python 2.7 or higher
#

from yahoo_finance import *
from math import *


def range_show(low, high, value, pattern):
    INCREMENTS = 20
    MARKER = '*'
    PATTERN = bytearray(pattern)

    if (high - low > 0):
        relval = ceil( (value - low) / (high - low) * INCREMENTS )
        relvalue = int(relval)
    else:
        relvalue = 10

    PATTERN[ relvalue ] = MARKER
    s = '{:7.2f}'.format(low) + \
        PATTERN + \
        '{:7.2f}'.format(high)

    return( s )


def data_show(stocksym, category):
    YPATTERN = bytearray("|    .    .    .    |")
    DPATTERN = bytearray("[    .    .    .    ]")
    S = Share(stocksym)

#    S.refresh()

    info = S.get_info()
    info['category'] = category
    info['price'] = price = float(S.get_price())
    info['volume'] = volume = float( S.get_volume() )
    info['ebitda'] = ebitda = S.get_ebitda()
    info['dividend_share'] = dividend_share = S.get_dividend_share()
    info['year_low'] = year_low = float(S.get_year_low())
    info['year_high'] = year_high = float(S.get_year_high())
    info['days_low'] = days_low = float(S.get_days_low())
    info['days_high'] = days_high = float(S.get_days_high())
    info['market_cap'] = market_cap = S.get_market_cap()
    info['book_value'] = book_value = S.get_book_value()
    info['earnings_share'] = earnings_share = S.get_earnings_share()
    info['price_earnings_ratio'] = price_earnings_ratio = \
                                   S.get_price_earnings_ratio()
    info['price_earnings_growth_ratio'] = price_earnings_growth_ratio = \
                                   S.get_price_earnings_growth_ratio()
    info['short_ratio'] = short_ratio = S.get_short_ratio()

    info['output'] = output = \
         '{:6s}'.format( stocksym ) + " " + \
         '{:7.2f}'.format( price ) + " " + \
         '{:9,.4e}'.format( volume ) + " " + \
         '{:>8s}'.format( ebitda )+ " " + \
         '{:>6s}'.format( dividend_share ) + " " + \
         range_show( year_low, year_high, price, YPATTERN ) + \
         '\n' + \
         '{:>7s}'.format( market_cap ) + " " + \
         '{:>6s}'.format( book_value ) + " " + \
         '{:>6s}'.format( earnings_share ) + " " + \
         '{:>6s}'.format( price_earnings_ratio ) + " " + \
         '{:>6s}'.format( price_earnings_growth_ratio ) + " " + \
         '{:>5s}'.format( short_ratio ) + " " + \
         range_show( days_low, days_high, price, DPATTERN ) + " " + \
         '{:>5s}'.format( category )

    return ( info )


INFILE = "stocklist2.txt"
def main():

    category = ""
    stocklist = []
    f = open(INFILE)

    while ( 1 ):
        line = f.readline()
        if not line:
            break
        stock = line[0:-1]

        if stock[0] == ":":
            category = stock[1:-1]
            print category
            continue

        stockinfo = data_show(stock, category)
        stocklist.append( stockinfo )
        print stockinfo['output']
    f.close()


main()



