"""Unittests vstr.py."""

import pytest

from vhelpers import vstr
from vhelpers.types_ import LStr, DAny

APOSTROPHE = "'"
SPEECH = "\""


@pytest.mark.parametrize("cmd, expected", [
    ("", ""),
    ("description VALUE", "VALUE"),
    ("description \tVALUE\t", "VALUE"),
    ("descriptionTYPO", ""),
    ("    description SPACES", ""),
])
def test__cmd_value(cmd, expected):
    """vstr.cmd_value()."""
    actual = vstr.cmd_value(key="description", cmd=cmd)
    assert actual == expected


@pytest.mark.parametrize("args, kwargs, expected", [
    ([], {}, ""),
    (["a"], {}, "a"),
    ([], {"a": "a"}, "a=a"),
    (["a", "b"], {"c": "c", "d": "d"}, "a, b, c=c, d=d"),
])
def test__repr_info(args: LStr, kwargs: DAny, expected: str):
    """vstr.repr_info()"""
    actual = vstr.repr_info(*args, **kwargs)
    actual = actual.replace(APOSTROPHE, SPEECH)
    assert actual == expected


@pytest.mark.parametrize("args, kwargs, expected", [
    ([], {}, ""),
    (["a"], {}, "\"a\""),
    ([], {"a": "a"}, "a=\"a\""),
    (["a", "b"], {"c": "c", "d": "d"}, "\"a\", \"b\", c=\"c\", d=\"d\""),
])
def test__repr_params(args: LStr, kwargs: DAny, expected: str):
    """vstr.repr_params()"""
    actual = vstr.repr_params(*args, **kwargs)
    actual = actual.replace(APOSTROPHE, SPEECH)
    assert actual == expected


@pytest.mark.parametrize("line, expected", [
    ("", ""),
    ("abc", "cba"),
])
def test__repr_params_2(line: str, expected: str):
    """vstr.reverse() 2"""
    actual = vstr.reverse(line=line)
    assert actual == expected
