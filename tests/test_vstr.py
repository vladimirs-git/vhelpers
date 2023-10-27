"""Unittests vstr.py."""

import pytest

from vhelpers import vstr
from vhelpers.types_ import LStr, DAny

APOSTROPHE = "'"
SPEECH = "\""


@pytest.mark.parametrize("args, kwargs, expected", [
    ([], {}, ""),
    (["a"], {}, "\"a\""),
    ([], {"a": "a"}, "a=\"a\""),
    (["a", "b"], {"c": "c", "d": "d"}, "\"a\", \"b\", c=\"c\", d=\"d\""),
])
def test_valid__repr_params(args: LStr, kwargs: DAny, expected: str):
    """vstr.repr_params()"""
    actual = vstr.repr_params(*args, **kwargs)
    actual = actual.replace(APOSTROPHE, SPEECH)
    assert actual == expected
