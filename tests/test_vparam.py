"""Unittests vparam.py."""
import pytest

from vhelpers import vparam

FROM_DICT = [
    ({}, []),
    ({"a": 1}, [("a", 1)]),
    ({"a": 1, "b": 1}, [("a", 1), ("b", 1)]),
    ({"a": [1, 1]}, [("a", 1), ("a", 1)]),
    ({"a": [1, 1], "b": [1, 1]}, [("a", 1), ("a", 1), ("b", 1), ("b", 1)]),
]

TO_DICT = [
    ([], {}),
    ([("a", 1)], {"a": 1}),
    ([("a", 1), ("b", 1)], {"a": 1, "b": 1}),
    ([("a", 1), ("a", 1)], {"a": [1, 1]}),
    ([("a", 1), ("b", 1), ("a", 1), ("b", 1)], {"a": [1, 1], "b": [1, 1]}),
]


@pytest.mark.parametrize("params_d, expected", FROM_DICT)
def test__from_dict(params_d, expected):
    """from_dict."""
    actual = vparam.from_dict(params_d=params_d)
    assert actual == expected


@pytest.mark.parametrize("params_, expected", TO_DICT)
def test__to_dict(params_, expected):
    """to_dict."""
    actual = vparam.to_dict(params=params_)
    assert actual == expected
