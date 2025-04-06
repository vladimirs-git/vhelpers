"""Tests vint.py."""

import pytest

from vhelpers import vint
from vhelpers.types_ import IntStr


@pytest.mark.parametrize("digit, expected", [
    (0, 0),
    (1, 1),
    ("", 0),
    ("a", 0),
    ("a1", 0),
    ("0", 0),
    ("1", 1),
    ("1 ", 1),
])
def test__to_int(digit: IntStr, expected: int):
    """vint.to_int()."""
    actual = vint.to_int(digit=digit)
    assert actual == expected


@pytest.mark.parametrize("digit, expected", [
    (0, "0th"),
    (1, "1st"),
    (2, "2nd"),
    (3, "3rd"),
    (4, "4th"),
    (10, "10th"),
    (11, "11th"),
    (12, "12th"),
    (13, "13th"),
    (21, "21st"),
    (22, "22nd"),
    (23, "23rd"),
    (24, "24th"),
    (101, "101st"),
    (-1, "-1st"),
    ("1", "1st"),
    ("a", "0th"),
    ("", "0th"),
])
def test__to_ordinal(digit: IntStr, expected: str):
    """vint.to_ordinal()."""
    actual = vint.to_ordinal(digit=digit)
    assert actual == expected
