"""Unittests vlist.py."""
from datetime import date

import pytest

from vhelpers import vlist

FROM_ANY = [
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
]

NO_DUPL = [
    ([], []),
    (["a", "b", "a"], ["a", "b"]),
    (("a", "b", "a"), ["a", "b"]),
    ([1, 2, 1], [1, 2]),
    ([["a"], ["b"], ["a"]], [["a"], ["b"]]),
    ([{"a": 1}, {"b": 2}, {"a": 1}], [{"a": 1}, {"b": 2}]),
]


@pytest.mark.parametrize("items, expected", FROM_ANY)
def test__from_any(items, expected):
    """from_any."""
    actual = vlist.from_any(items=items)
    if isinstance(items, set):
        actual.sort()
    assert actual == expected


@pytest.mark.parametrize("items, expected", NO_DUPL)
def test__no_dupl(items, expected):
    """no_dupl."""
    actual = vlist.no_dupl(items=items)
    assert actual == expected
