"""Unittests vparam.py."""
import pytest

from vhelpers import vparam


@pytest.mark.parametrize("params_d, expected", [
    ({}, []),
    ({"a": 1}, [("a", 1)]),
    ({"a": 1, "b": 1}, [("a", 1), ("b", 1)]),
    ({"a": [1, 1]}, [("a", 1), ("a", 1)]),
    ({"a": [1, 1], "b": [1, 1]}, [("a", 1), ("a", 1), ("b", 1), ("b", 1)]),
])
def test__from_dict(params_d, expected):
    """vparam.from_dict()."""
    actual = vparam.from_dict(params_d=params_d)
    assert actual == expected


@pytest.mark.parametrize("params_, expected", [
    ([], {}),
    ([("a", 1)], {"a": 1}),
    ([("a", 1), ("b", 1)], {"a": 1, "b": 1}),
    ([("a", 1), ("a", 1)], {"a": [1, 1]}),
    ([("a", 1), ("b", 1), ("a", 1), ("b", 1)], {"a": [1, 1], "b": [1, 1]}),
])
def test__to_dict(params_, expected):
    """vparam.to_dict()."""
    actual = vparam.to_dict(params=params_)
    assert actual == expected
