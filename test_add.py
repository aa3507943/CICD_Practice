from main import Calculator
def test_add():
    assert Calculator().add(2, 7) == 9

if __name__ == "__main__":
    test_add()