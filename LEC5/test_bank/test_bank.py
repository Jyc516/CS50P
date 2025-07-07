from bank import value

def test_helloworld():
    assert value("hello, world") == 0


def test_spaceHI():
    assert value("  HI") == 20


def test_void():
    assert value("") == 100