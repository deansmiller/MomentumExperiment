__author__ = 'deansmiller'

import datetime

logging = False


def log(message):
    if logging:
        print(message)


def check_weekend(date):
    if date.weekday() == 5:
        return datetime.datetime(date.year, date.month, date.day - 1)
    elif date.weekday() == 6:
        return datetime.datetime(date.year, date.month, date.day - 2)
    else:
        return date

def print_stocks(label, stocks):
    print
    print(label)
    for stock in stocks:
        print(stock)
    print

def save_portfolio(filename, stocks):
    file = open("portfolios/" + filename, "w")
    file.write("Symbol, Price, Shares\n")
    for stock in stocks:
        symbol = stock[0]
        price = str(stock[1])
        ret = str(stock[2])
        line = symbol + "," + price + "," + ret + "\n"
        file.write(line)
    file.close()
