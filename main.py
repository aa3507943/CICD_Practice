import pytest
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    
def test_add():
    assert Calculator().add(1, 2) == 3

def test_subtract():
    assert Calculator().subtract(4, 2) == 2

def test_multiply():
    assert Calculator().multiply(7, 13) == 91

def test_divide():
    assert Calculator().divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        Calculator().divide(10, 0)
