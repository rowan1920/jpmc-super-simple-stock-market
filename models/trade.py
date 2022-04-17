import re
from datetime import datetime
from pydantic import BaseModel, validator

from models import Stock


VALID_TRADE_TYPE_EXPRESSION: str = r'^(buy|sell)$'


class Trade(BaseModel):
    """
    Args:
        stock (Stock): A Stock model.
        timestamp (datetime): A timestamp class with the time of the trade
        quantity (int): Number of stocks traded
        type (str): Trade type, either `buy` or `sell`
        traded_price (int): Price per share of trade in pence
    """
    stock: Stock
    timestamp: datetime
    quantity: int
    type: str
    traded_price: int

    @validator('quantity')
    def check_quantity(cls, v: int) -> int:
        if v <= 0:
            raise ValueError('Trade quantity must be greater than zero')
        return v

    @validator('type')
    def check_type(cls, v: str) -> str:
        if not re.match(VALID_TRADE_TYPE_EXPRESSION, v):
            raise ValueError('Trade type doesn\'t match the regex "{}"'.format(VALID_TRADE_TYPE_EXPRESSION))
        return v

    @validator('traded_price')
    def check_traded_price(cls, v: int) -> int:
        if v <= 0:
            raise ValueError('Trade traded_price must be greater than zero')
        return v
