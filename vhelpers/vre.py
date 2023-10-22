"""Helpers for regex processing."""

import re

from vhelpers.types_ import T2Str, T3Str, T4Str


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
