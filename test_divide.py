from main import Calculator
import os
def test_subtract():
    assert Calculator().subtract(19, 6) == 13

if __name__ == '__main__':
    if os.path.isdir("./logs") == False:
        os.mkdir("./logs")
    if os.path.isfile("./logs/test_subtract_log.log") == False:
        os.mkdir("./logs/test_subtract_log.log")
    try:
        test_subtract()
        print("test_subtract pass")
    except AssertionError as e:
        print(f"test_subtract failed: {e}")
        exit(1)