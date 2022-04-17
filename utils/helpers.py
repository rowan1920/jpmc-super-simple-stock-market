from datetime import datetime, timedelta
from typing import Dict

from models import Trade, Stock
from utils import global_variables


def record_trade(stock: Stock, quantity: int, trade_type: str, price: int) -> None:
    current_timestamp = datetime.now()
    global_variables.trades.insert(0, (Trade(
        stock=stock,
        timestamp=current_timestamp,
        quantity=quantity,
        type=trade_type,
        traded_price=price
    )))


def calculate_volume_weighted_stock_price(stock_symbol: str) -> float:
    """
    Due to the structure of the trade data in memory, this method would need to loop through all stocks in the
    last 15 minutes. This would not be optimal in a production system with large amounts of data.
    """
    total_product_of_quantity_and_price: float = 0
    total_traded_quantity: float = 0
    time_15_minutes_ago: datetime = datetime.now() - timedelta(minutes=15)

    for trade in global_variables.trades:
        if trade.timestamp <= time_15_minutes_ago:
            break
        if trade.stock.symbol == stock_symbol:
            total_product_of_quantity_and_price += trade.traded_price * trade.quantity
            total_traded_quantity += trade.quantity

    if total_product_of_quantity_and_price == 0 or total_traded_quantity == 0:
        raise ValueError('There have been no trades for {} in the past 15 minutes'.format(stock_symbol))

    try:
        to_return = total_product_of_quantity_and_price / total_traded_quantity
    except ZeroDivisionError:
        to_return = 0

    return to_return


def calculate_gbce_all_share_index() -> float:
    if len(global_variables.trades) < 1:
        raise ValueError('There must be more than zero trades to calculate the GBCE All Share Index')
    total_trade_quantity: float = 0
    total_trade_value: float = 1

    for trade in global_variables.trades:
        total_trade_quantity += trade.quantity
        total_trade_value = total_trade_value * pow(trade.traded_price, trade.quantity)
    try:
        to_return = total_trade_value**(1/total_trade_quantity)
    except ZeroDivisionError:
        to_return = 0

    return to_return


def hydrate_stocks(data) -> Dict[str, Stock]:
    hydrated_stocks: Dict[str, Stock] = {}
    for stock_data in data:
        hydrated_stocks[stock_data['symbol']] = Stock(**stock_data)
    return hydrated_stocks
