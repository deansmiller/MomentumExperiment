__author__ = 'deansmiller'

import datetime
import pandas.io.data as pid
import utils as utils


class MomentumStockSelector:

    def __init__(self, ticker_file,
                 end_date,
                 collection_period = 52,
                 threshold = 0.3):
        self.tickers = open(ticker_file).read().split(",")
        self.collection_period = collection_period
        self.threshold = threshold
        self.stocks = []

        if end_date is None:
            date = datetime.datetime.today() - datetime.timedelta(days=1)
            self.end_date = datetime.datetime(date.year, date.month, date.day)
        else:
            self.end_date = end_date

        self.start_date = self.end_date - datetime.timedelta(weeks=self.collection_period)


    def select_stocks(self, buy_label, sell_label):


        if self.start_date.weekday() == 5 or self.start_date.weekday() == 6:
            self.start_date = datetime.datetime(self.start_date.year, self.start_date.month, self.start_date.day - 2)

        print((self.start_date.date(), self.end_date.date()))
        for ticker in self.tickers:
            try:
                data = pid.get_data_yahoo(ticker, start=self.start_date, end=self.end_date)["Close"]
                dates = data.index
                last_price = data[len(dates) - 1]
                end_term_ret = (last_price - data[self.start_date]) / data[self.start_date]
                print((ticker, end_term_ret))
                self.stocks.append((ticker, end_term_ret, last_price))
            except (KeyError, IOError) as e:
                raise e


        self.stocks.sort(key=lambda t: t[1])
        utils.print_stocks("Stocks sorted on return", self.stocks);

        decile = int(len(self.stocks) * 0.10)
        sell_stocks = self.stocks[:decile]
        buy_stocks = self.stocks[decile * 9:]
        buy_stocks.reverse()
        utils.print_stocks("Sell stocks", sell_stocks)
        utils.print_stocks("Buy stocks", buy_stocks)

        utils.save_portfolio(sell_label, sell_stocks)
        utils.save_portfolio(buy_label, buy_stocks)



