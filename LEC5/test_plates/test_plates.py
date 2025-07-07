from plates import is_valid

def test_short():
    assert is_valid("A") == False


def test_long():
    assert is_valid("ABCDEFG") == False


def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True


def test_number():
    assert is_valid("A2A") == False


def test_beginning():
    assert is_valid("AA22") == True
    assert is_valid("A22") == False
    assert is_valid("2AA") == False
    assert is_valid("A'A") == False
    assert is_valid(" ") == False
    assert is_valid("ABC123") == True


def test_suffix():
    assert is_valid("AAA22A") == False


def test_period():
    assert is_valid("AA.22") == False


def test_true():
    assert is_valid("AAA222") == True
