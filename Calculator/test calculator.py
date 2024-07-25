import pytest

from app.calculator import Calculator

class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 2, 2) == 4

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 999, 99) == 900

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 100, 100) == 10000

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 1024, 256) == 4

    def teardown(self):
        print('Выполнение метода Teardown')