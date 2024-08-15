import pytest
from numb3rs import validate

def main():
    test_valid_ip()
    test_ip_range()

def test_valid_ip():
    assert validate(r'1.2.3.4') == True
    assert validate(r'192.168.3.0') == True
    assert validate(r'512.512.512.512.0') == False
    assert validate(r'cat') == False

def test_ip_range():
    assert validate('255.255.255.255') == True
    assert validate('512.1.1.1') == False
    assert validate('1.512.1.1') == False
    assert validate('1.1.512.1') == False
    assert validate('1.1.1.512') == False

if __name__ == "__main__":
    main()