"""Unittests vre.py."""
import re

import pytest

from vhelpers import vre


@pytest.mark.parametrize("pattern, string, flags, expected", [
    ("", "abcdef", 0, ""),
    ("typo", "abcdef", 0, ""),
    ("(typo)", "abcdef", 0, ""),
    ("(b)", "abcdef", 0, "b"),
    ("(b)", "a\nabcdef", re.M, "b"),
    ("(bc)", "abcdef", 0, "bc"),
    ("(b)(c)", "abcdef", 0, "b"),
])
def test__find1(pattern, string, flags, expected):
    """find1."""
    actual = vre.find1(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, error", [
    (1, "abcdef", 0, TypeError),
    ("", 1, 0, TypeError),
])
def test__find1__invalid(pattern, string, flags, error):
    """find1."""
    with pytest.raises(error):
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
])
def test__find2(pattern, string, flags, expected):
    """find2."""
    actual = vre.find2(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, error", [
    (1, "abcdef", 0, TypeError),
    ("", 1, 0, TypeError),
])
def test__find2__invalid(pattern, string, flags, error):
    """find2."""
    with pytest.raises(error):
        vre.find2(pattern=pattern, string=string, flags=flags)


@pytest.mark.parametrize("pattern, string, flags, expected", [
    ("", "abcdef", 0, ("", "", "")),
    ("(b)", "abcdef", 0, ("", "", "")),
    ("(b)(c)", "abcdef", 0, ("", "", "")),
    ("(b)(c)(d)", "abcdef", 0, ("b", "c", "d")),
    ("(b)(c)(d)", "a\nabcdef", re.M, ("b", "c", "d")),
    ("(b)(c)(d)(e)", "abcdef", 0, ("b", "c", "d")),
    ("(b)(c)(typo)", "abcdef", 0, ("", "", "")),
])
def test__find3(pattern, string, flags, expected):
    """find3."""
    actual = vre.find3(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, error", [
    (1, "abcdef", 0, TypeError),
    ("", 1, 0, TypeError),
])
def test__find3__invalid(pattern, string, flags, error):
    """find3."""
    with pytest.raises(error):
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
def test__find4(pattern, string, flags, expected):
    """find4."""
    actual = vre.find4(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, error", [
    (1, "abcdef", 0, TypeError),
    ("", 1, 0, TypeError),
])
def test__find4__invalid(pattern, string, flags, error):
    """find4."""
    with pytest.raises(error):
        vre.find4(pattern=pattern, string=string, flags=flags)
