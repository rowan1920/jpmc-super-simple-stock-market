import json

from console import Console
from utils import global_variables
from utils.helpers import hydrate_stocks


if __name__ == '__main__':
    with open('GBCE_sample_data.json', 'r') as f:
        global_variables.stocks = hydrate_stocks(json.load(f))

    while True:
        Console.main_menu()
