from main import Calculator
import pytest

def test_divide():
    assert Calculator().divide(13, 4) == 3.25
    with pytest.raises(ZeroDivisionError):
        Calculator().divide(10, 0)