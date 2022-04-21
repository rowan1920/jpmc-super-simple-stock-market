import unittest

from pydantic import ValidationError

from models.stock import Stock


class TestSock(unittest.TestCase):
    def test_init_works_with_valid_parameters(self):
        initialised_stock = Stock(symbol="POP", type="common", last_dividend=8, fixed_dividend=0.2, par_value=100)
        self.assertEqual(initialised_stock.symbol, "POP")
        self.assertEqual(initialised_stock.type, "common")
        self.assertEqual(initialised_stock.last_dividend, 8)
        self.assertEqual(initialised_stock.fixed_dividend, 0.2)
        self.assertEqual(initialised_stock.par_value, 100)

    def test_init_works_without_optional_arguments(self):
        initialised_stock = Stock(symbol="POP", type="common", last_dividend=8, par_value=100)
        self.assertEqual(initialised_stock.fixed_dividend, None)

    def test_init_fails_without_required_parameters(self):
        with self.assertRaises(ValidationError) as context:
            Stock(symbol="POP")
        self.assertTrue('3 validation errors for Stock' in str(context.exception))

    def test_calculate_dividend_yield_returns_valid_value_for_common_stocks(self):
        stock = Stock(symbol="POP", type="common", last_dividend=8, fixed_dividend=0.2, par_value=100)
        self.assertEqual(stock.calculate_dividend_yield(100), 0.08)

    def test_calculate_dividend_yield_returns_valid_value_for_preferred_stocks(self):
        stock = Stock(symbol="POP", type="preferred", last_dividend=8, fixed_dividend=0.2, par_value=100)
        self.assertEqual(stock.calculate_dividend_yield(100), 0.2)

    def test_calculate_dividend_yield_handles_division_by_zero(self):
        stock = Stock(symbol="POP", type="preferred", last_dividend=8, fixed_dividend=0.2, par_value=100)
        self.assertEqual(stock.calculate_dividend_yield(0), 0)


if __name__ == '__main__':
    unittest.main()