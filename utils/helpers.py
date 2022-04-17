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

def hydrate_stocks(data) -> Dict[str, Stock]:
    hydrated_stocks: Dict[str, Stock] = {}
    for stock_data in data:
        hydrated_stocks[stock_data['symbol']] = Stock(**stock_data)
    return hydrated_stocks
