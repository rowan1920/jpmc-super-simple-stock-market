import re
from typing import Optional
from pydantic import BaseModel, validator


VALID_STOCK_SYMBOL_EXPRESSION: str = r'^[A-Z]{3}$'
VALID_STOCK_TYPE_EXPRESSION: str = r'^(preferred|common)$'


class Stock(BaseModel):
    """
    Args:
        symbol (str): 3 letter stock symbol.
        type (str): Either `preferred` or `common`
        last_dividend (int): Value of the last dividend in pence
        fixed_dividend (float): An optional fixed_dividend rate
        par_value (int): Par value in pence
    """
    symbol: str
    type: str
    last_dividend: int
    fixed_dividend: Optional[float]
    par_value: int

    @validator('symbol')
    def check_symbol(cls, v: str) -> str:
        if not re.match(VALID_STOCK_SYMBOL_EXPRESSION, v):
            raise ValueError('Stock symbol doesn\'t match the regex "{}"'.format(VALID_STOCK_SYMBOL_EXPRESSION))
        return v

    @validator('type')
    def check_type(cls, v: str) -> str:
        if not re.match(VALID_STOCK_TYPE_EXPRESSION, v):
            raise ValueError('Stock type doesn\'t match the regex "{}"'.format(VALID_STOCK_TYPE_EXPRESSION))
        return v

    @validator('last_dividend')
    def check_last_dividend(cls, v: int) -> int:
        if v < 0:
            raise ValueError('Stock last_dividend must be positive or zero')
        return v

    @validator('fixed_dividend')
    def check_fixed_dividend(cls, v: Optional[float]) -> Optional[float]:
        if (v is not None) and (v < 0):
            raise ValueError('Stock {}: fixed_dividend must be positive, zero or not set'.format(v))
        return v

    @validator('par_value')
    def check_par_value(cls, v: int) -> int:
        if v <= 0:
            raise ValueError('Stock par_value must be greater than zero')
        return v

    def calculate_dividend(self) -> float:
        if self.type == 'preferred':
            return self.fixed_dividend * self.par_value
        else:
            return self.last_dividend

    def calculate_dividend_yield(self, price: int) -> float:
        try:
            to_return: float = self.calculate_dividend() / price
        except ZeroDivisionError:
            to_return: float = 0
        return to_return

    def calculate_pe_ratio(self, price: int) -> float:
        dividend: float = self.calculate_dividend()
        try:
            to_return: float = price / dividend
        except ZeroDivisionError:
            to_return: float = 0
        return to_return
