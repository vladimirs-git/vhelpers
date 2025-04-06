"""Helpers for int processing."""

from vhelpers.types_ import IntStr


def to_int(digit: IntStr) -> int:
    """Convert string digit to integer.

    :param digit: Digit, string ot integer.
    :return: Integer or 0 if value is not digit.

    :example:
        to_int(digit="1") -> 1
        to_int(digit="a") -> 0
    """
    if isinstance(digit, int):
        return digit
    digit = digit.strip()
    if not digit.isdigit():
        return 0
    return int(digit)


def to_ordinal(digit: IntStr) -> str:
    """Convert an integer or numeric string to its ordinal representation.

    :param digit: An integer or a string that can be converted to an integer.
    :return: The ordinal string representation of the number.

    :example:
        to_ordinal(digit=1) -> "1st"
        to_ordinal(digit=2) -> "2nd"
        to_ordinal(digit=21) -> "21st"
    """
    int_ = to_int(digit)
    abs_int = abs(int_)

    if int_ == 0:
        return "0th"

    if 10 <= abs_int % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(abs_int % 10, "th")

    return f"{int_}{suffix}"
