"""
This module is used in place of a database to store shared data globally.
"""
from typing import Dict

from models import Stock

stocks: Dict[str, Stock] = {}
