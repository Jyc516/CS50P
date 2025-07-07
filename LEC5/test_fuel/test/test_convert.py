from fuel import convert
from pytest import raises

def test_float():
    with raises(ValueError) as excinfo:
        convert("1.1/2")
    assert excinfo.type is ValueError


def test_string():
    with raises(ValueError) as excinfo:
        convert("cat/dog")
    assert excinfo.type is ValueError


def test_greater():
    with raises(ValueError) as excinfo:
        convert("2/1")
    assert excinfo.type is ValueError


def test_negative():
    with raises(ValueError) as excinfo:
        convert("-1/0")
    assert excinfo.type is ValueError

    
def test_zero_division():
    with raises(ZeroDivisionError) as excinfo:
        convert("1/0")
    assert excinfo.type is ZeroDivisionError


def test_round():
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("0/1") == 0
    assert convert("1/1") == 100