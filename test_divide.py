from main import Calculator
def test_subtract():
    assert Calculator().subtract(19, 6) == 13

if __name__ == '__main__':
    test_subtract()