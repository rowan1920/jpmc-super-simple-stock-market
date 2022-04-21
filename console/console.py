from pydantic import ValidationError

from console import user_inputs
from utils.helpers import record_trade, calculate_volume_weighted_stock_price, calculate_gbce_all_share_index


class Console:
    @classmethod
    def main_menu(cls):
        print("\n")
        print('----------')
        print("\nPlease select one of the following options:\n")
        print("A. Given any price as input, calculate the dividend yield of a given stock")
        print("B. Given any price as input, calculate the P/E Ratio of a given stock")
        print("C. Record the trade of a given stock")
        print("D. Calculate the Volume Weighted Stock Price based on trades in the past 15 minutes for a given stock")
        print("E. Calculate the GBCE All Share Index using the geometric mean of prices for all stocks")
        selected_option = input(">").upper()

        if selected_option == "A":
            cls.calculate_dividend_yield()
        if selected_option == "B":
            cls.calculate_pe_ratio()
        if selected_option == "C":
            cls.record_trade()
        if selected_option == "D":
            cls.calculate_volume_weighted_stock_price()
        if selected_option == "E":
            cls.calculate_gbce_index()

    @classmethod
    def calculate_dividend_yield(cls):
        price = user_inputs.get_price()
        stock = user_inputs.get_stock()

        print('Dividend yield for {} at {}: {}'.format(stock.symbol, price, stock.calculate_dividend_yield(price)))

    @classmethod
    def calculate_pe_ratio(cls):
        price = user_inputs.get_price()
        stock = user_inputs.get_stock()

        print('PE Ratio for {} at {}: {}'.format(stock.symbol, price, stock.calculate_pe_ratio(price)))

    @classmethod
    def record_trade(cls):
        trade_type = input("\nEnter a trade type (buy or sell)\n>")
        quantity = user_inputs.get_trade_quantity()
        price = user_inputs.get_price()
        stock = user_inputs.get_stock()
        try:
            record_trade(stock, quantity, trade_type, price)
        except ValidationError as e:
            print(str(e))
            return cls.record_trade()

        print('Trade recorded')

    @classmethod
    def calculate_volume_weighted_stock_price(cls):
        stock = user_inputs.get_stock()
        try:
            volume_weighted_stock_price = calculate_volume_weighted_stock_price(stock.symbol)
            print('Volume Weighted Stock Price for {}: {}'.format(stock.symbol, volume_weighted_stock_price))
        except ValueError as e:
            print(str(e))

    @classmethod
    def calculate_gbce_index(cls):
        try:
            print('GBCE All Share Index: {}'.format(calculate_gbce_all_share_index()))
        except ValueError as e:
            print(str(e))

