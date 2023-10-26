"""Helpers for int processing."""

from vhelpers.types_ import IntStr


def to_int(digit: IntStr) -> int:
    """Convert string digit to integer.

    :param digit: Digit, string ot integer.
    :return: Integer or 0 if value is not digit.
    :example:
        int_(digit="1") -> 1
        int_(digit="a") -> 0
    """
    if isinstance(digit, int):
        return digit
    digit = digit.strip()
    if not digit.isdigit():
        return 0
    return int(digit)
