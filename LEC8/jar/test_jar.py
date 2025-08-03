from jar import Jar
from pytest import raises


def test_init():
    with raises(ValueError) as excinfo:
        Jar(-3)
    assert excinfo.type is ValueError


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with raises(ValueError) as excinfo:
        jar.deposit(13)
    assert excinfo.type is ValueError


def test_withdraw():
    jar = Jar()
    with raises(ValueError) as excinfo:
        jar.withdraw(1)
    assert excinfo.type is ValueError