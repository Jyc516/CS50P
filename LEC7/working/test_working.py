from working import convert
from pytest import raises


def test_hour():
    with raises(ValueError) as excinfo:
        convert("9:00 AM to 13:00 PM")
    assert  excinfo.type is ValueError


def test_min():
    with raises(ValueError) as excinfo:
        convert("9:60 AM to 5:60 PM")
    assert excinfo.type is ValueError
    with raises(ValueError) as excinfo:
        convert("10:7 AM - 5:1 PM")
    assert excinfo.type is ValueError


def test_format():
    with raises(ValueError) as excinfo:
        convert("cat")
    assert excinfo.type is ValueError
    with raises(ValueError) as excinfo:
        convert("9:00 AM - 5:00 PM")
    assert excinfo.type is ValueError
    with raises(ValueError) as excinfo:
        convert("9AM to 5PM")
    assert excinfo.type is ValueError


def test_True():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"