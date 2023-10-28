"""Unittests vre.py."""
import re
from typing import Any

import pytest

from vhelpers import vre

TEXT = "a1\nb2\na1\nc3\nd4"


@pytest.mark.parametrize("kwargs, expected", [
    # empty
    ({'text': "", 'start': "", 'end': "", 'strict': True}, ""),
    ({'text': "", 'start': "", 'end': ""}, ""),
    ({'text': "", 'start': "a1", 'end': "c3"}, ""),
    # found
    ({'text': TEXT, 'start': "", 'end': "c3"}, "a1\nb2\na1\n"),
    ({'text': TEXT, 'start': "a1", 'end': "c3"}, "\nb2\na1\n"),
    ({'text': TEXT, 'start': "b2", 'end': "c3"}, "\na1\n"),
    ({'text': TEXT, 'start': "b2", 'end': "c3", 'w_start': True}, "b2\na1\n"),
    ({'text': TEXT, 'start': "b2", 'end': "c3", 'w_start': True, 'w_end': True}, "b2\na1\nc3"),
    ({'text': TEXT, 'start': "b2", 'end': "a1"}, "\n"),
    # not found
    ({'text': TEXT, 'start': "", 'end': ""}, ""),
    ({'text': TEXT, 'start': "a1", 'end': ""}, ""),
    ({'text': TEXT, 'start': "typo", 'end': "typo"}, ""),
    # error
    ({'text': TEXT, 'start': "a1", 'end': "typo", 'strict': True}, ValueError),
    ({'text': TEXT, 'start': "typo", 'end': "c3", 'strict': True}, ValueError),
    ({'text': TEXT, 'start': "typo", 'end': "typo", 'strict': True}, ValueError),
])
def test__between(kwargs: dict, expected: Any):
    """vre.between()"""
    if isinstance(expected, str):
        actual = vre.between(**kwargs)
        assert actual == expected
    else:
        with pytest.raises(expected):
            vre.between(**kwargs)


@pytest.mark.parametrize("pattern, string, flags, expected", [
    ("", "abcdef", 0, ""),
    ("typo", "abcdef", 0, ""),
    ("(typo)", "abcdef", 0, ""),
    ("(b)", "abcdef", 0, "b"),
    ("(b)", "a\nabcdef", re.M, "b"),
    ("(bc)", "abcdef", 0, "bc"),
    ("(b)(c)", "abcdef", 0, "b"),
    (1, "abcdef", 0, TypeError),
    ("", 1, 0, TypeError),
])
def test__find1(pattern: str, string: str, flags: int, expected: Any):
    """vre.find1()."""
    if isinstance(expected, str):
        actual = vre.find1(pattern=pattern, string=string, flags=flags)
        assert actual == expected
    else:
        with pytest.raises(expected):
            vre.find1(pattern=pattern, string=string, flags=flags)


@pytest.mark.parametrize("pattern, string, flags, expected", [
    ("", "abcdef", 0, ("", "")),
    ("typo", "abcdef", 0, ("", "")),
    ("(typo)", "abcdef", 0, ("", "")),
    ("(b)", "abcdef", 0, ("", "")),
    ("(b)(typo)", "abcdef", 0, ("", "")),
    ("(typo)(c)", "abcdef", 0, ("", "")),
    ("(b)(c)", "abcdef", 0, ("b", "c")),
    ("(b)(c)", "a\nabcdef", re.M, ("b", "c")),
    ("(b)(c)(d)", "abcdef", 0, ("b", "c")),
    (1, "abcdef", 0, TypeError),
    ("", 1, 0, TypeError),
])
def test__find2(pattern: str, string: str, flags: int, expected: Any):
    """vre.find2()."""
    if isinstance(expected, tuple):
        actual = vre.find2(pattern=pattern, string=string, flags=flags)
        assert actual == expected
    else:
        with pytest.raises(expected):
            vre.find2(pattern=pattern, string=string, flags=flags)


@pytest.mark.parametrize("pattern, string, flags, expected", [
    ("", "abcdef", 0, ("", "", "")),
    ("(b)", "abcdef", 0, ("", "", "")),
    ("(b)(c)", "abcdef", 0, ("", "", "")),
    ("(b)(c)(d)", "abcdef", 0, ("b", "c", "d")),
    ("(b)(c)(d)", "a\nabcdef", re.M, ("b", "c", "d")),
    ("(b)(c)(d)(e)", "abcdef", 0, ("b", "c", "d")),
    ("(b)(c)(typo)", "abcdef", 0, ("", "", "")),
    (1, "abcdef", 0, TypeError),
    ("", 1, 0, TypeError),
])
def test__find3(pattern: str, string: str, flags: int, expected: Any):
    """vre.find3()."""
    if isinstance(expected, tuple):
        actual = vre.find3(pattern=pattern, string=string, flags=flags)
        assert actual == expected
    else:
        with pytest.raises(expected):
            vre.find3(pattern=pattern, string=string, flags=flags)


@pytest.mark.parametrize("pattern, string, flags, expected", [
    ("", "abcdef", 0, ("", "", "", "")),
    ("(b)", "abcdef", 0, ("", "", "", "")),
    ("(b)(c)", "abcdef", 0, ("", "", "", "")),
    ("(b)(c)(d)", "abcdef", 0, ("", "", "", "")),
    ("(b)(c)(d)(e)", "abcdef", 0, ("b", "c", "d", "e")),
    ("(b)(c)(d)(e)", "a\nabcdef", re.M, ("b", "c", "d", "e")),
    ("(b)(c)(d)(e)(f)", "abcdef", 0, ("b", "c", "d", "e")),
    ("(b)(c)(d)(typo)", "abcdef", 0, ("", "", "", "")),
])
def test__find4(pattern: str, string: str, flags: int, expected: Any):
    """vre.find4()."""
    if isinstance(expected, tuple):
        actual = vre.find4(pattern=pattern, string=string, flags=flags)
        assert actual == expected
    else:
        with pytest.raises(expected):
            vre.find4(pattern=pattern, string=string, flags=flags)


@pytest.mark.parametrize("pattern, string, flags, expected", [
    ("", "a12b", 0, 0),
    ("typo", "a12b", 0, 0),
    ("(typo)", "a12b", 0, 0),
    (r"(\d+)", "ab", 0, 0),
    (r"(\d+)", "a12b", 0, 12),
    (r"a(\d+)b(\d+)c", "a1b2c", 0, 1),
    ("(2)", "a1b\n2c", re.M, 2),
])
def test__find1i(pattern: str, string: str, flags: int, expected: int):
    """vre.find1i()."""
    actual = vre.find1i(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, expected", [
    ("", "a12b34c", 0, (0, 0)),
    ("typo", "a12b34c", 0, (0, 0)),
    (r"(\d+)", "a12b34c", 0, (0, 0)),
    (r"(\d+)b(typo)", "a12b34c", 0, (0, 0)),
    (r"(typo)b(\d+)", "a12b34c", 0, (0, 0)),
    (r"(\d+)b(\d+)", "a12b34c", 0, (12, 34)),
    (r"(\d+)b(\d+)c(\d+)", "a12b34c56d", 0, (12, 34)),
])
def test__find2i(pattern: str, string: str, flags: int, expected: int):
    """vre.find2i()."""
    actual = vre.find2i(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("patterns, string, flags, expected", [
    ([], "abcdef", 0, ""),
    (["typo"], "abcdef", 0, ""),
    (["(typo)"], "abcdef", 0, ""),
    (["(b)"], "abcdef", 0, "b"),
    (["(b)"], "a\nabcdef", re.M, "b"),
    (["(bc)"], "abcdef", 0, "bc"),
    (["(b)(c)"], "abcdef", 0, "b"),
    (["(c)", "(b)"], "abcdef", 0, "c"),
    (["(typo)", "(b)"], "abcdef", 0, "b"),
    ("", "abcdef", 0, TypeError),
])
def test__find1s(patterns, string, flags, expected):
    """vre.find1s()."""
    if isinstance(expected, str):
        actual = vre.find1s(patterns=patterns, string=string, flags=flags)
        assert actual == expected
    else:
        with pytest.raises(expected):
            vre.find1s(patterns=patterns, string=string, flags=flags)


@pytest.mark.parametrize("string, expected", [
    ("", ""),
    ("10.0.0.", ""),
    ("10.0.0.1/32", "10.0.0.1"),
    ("a10.0.0.1/24b10.0.0.2/24c", "10.0.0.1"),
])
def test_valid__find_ip(string: str, expected: str):
    """vre.find_ip()"""
    actual = vre.find_ip(string=string)
    assert actual == expected


@pytest.mark.parametrize("string, expected", [
    ("", ""),
    ("10.0.0.1_24", ""),
    ("10.0.0.1/24", "10.0.0.1/24"),
    ("a10.0.0.1/24b10.0.0.2/24c", "10.0.0.1/24"),
])
def test_valid__find_prefix(string: str, expected: str):
    """vre.find_prefix()"""
    actual = vre.find_prefix(string=string)
    assert actual == expected
