from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"


def test_uppercase():
    assert shorten("DAVID") == "DVD"


def test_sentence():
    assert shorten("Hello, CS50") == "Hll, CS50"