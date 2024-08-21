from main import Calculator
def test_add():
    assert Calculator().add(2, 7) == 9

if __name__ == "__main__":
    try:
        test_add()
        print("test_add pass")
    except AssertionError as e:
        print(f"test_add failed: {e}")
        exit(1)