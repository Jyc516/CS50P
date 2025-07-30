from um import count


def test_mixed():
    assert count("yummy") == 0
    assert count("um, yum") == 1
    assert count("umm") == 0


def test_case():
    assert count("Um...You're right") == 1


def test():
    assert count("hello, um, world") == 1
    assert count("um, um") == 2
    assert count("um") == 1