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
    assert Calculator().add(2, 7) == 9

def test_subtract():
    assert Calculator().subtract(19, 6) == 13

def test_multiply():
    assert Calculator().multiply(7, 13) == 91

def test_divide():
    assert Calculator().divide(13, 4) == 3.25
    with pytest.raises(ZeroDivisionError):
        Calculator().divide(10, 0)
