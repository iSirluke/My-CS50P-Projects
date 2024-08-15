import plates
from plates import is_valid

def main():
    test_length()
    test_digits()
    test_firstChar()

def test_length():
    assert is_valid('a') == False
    assert is_valid('AA') == True
    assert is_valid('CS50') == True
    assert is_valid('AB2613') == True

def test_digits():
    assert is_valid('AAA444') == True
    assert is_valid('21') == False
    assert is_valid('AB021') == False

def test_characters():
    assert is_valid('CS,.50') == False
    assert is_valid('cs50') == True
    assert is_valid('cs50b') == False



if __name__ == "__main__":
    main()
