"""Unittests vlist.py."""
from datetime import date

import pytest

from vhelpers import vlist


@pytest.mark.parametrize("items, expected", [
    ([], []),
    (tuple(), []),
    (set(), []),
    ([1, 2], [1, 2]),
    ((1, 2), [1, 2]),
    ({1, 2}, [1, 2]),
    ("12", ["12"]),
    (b"0", [b"0"]),
    (0, [0]),
    ({0: 0}, [{0: 0}]),
    (None, []),
    (date(2000, 12, 31), [date(2000, 12, 31)])
])
def test__from_any(items, expected):
    """vlist.from_any()."""
    actual = vlist.from_any(items=items)
    if isinstance(items, set):
        actual.sort()
    assert actual == expected


@pytest.mark.parametrize("items, expected", [
    ([], []),
    (["a", "b", "a"], ["a", "b"]),
    (("a", "b", "a"), ["a", "b"]),
    ([1, 2, 1], [1, 2]),
    ([["a"], ["b"], ["a"]], [["a"], ["b"]]),
    ([{"a": 1}, {"b": 2}, {"a": 1}], [{"a": 1}, {"b": 2}]),
])
def test__no_dupl(items, expected):
    """vlist.no_dupl()."""
    actual = vlist.no_dupl(items=items)
    assert actual == expected


@pytest.mark.parametrize("text, chars, ignore, expected", [
    ("a", "", "", ["a"]),
    ("a", "-", "", ["a"]),
    ("a", "", "-", ["a"]),
    ("a", "-", "-", ["a"]),
    ("a-b_c.d", "", "", ["a", "b", "c", "d"]),
    ("a-b_c.d", "b", "", ["a", "c", "d"]),
    ("a-b_c.d", "", "-", ["a-b", "c", "d"]),
    ("a-b_c.d", "b", "-", ["a-", "c", "d"]),
    ("a!b", "", "", ["a", "b"]),
    ("a(b", "", "", ["a", "b"]),
    ("a(b)c", "", "", ["a", "b", "c"]),
    ("domain.com", "", ".", ["domain.com"]),
    ("rix1-fw-t001-asa,rix1-fw-t002-asa rix1-fw-t003-asa", "", "-",
     ["rix1-fw-t001-asa", "rix1-fw-t002-asa", "rix1-fw-t003-asa"]),
])
def test__split(text: str, chars: str, ignore: str, expected):
    """vlist.split()."""
    actual = vlist.split(text=text, chars=chars, ignore=ignore)
    assert actual == expected
