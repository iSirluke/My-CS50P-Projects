from twttr import shorten

def main():
    test_letterCase()
    test_numbers()
    test_punctuation()

def test_letterCase():
    assert shorten('luke') == 'lk'
    assert shorten('IPAD') == 'PD'
    assert shorten('TabLe') == 'TbL'

def test_numbers():
    assert shorten('4567') == '4567'

def test_punctuation():
    assert shorten('!?.,') == '!?.,'

if __name__ == "__main__":
    main()