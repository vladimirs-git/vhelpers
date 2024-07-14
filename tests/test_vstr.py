"""Tests vstr.py."""

import pytest

from vhelpers import vstr

APOSTROPHE = "'"
SPEECH = "\""


@pytest.mark.parametrize("args, expected", [
    ([], ""),
    ([",", "a", "", 0, ], "a,0"),
    ([",", " a ", " ", 0], " a , ,0"),
    (["\n", "a", "", 0], "a\n0"),
    (["\n", " a\n", " ", 0], " a\n\n \n0"),
])
def test__join(args, expected):
    """vstr.join()"""
    actual = vstr.join(*args)
    assert actual == expected


@pytest.mark.parametrize("args, expected", [
    ([], ""),
    (["a", "", 0], "a\n0"),
    (["a\n", " ", 0], "a\n\n \n0"),
])
def test__join_lines(args, expected):
    """vstr.join_lines()"""
    actual = vstr.join_lines(*args)
    assert actual == expected


@pytest.mark.parametrize("args, kwargs, expected", [
    ([], {}, ""),
    (["a"], {}, "a"),
    ([], {"a": "a"}, "a=a"),
    (["a", "b"], {"c": "c", "d": "d"}, "a, b, c=c, d=d"),
])
def test__repr_info(args, kwargs, expected):
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
def test__repr_params(args, kwargs, expected):
    """vstr.repr_params()"""
    actual = vstr.repr_params(*args, **kwargs)
    actual = actual.replace(APOSTROPHE, SPEECH)
    assert actual == expected


@pytest.mark.parametrize("line, expected", [
    ("", ""),
    ("abc", "cba"),
])
def test__repr_params_2(line, expected):
    """vstr.reverse() 2"""
    actual = vstr.reverse(line=line)
    assert actual == expected


@pytest.mark.parametrize("text, idx, expected", [
    ("before_after", 0, ("", "before_after")),
    ("before_after", 6, ("before", "_after")),
    ("before_after", 7, ("before_", "after")),
    ("before_after", 100, ("before_after", "")),
])
def test__split_idx(text, idx, expected):
    """vstr.split_idx()"""
    actual = vstr.split_idx(text=text, idx=idx)
    assert actual == expected
