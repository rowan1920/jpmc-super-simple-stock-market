"""
This module is used in place of a database to store shared data globally.
"""
from typing import Dict, List

from models import Stock, Trade

trades: List[Trade] = []
stocks: Dict[str, Stock] = {}
