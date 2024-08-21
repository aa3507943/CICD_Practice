from main import Calculator

def test_multiply():
    assert Calculator().multiply(7, 13) == 91

if __name__ == "__main__":
    try:
        test_multiply()
        print("test_multiply pass")
    except Exception as e:
        print(f"test_multiply failed: {e}")
        exit(1)