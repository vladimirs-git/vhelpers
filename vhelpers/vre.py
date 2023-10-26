"""Helpers for regex processing."""

import re

from vhelpers import vint
from vhelpers.types_ import T2Str, T3Str, T4Str, T2Int, SeqStr


def find1(pattern: str, string: str, flags: int = 0) -> str:
    """Parse 1 item using findall.

    1 group with parentheses in pattern is required.
    If nothing is found, return 1 empty string.

    :param pattern: The regular expression pattern to search for.
    :param string: The string to search within.
    :param flags: Optional flags to modify the behavior of the search.
    :return: The interested substring, or an empty string if nothing is found.
    :example:
        find1(pattern="a(b)cde", string="abcde") -> "b"
    """
    empty = ""
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [empty])[0]
    if isinstance(result, str):
        return result
    if isinstance(result, tuple):
        return result[0]
    return empty


def find2(pattern: str, string: str, flags: int = 0) -> T2Str:
    """Parse 2 items using findall.

    2 groups with parentheses in pattern is required.
    If nothing is found, return 2 empty strings.

    :param pattern: The regular expression pattern.
    :param string: The string to search within.
    :param flags: Optional flags to modify the behavior of the search.
    :return: A tuple with two interested substrings, or empty strings if nothing is found.
    :example:
        find2(pattern="a(b)(c)de", string="abcde") -> ("b", "c")
    """
    empty = ("", "")
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [empty])[0]
    if isinstance(result, tuple) and len(result) >= 2:
        return result[0], result[1]
    return empty


def find3(pattern: str, string: str, flags: int = 0) -> T3Str:
    """Parse 3 items using findall.

    3 groups with parentheses in pattern is required.
    If nothing is found, returns 3 empty strings.

    :param pattern: The regular expression pattern.
    :param string: The string to search within.
    :param flags: Optional flags to modify the behavior of the search.
    :return: A tuple with three interested substrings, or empty strings if nothing is found.
    :example:
        find3(pattern="a(b)(c)(d)e", string="abcde") -> ("b", "c", "d")
    """
    empty = ("", "", "")
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [empty])[0]
    if isinstance(result, tuple) and len(result) >= 3:
        return result[0], result[1], result[2]
    return empty


def find4(pattern: str, string: str, flags: int = 0) -> T4Str:
    """Parse 4 items using findall.

    4 groups with parentheses in pattern is required.
    If nothing is found, return 4 empty strings.

    :param pattern: The regular expression pattern.
    :param string: The string to search within.
    :param flags: Optional flags to modify the behavior of the search.
    :return: A tuple with three interested substrings, or empty strings if nothing is found.
    :example:
        find4(pattern="a(b)(c)(d)(e)", string="abcde") -> ("b", "c", "d", "e")
    """
    empty = ("", "", "", "")
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [empty])[0]
    if isinstance(result, tuple) and len(result) >= 4:
        return result[0], result[1], result[2], result[3]
    return empty


def find1i(pattern: str, string: str, flags: int = 0) -> int:
    """Parse 1 digit using findall.

    1 group with parentheses in pattern is required.
    If nothing is found, return 0.

    :param pattern: The regular expression pattern to search for.
    :param string: The string to search within.
    :param flags: Optional flags to modify the behavior of the search.
    :return: The interested integer, or 0 if nothing is found.
    :example:
        find1i(pattern="a([0-9]+)b", string="a123b") -> 123
    """
    result = find1(pattern=pattern, string=string, flags=flags)
    return int(result) if result else 0


def find2i(pattern: str, string: str, flags: int = 0) -> T2Int:
    """Parse 2 digits using findall.

    2 groups with parentheses in pattern is required.
    If nothing is found, return tuple of 0.

    :param pattern: The regular expression pattern to search for.
    :param string: The string to search within.
    :param flags: Optional flags to modify the behavior of the search.
    :return: The interested integers, or tuple of 0 if nothing is found.
    :example:
        find2i(pattern="a([0-9])b([0-9])c", string="a1b2c") -> (1, 2)
    """
    result = find2(pattern=pattern, string=string, flags=flags)
    if isinstance(result, tuple) and len(result) >= 2:
        return vint.to_int(result[0]), vint.to_int(result[1])
    return 0, 0


def find1s(patterns: SeqStr, string: str, flags: int = 0) -> str:
    """Parse 1st item that match one of regex in patterns.

    1 group with parentheses in pattern is required.
    If nothing is found, return 1 empty string.

    :param patterns: The list of regular expression patterns to search for.
    :param string: The string to search within.
    :param flags: Optional flags to modify the behavior of the search.
    :return: The interested substring, or an empty string if nothing is found.
    :example:
        find1s(patterns=["a(a)cde", "a(b)cde"], string="abcde") -> "b"
    """
    if not isinstance(patterns, (list, set, tuple)):
        raise TypeError(f"{list} expected")
    for pattern in patterns:
        if result := find1(pattern, string, flags):
            return result
    return ""
