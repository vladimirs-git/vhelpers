"""Unittests vre.py."""
import re

import pytest

from vhelpers import vre

FIND1 = [
    ("", "abcdef", 0, ""),
    ("typo", "abcdef", 0, ""),
    ("(typo)", "abcdef", 0, ""),
    ("(b)", "abcdef", 0, "b"),
    ("(b)", "a\nabcdef", re.M, "b"),
    ("(bc)", "abcdef", 0, "bc"),
    ("(b)(c)", "abcdef", 0, "b"),
]
FIND2 = [
    ("", "abcdef", 0, ("", "")),
    ("typo", "abcdef", 0, ("", "")),
    ("(typo)", "abcdef", 0, ("", "")),
    ("(b)", "abcdef", 0, ("", "")),
    ("(b)(typo)", "abcdef", 0, ("", "")),
    ("(typo)(c)", "abcdef", 0, ("", "")),
    ("(b)(c)", "abcdef", 0, ("b", "c")),
    ("(b)(c)", "a\nabcdef", re.M, ("b", "c")),
    ("(b)(c)(d)", "abcdef", 0, ("b", "c")),
]
FIND3 = [
    ("", "abcdef", 0, ("", "", "")),
    ("(b)", "abcdef", 0, ("", "", "")),
    ("(b)(c)", "abcdef", 0, ("", "", "")),
    ("(b)(c)(d)", "abcdef", 0, ("b", "c", "d")),
    ("(b)(c)(d)", "a\nabcdef", re.M, ("b", "c", "d")),
    ("(b)(c)(d)(e)", "abcdef", 0, ("b", "c", "d")),
    ("(b)(c)(typo)", "abcdef", 0, ("", "", "")),
]
FIND4 = [
    ("", "abcdef", 0, ("", "", "", "")),
    ("(b)", "abcdef", 0, ("", "", "", "")),
    ("(b)(c)", "abcdef", 0, ("", "", "", "")),
    ("(b)(c)(d)", "abcdef", 0, ("", "", "", "")),
    ("(b)(c)(d)(e)", "abcdef", 0, ("b", "c", "d", "e")),
    ("(b)(c)(d)(e)", "a\nabcdef", re.M, ("b", "c", "d", "e")),
    ("(b)(c)(d)(e)(f)", "abcdef", 0, ("b", "c", "d", "e")),
    ("(b)(c)(d)(typo)", "abcdef", 0, ("", "", "", "")),
]
ERRORS = [
    (1, "abcdef", 0, TypeError),
    ("", 1, 0, TypeError),
]


@pytest.mark.parametrize("pattern, string, flags, expected", FIND1)
def test_find1(pattern, string, flags, expected):
    """find1."""
    actual = vre.find1(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, error", ERRORS)
def test_find1__invalid(pattern, string, flags, error):
    """find1."""
    with pytest.raises(error):
        vre.find1(pattern=pattern, string=string, flags=flags)


@pytest.mark.parametrize("pattern, string, flags, expected", FIND2)
def test_find2(pattern, string, flags, expected):
    """find2."""
    actual = vre.find2(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, error", ERRORS)
def test_find2__invalid(pattern, string, flags, error):
    """find2."""
    with pytest.raises(error):
        vre.find2(pattern=pattern, string=string, flags=flags)


@pytest.mark.parametrize("pattern, string, flags, expected", FIND3)
def test_find3(pattern, string, flags, expected):
    """find3."""
    actual = vre.find3(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, error", ERRORS)
def test_find3__invalid(pattern, string, flags, error):
    """find3."""
    with pytest.raises(error):
        vre.find3(pattern=pattern, string=string, flags=flags)


@pytest.mark.parametrize("pattern, string, flags, expected", FIND4)
def test_find4(pattern, string, flags, expected):
    """find4."""
    actual = vre.find4(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, error", ERRORS)
def test_find4__invalid(pattern, string, flags, error):
    """find4."""
    with pytest.raises(error):
        vre.find4(pattern=pattern, string=string, flags=flags)
