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
