from momentum_stock_selector import MomentumStockSelector
import datetime

end_date = datetime.datetime.today() - datetime.timedelta(weeks=52)
mo_stock_sel = MomentumStockSelector("data/ftse100.dat", end_date)
mo_stock_sel.select_stocks("Buy2.csv", "Sell2.csv")