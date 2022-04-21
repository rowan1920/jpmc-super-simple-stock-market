from models import Stock
from utils import global_variables


def get_stock() -> Stock:
    print("\nSelect one of the following stock symbols:\n")
    print(" - " + ("\n - ".join(global_variables.stocks.keys())))
    stock_symbol = input("\n>").upper()

    try:
        return global_variables.stocks[stock_symbol]
    except KeyError:
        print('Please enter a valid stock symbol')
        return get_stock()


def get_price() -> int:
    price = input("\nEnter a price (in pence)\n>")
    if price.isdigit():
        return int(price)
    else:
        print('Please enter a valid price')
        return get_price()


def get_trade_quantity() -> int:
    trade_quantity = input("\nEnter a trade quantity\n>")
    if trade_quantity.isdigit() and int(trade_quantity) > 0:
        return int(trade_quantity)
    else:
        print('Please enter a valid quantity')
        return get_trade_quantity()
