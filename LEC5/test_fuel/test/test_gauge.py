from fuel import gauge

def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_other():
    assert gauge(50) == "50%"
    assert gauge(33) == "33%"