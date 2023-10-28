"""Unittests vdate.py."""

import datetime
from unittest.mock import patch, Mock

import pytest

from vhelpers import vdate


def test__time_fmt():
    """vdate.TIME_FMT"""
    assert vdate.TIME_FMT == "%Y-%m-%d %H:%M:%S"


@pytest.mark.parametrize("delta, expected", [
    ({"hours": 0, "minutes": 0, "seconds": 0}, "00:00:00"),
    ({"hours": 2, "minutes": 3, "seconds": 4}, "02:03:04"),
    ({"hours": 8810, "minutes": 3, "seconds": 4}, "8810:03:04"),
])
def test__aged(delta, expected):
    """vdate.aged()"""
    actual = vdate.aged(delta_=delta)
    assert actual == expected


@pytest.mark.parametrize("now, expected", [
    ("2000-01-01 0:0:0", {"hours": 0, "minutes": 0, "seconds": 0}),
    ("2000-01-01 2:3:4", {"hours": 2, "minutes": 3, "seconds": 4}),
    ("2000-01-02 2:3:4", {"hours": 26, "minutes": 3, "seconds": 4}),
    ("2001-01-02 2:3:4", {"hours": 8810, "minutes": 3, "seconds": 4}),
])
def test__delta(now: str, expected: dict):
    """vdate.delta()"""
    start = datetime.datetime(2000, 1, 1)
    datetime_mock = Mock(wraps=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime.strptime(now, vdate.TIME_FMT)
    with patch("datetime.datetime", new=datetime_mock):
        actual = vdate.delta(start=start)
        assert actual == expected


def test__delta_2():
    """vdate.delta() """
    start = datetime.datetime(2000, 1, 1)
    end = datetime.datetime(2000, 1, 1, 23, 30, 31)
    expected = {"hours": 23, "minutes": 30, "seconds": 31}
    actual = vdate.delta(start=start, end=end)
    assert actual == expected
