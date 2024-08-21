from main import Calculator
import os
def test_multiply():
    assert Calculator().multiply(7, 13) == 91

if __name__ == "__main__":
    if os.path.isdir("./logs") == False:
        os.mkdir("./logs")
    if os.path.isfile("./logs/test_multiply_log.log") == False:
        os.mkdir("./logs/test_multiply_log.log")
    try:
        test_multiply()
        print("test_multiply pass")
    except Exception as e:
        print(f"test_multiply failed: {e}")
        exit(1)