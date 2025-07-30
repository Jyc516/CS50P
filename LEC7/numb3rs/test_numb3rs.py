from numb3rs import validate

def test_format():
    assert validate("1") == False
    assert validate("1.1") == False
    assert validate("1.1.1") == False
    assert validate("1,3.2.4") == False
    assert validate("cat") == False


def test_number():
    assert validate("0.1.2.3") == True
    assert validate("1.12.123.1") == True
    assert validate("1.12.123.1234") == False
    assert validate("255.255.255.256") == False
    assert validate("000.001.010.100") == False