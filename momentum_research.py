__author__ = 'deansmiller'

import datetime
import pandas.io.data as pid
import numpy as np
import utils as utils


tickers = open("data/ftse100.dat").read().split(",")
stocks = []
collection_period = 52
threshold = 0.3
date = datetime.datetime.today() - datetime.timedelta(days=1)
end_date = datetime.datetime(date.year, date.month, date.day)
start_date = end_date - datetime.timedelta(weeks=collection_period)
shares = 1

if start_date.weekday() == 5 or start_date.weekday() == 6:
    start_date = datetime.datetime(start_date.year, start_date.month, start_date.day - 2)

print((start_date.date(), end_date.date()))
for ticker in tickers:
    try:
        data = pid.get_data_yahoo(ticker, start=start_date, end=end_date)["Close"]
        dates = data.index
        last_price = data[len(dates) - 1]
        end_term_ret = (last_price - data[start_date]) / data[start_date]
        print((ticker, end_term_ret))
        stocks.append((ticker, end_term_ret, last_price))
    except (KeyError, IOError):
        print("fuck up")


stocks.sort(key=lambda t: t[1])
utils.print_stocks("Stocks sorted on return", stocks);

decile = int(len(stocks) * 0.10)
sell_stocks = stocks[:decile]
buy_stocks = stocks[decile * 9:]
buy_stocks.reverse()
utils.print_stocks("Sell stocks", sell_stocks)
utils.print_stocks("Buy stocks", buy_stocks)

utils.save_portfolio("Sell.csv", sell_stocks)
utils.save_portfolio("Buy.csv", buy_stocks)



