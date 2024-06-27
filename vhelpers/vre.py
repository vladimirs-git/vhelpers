"""Helpers for regex processing."""

import re

from vhelpers import helpers as h
from vhelpers import vint
from vhelpers.types_ import T2Str, T3Str, T4Str, T2Int, SeqStr, UStr


def cmd_value(key: str, config: UStr, flags: int = 0) -> str:
    """Find value in list of commands by required key.

    :param key: Key of required command.
    :param config: Config commands where need to find value.
        :param flags: Optional flags to modify the behavior of the search.
    :return: Value if key is found, empty string otherwise.

    :example:
        cmd_value(".+description ", [" description VALUE"]) -> "VALUE"
    """
    value = ""
    pattern = f"{key}(.+)"
    cmds = h.init_cmds(config)
    for cmd in cmds:
        if value := find1(pattern, cmd, flags):
            break
    return value


def between(
    text: str,
    start: str,
    end: str,
    w_start: bool = False,
    w_end: bool = False,
    strict: bool = False,
) -> str:
    r"""Find all substrings between the start and end regexes.

    :param text: Text where need to find start and end.
    :param start: Regex of start.
    :param end: Regex of end.
    :param w_start: True  - Returns text with matched start text,
                    False - (default) Returns text without matched start text.
    :param w_end: True  - Returns text with matched end text,
                  False - (default) Returns text without matched end text.
    :param strict: True  - Raises ValueError if absent start or end,
                   False - Returns empty string if absent start or end.
    :return: Text between start and end.

    :example:
        between(text="a1\nb2\nc3\nd4", start="b2", end="c3", w_start=True, w_end=True) -> "b2\nc3"
    """
    match_start = re.search(start, text, re.M)
    if not match_start:
        if strict:
            raise ValueError("absent header in text")
        return ""
    header_start = match_start[0]
    idx = match_start.end()
    result_wo_start = text[idx:]

    match_end = re.search(end, result_wo_start, re.M)
    if not match_end:
        if strict:
            raise ValueError("absent footer in text")
        return ""
    header_end = match_end[0]
    idx1 = match_end.start()
    result_wo_end = result_wo_start[:idx1]

    results = [
        header_start if w_start else "",
        result_wo_end,
        header_end if w_end else "",
    ]
    result = "".join(results)
    return result


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


def ip(string: str) -> str:
    """Parse 1st IP address from string. If nothing is found, returns an empty string.

    :param string: String where need to find IP address.
    :return: IP address.

    :example:
        ip("text 10.0.0.1/24 10.0.0.2/24 text") -> "10.0.0.1"
    """
    return find1(pattern=r"\d+\.\d+\.\d+\.\d+", string=string)


def prefix(string: str) -> str:
    """Parse 1st prefix from string. If nothing is found, returns an empty string.

    :param string: String where need to find prefix.
    :return: Prefix.

    :example:
        prefix("text 10.0.0.1/24 10.0.0.2/24 text") -> "10.0.0.1/24"
    """
    return find1(pattern=r"\d+\.\d+\.\d+\.\d+/\d+", string=string)
