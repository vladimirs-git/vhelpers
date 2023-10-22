"""Helpers for list processing."""

from typing import Any

from vhelpers.types_ import SeqT, LT, TList


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


def to_list(items: Any) -> list:
    """Convert the input items into a list.

    :param items: The items to be converted into a list.
    :return: The converted list.
    :example:
        lst((1, 2)) -> [1, 2]
        lst(None) -> []
        lst(1) -> [1]
    """
    if items is None:
        return []
    if not isinstance(items, TList):
        return [items]
    return list(items)
