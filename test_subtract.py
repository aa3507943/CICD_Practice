from main import Calculator
import pytest

def test_divide():
    assert Calculator().divide(13, 4) == 3.25
    with pytest.raises(ZeroDivisionError):
        Calculator().divide(10, 0)

if __name__ == "__main__":
    try:
        test_divide()
        print("test_divide pass")
    except AssertionError as e:
        print(f"test_divide failed: {e}")
        exit(1)