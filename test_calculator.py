"""
Unit testing the calculator app
"""

import calculator


class TestCalculator:

    def test_add(self):
        assert 5 == calculator.addition(1, 4)

    def test_subtract(self):
        assert 2 == calculator.subtraction(5, 3)

    def test_multiply(self):
        assert 2 == calculator.multiply(1, 2)

    def test_multiply1(self):
        assert 0 == calculator.multiply(1, 0)

    def test_multiply2(self):
        assert -2 == calculator.multiply(-1, 2)
