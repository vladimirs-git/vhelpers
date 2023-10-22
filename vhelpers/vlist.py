"""Helpers for list processing."""

from typing import Any

from vhelpers.types_ import SeqT, LT, TList


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
