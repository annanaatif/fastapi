from app.calculations import add, subtract, multiply, divide
import pytest

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 5),
    (5, 7, 12),
    (10, 20, 30)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 2),
    (10, 5, 5),
    (20, 10, 10)
])
def test_subtract(num1, num2, expected):
    assert subtract(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 6),
    (5, 7, 35),
    (10, 20, 200)
])
def test_multiply(num1, num2, expected):
    assert multiply(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (6, 3, 2),
    (10, 5, 2),
    (20, 10, 2)
])
def test_divide(num1, num2, expected):
    assert divide(num1, num2) == expected