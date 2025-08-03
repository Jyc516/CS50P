import seasons
from pytest import raises
from datetime import date, timedelta


def test_get():
    with raises(SystemExit) as excinfo:
        seasons.get("January 1, 1999")
    assert excinfo.type is SystemExit
    assert seasons.get("1991-01-01") == date(1991, 1, 1)


def test_output():
    assert seasons.output(timedelta(365)) == "Five hundred twenty-five thousand, six hundred minutes"
    assert seasons.output(timedelta(1)) == "One thousand, four hundred forty minutes"
    assert seasons.output(timedelta(10957)) == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"
