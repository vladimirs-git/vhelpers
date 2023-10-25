"""Helpers for list processing."""

import re
from string import punctuation
from typing import Any

from vhelpers.types_ import SeqT, LT, TList, LStr


def from_any(items: Any) -> list:
    """Convert the input items into a list.

    If items is a list, set or tuple, simply change its type to list.
    Otherwise, create a list with the value as its first item.
    If items is None return an empty list.

    :param items: The items to be converted into a list.
    :return: The converted list.
    :example:
        lst((1, 2)) -> [1, 2]
        lst(1) -> [1]
        lst(None) -> []
    """
    if items is None:
        return []
    if not isinstance(items, TList):
        return [items]
    return list(items)


def no_dupl(items: SeqT) -> LT:
    """Remove duplicates from a list of items.

    :param items: A list of items.
    :return: A list of items without duplicates.
    :example:
        no_dupl([1, 2, 1]) -> [1, 2]
    """
    items_: LT = []
    for item in items:
        if item not in items_:
            items_.append(item)
    return items_


def split(text: str, chars: str = "", ignore: str = "") -> LStr:
    """Split string by punctuation chars.

    :param text: Text to split by punctuation.
    :param chars: Extra punctuation chars.
    :param ignore: Ignore punctuation chars.
    :return: Values without punctuation.
    :example:
        split(text="1; 2_3-4X5,6", chars="_X", ignore=",") -> ["1", "2", "3", "4", "5,6"]
    """
    punctuation_ = punctuation + chars
    for ignore_char in ignore:
        punctuation_ = punctuation_.replace(ignore_char, "")
    punctuation_ = punctuation_.replace("-", "\\-")
    punctuation_ = r"[\s{}]+".format(punctuation_)
    items: LStr = re.split(punctuation_, text)
    items = [s for s in items if s]
    return items
