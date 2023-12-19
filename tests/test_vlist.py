"""Unittests vlist.py."""
from datetime import date
from typing import Any

import pytest

from vhelpers import vlist


@pytest.mark.parametrize("items, expected", [
    ([], []),
    ([1, 2, 1], [1]),
    ((1, 2, 1), [1]),
    (["1", "2", "1"], ["1"]),
    ([{1}, {2}, {1}], [{1}]),
    ([{1: 1}, {1: 2}, {1: 1}], [{1: 1}]),
    ([{1: 1}, 1, "1", {1}], []),
    ([{1: 1}, 1, "1", {1}, 1, {1}], [1, {1}]),
    ({1: 1, 2: 1}, []),
])
def test__dupl(items: Any, expected: Any):
    """vlist.dupl()"""
    if isinstance(expected, list):
        actual = vlist.dupl(items)
        assert actual == expected
    else:
        with pytest.raises(expected):
            vlist.dupl(items)


@pytest.mark.parametrize("items, expected", [
    ([], []),
    ([1], [1]),
    ([1, [2, [3]], 4, [5, [6]]], [1, 2, 3, 4, 5, 6]),
    ("12", ["1", "2"]),
    (["12"], ["12"]),
    (["12", ["34", ["56"]], "78", ["90", ["ab"]]], ["12", "34", "56", "78", "90", "ab"]),
    (b"12", [49, 50]),
    ([b"12"], [b"12"]),
])
def test__flatten(items, expected):
    """vlist.flatten()"""
    actual = vlist.flatten(items)
    assert actual == expected


@pytest.mark.parametrize("items1, items2, expected", [
    ([], [], False),
    ([], [1], False),
    ([1, 2], [], False),
    ([1, 2], [3], False),
    ([1, 2], [1, 3], True),
    ([1, 2], [2, 3], True),
])
def test__is_in(items1, items2, expected):
    """vlist.is_in()."""
    actual = vlist.is_in(items1=items1, items2=items2)
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


@pytest.mark.parametrize("items, old, new, expected", [
    ([], None, None, []),
    ([1], None, None, [1]),
    ([None], None, None, [None]),
    ([None], None, 1, [1]),
    ([1, 2, 3], 2, 4, [1, 4, 3]),
    ([1, {2: 2}, 3], {2: 2}, 4, [1, 4, 3]),
])
def test__replace(items: list, old: Any, new: Any, expected: list):
    """vlist.replace()."""
    vlist.replace(items=items, old=old, new=new)
    assert items == expected


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
def test__to_list(items, expected):
    """vlist.to_list()."""
    actual = vlist.to_list(items=items)
    if isinstance(items, set):
        actual.sort()
    assert actual == expected


@pytest.mark.parametrize("items, count, expected", [
    ([], -1, []),
    ([], 0, []),
    ([], 1, [[]]),
    ([], 2, [[], []]),
    ([], 3, [[], [], []]),
    ([1, 2, 3, 4, 5], 0, []),
    ([1, 2, 3, 4, 5], 1, [[1, 2, 3, 4, 5]]),
    ([1, 2, 3, 4, 5], 2, [[1, 2, 3], [4, 5]]),
    ([1, 2, 3, 4, 5], 3, [[1, 2], [3, 4], [5]]),
    ([1, 2, 3, 4, 5], 4, [[1, 2], [3, 4], [5], []]),
    ([1, 2, 3, 4, 5], 5, [[1], [2], [3], [4], [5]]),
    ([1, 2, 3, 4, 5], 6, [[1], [2], [3], [4], [5], []]),
    ([1, 2, 3, 4, 5], 7, [[1], [2], [3], [4], [5], [], []]),
])
def test__to_lists(items, count, expected):
    """vlist.to_lists()."""
    actual = vlist.to_lists(items=items, count=count)
    assert actual == expected


@pytest.mark.parametrize("items, count, expected", [
    ([], 1, []),
    ([1], 1, [[1]]),
    ([1, 2, 3], 1, [[1], [2], [3]]),
    ([1, 2, 3], 2, [[1, 2], [3]]),
])
def test__to_multi(items, count, expected):
    """vlist.to_multi()"""
    actual = vlist.to_multi(items=items, count=count)
    assert actual == expected
