from main import Calculator
import pytest, os

def test_divide():
    assert Calculator().divide(13, 4) == 3.25
    with pytest.raises(ZeroDivisionError):
        Calculator().divide(10, 0)

if __name__ == "__main__":
    if os.path.isdir("./logs") == False:
        os.mkdir("./logs")
    if os.path.isfile("./logs/test_divide_log.log") == False:
        os.mkdir("./logs/test_divide_log.log")
    try:
        test_divide()
        print("test_divide pass")
    except AssertionError as e:
        print(f"test_divide failed: {e}")
        exit(1)