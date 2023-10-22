"""Parameterized data for str_.py."""
import re

FINDALL1 = [
    ("", "abcdef", 0, ""),
    ("typo", "abcdef", 0, ""),
    ("(typo)", "abcdef", 0, ""),
    ("(b)", "abcdef", 0, "b"),
    ("(b)", "a\nabcdef", re.M, "b"),
    ("(bc)", "abcdef", 0, "bc"),
    ("(b)(c)", "abcdef", 0, "b"),
]

FINDALL_ERR = [
    (1, "abcdef", 0, TypeError),
    ("", 1, 0, TypeError),
]

FINDALL2 = [
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

FINDALL3 = [
    ("", "abcdef", 0, ("", "", "")),
    ("(b)", "abcdef", 0, ("", "", "")),
    ("(b)(c)", "abcdef", 0, ("", "", "")),
    ("(b)(c)(d)", "abcdef", 0, ("b", "c", "d")),
    ("(b)(c)(d)", "a\nabcdef", re.M, ("b", "c", "d")),
    ("(b)(c)(d)(e)", "abcdef", 0, ("b", "c", "d")),
    ("(b)(c)(typo)", "abcdef", 0, ("", "", "")),
]

FINDALL4 = [
    ("", "abcdef", 0, ("", "", "", "")),
    ("(b)", "abcdef", 0, ("", "", "", "")),
    ("(b)(c)", "abcdef", 0, ("", "", "", "")),
    ("(b)(c)(d)", "abcdef", 0, ("", "", "", "")),
    ("(b)(c)(d)(e)", "abcdef", 0, ("b", "c", "d", "e")),
    ("(b)(c)(d)(e)", "a\nabcdef", re.M, ("b", "c", "d", "e")),
    ("(b)(c)(d)(e)(f)", "abcdef", 0, ("b", "c", "d", "e")),
    ("(b)(c)(d)(typo)", "abcdef", 0, ("", "", "", "")),
]
