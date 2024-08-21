from main import Calculator

def test_multiply():
    assert Calculator().multiply(7, 13) == 91

if __name__ == "__main__":
    test_multiply()