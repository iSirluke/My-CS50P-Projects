import bank
from bank import value

def main():
    test_zero()
    test_twenty()
    test_hundred()

def test_zero():
    assert value('hello') == 0
    assert value('Hello') == 0
    assert value('heLLo') == 0

def test_twenty():
    assert value('hi') == 20
    assert value('Hai') == 20
    assert value('hie') == 20

def test_hundred():
    assert value('Good morning') == 100
    assert value('Welcome') == 100
    assert value('Evening Luke') == 100

if __name__ == "__main__":
    main()