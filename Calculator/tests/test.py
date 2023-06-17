import pytest

from app.calc import Calculator

class TestCalculator:

    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 5, 5) == 25

    def test_summ(self):
        assert self.calc.summ(self, 5, 5) == 10

    def test_difference(self):
        assert self.calc.difference(self, 10, 5) == 5

    def test_devide(self):
        assert self.calc.devide(self, 10, 5) == 2

    def test_devide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            assert self.calc.devide_by_zero(self, 10, 0) == 0

    def test_sqrt(self):
        assert self.calc.sqrt(self, 9) == 3

    def test_square(self):
        assert self.calc.square(self, 5, 2) == 25



    def teardown(self):
        print('Выполнение метода Teardown')


