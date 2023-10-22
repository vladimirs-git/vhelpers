"""Helpers for string processing."""

import re

from vhelpers.types_ import T2Str, T3Str, T4Str


def findall1(pattern: str, string: str, flags: int = 0) -> str:
    """Parse the first item of re.findall.

    Group with parentheses in pattern is required.
    If nothing is found, return 1 empty string.

    :param pattern: The regular expression pattern to search for.
    :param string: The string to search within.
    :param flags: Optional flags to modify the behavior of the search.
    :return: The interested substring, or an empty string if nothing is found.
    :example:
        findall1(pattern="a(b)cde", string="abcde") -> "b"
    """
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [""])[0]
    if isinstance(result, str):
        return result
    if isinstance(result, tuple):
        return result[0]
    return ""


def findall2(pattern: str, string: str, flags: int = 0) -> T2Str:
    """Parse 2 items of re.findall().

    Group with parentheses in pattern is required.
    If nothing is found, return 2 empty strings.

    :param pattern: The regular expression pattern.
    :param string: The string to search within.
    :param flags: Optional flags to modify the behavior of the search.
    :return: A tuple with two interested substrings, or empty strings if nothing is found.
    :example:
        findall2(pattern="a(b)(c)de", string="abcde") -> ("b", "c")
    """
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [("", "")])[0]
    if isinstance(result, tuple) and len(result) >= 2:
        return result[0], result[1]
    return "", ""


def findall3(pattern: str, string: str, flags: int = 0) -> T3Str:
    """Parse 3 items of re.findall().

    Group with parentheses in pattern is required.
    If nothing is found, returns 3 empty strings.

    :param pattern: The regular expression pattern.
    :param string: The string to search within.
    :param flags: Optional flags to modify the behavior of the search.
    :return: A tuple with three interested substrings, or empty strings if nothing is found.
    :example:
        findall3(pattern="a(b)(c)(d)e", string="abcde") -> ("b", "c", "d")
    """
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [("", "", "")])[0]
    if isinstance(result, tuple) and len(result) >= 3:
        return result[0], result[1], result[2]
    return "", "", ""


def findall4(pattern: str, string: str, flags: int = 0) -> tuple:
    """Parse 4 items of re.findall().

    Group with parentheses in pattern is required.
    If nothing is found, return 4 empty strings.

    :param pattern: The regular expression pattern.
    :param string: The string to search within.
    :param flags: Optional flags to modify the behavior of the search.
    :return: A tuple with three interested substrings, or empty strings if nothing is found.
    :example:
        findall4(pattern="a(b)(c)(d)(e)", string="abcde") -> ("b", "c", "d", "e")
    """
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [("", "", "")])[0]
    if isinstance(result, tuple) and len(result) >= 4:
        return result[0], result[1], result[2], result[3]
    return "", "", "", ""
