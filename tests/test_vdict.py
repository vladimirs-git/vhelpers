"""Unittests vdict.py."""
import pytest

from vhelpers import vdict

POP_D = [
    (1, {1: 2}, 2),
    (2, {1: 2}, None),
]


@pytest.mark.parametrize("key, data, expected", POP_D)
def test_pop_d(key, data, expected):
    """pop_d."""
    actual = vdict.pop_d(key=key, data=data)
    assert actual == expected
