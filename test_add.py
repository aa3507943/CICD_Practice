from main import Calculator
import os
def test_add():
    assert Calculator().add(2, 7) == 9

if __name__ == "__main__":
    if os.path.isdir("./logs") == False:
        os.mkdir("./logs")
    if os.path.isfile("./logs/test_add_log.log") == False:
        os.mkdir("./logs/test_add_log.log")
    try:
        test_add()
        print("test_add pass")
    except AssertionError as e:
        print(f"test_add failed: {e}")
        exit(1)