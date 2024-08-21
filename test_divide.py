from main import Calculator
def test_subtract():
    assert Calculator().subtract(19, 6) == 13

if __name__ == '__main__':
    try:
        test_subtract()
        print("test_subtract pass")
    except AssertionError as e:
        print(f"test_subtract failed: {e}")
        exit(1)