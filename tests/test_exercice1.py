import pytest
import sys
sys.path.append("..")

from exercice1 import Calculator

calculator = Calculator()


def test_add():
    result = calculator.add(2, 3)
    assert result == 5
    assert calculator.get_memory() == 5


def test_subtract():
    result = calculator.subtract(5, 3)
    assert result == 2
    assert calculator.get_memory() == 2


def test_multiply():
    result = calculator.multiply(2, 4)
    assert result == 8
    assert calculator.get_memory() == 8


def test_divide():
    result = calculator.divide(10, 2)
    assert result == 5
    assert calculator.get_memory() == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(10, 0)


def test_power():
    result = calculator.power(2, 3)
    assert result == 8
    assert calculator.get_memory() == 8
