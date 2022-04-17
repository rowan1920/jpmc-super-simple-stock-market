from typing import Dict


def hydrate_stocks(data) -> Dict[str, Stock]:
    hydrated_stocks: Dict[str, Stock] = {}
    for stock_data in data:
        hydrated_stocks[stock_data['symbol']] = Stock(**stock_data)
    return hydrated_stocks
