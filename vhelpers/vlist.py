"""Helpers for list processing."""

import re
from string import punctuation
from typing import Any, Generator, Sequence

from vhelpers.types_ import SeqT, LT, TList, LStr, LAny, LLAny


def dupl(items: SeqT) -> LT:
    """Find duplicates of the items.

    :param items: A list of items where need to find duplicates.
    :return: A list of items with duplicates.
    :example:
        dupl([1, 2, 1]) -> [1]
        dupl([{1}, {2}, {1}]) -> [{1}]
    """
    types = set()
    is_hash_error = False
    seen = set()
    duplicates_hashable = set()
    duplicates = []

    for item in items:
        types.add(type(item))

        if isinstance(item, (int, str)):
            hashable: Any = item
        elif isinstance(item, dict):
            hashable = tuple(item.items())
        elif isinstance(item, set):
            hashable = frozenset(item)
        else:
            try:
                hashable = hash(item)
            except TypeError:
                is_hash_error = True
                hashable = str(item)

        if hashable in seen:
            duplicates_hashable.add(hashable)
            if item not in duplicates:
                duplicates.append(item)
        seen.add(hashable)

    if is_hash_error and len(types) > 1:
        raise TypeError(f"{types=} expected only one.")

    return duplicates


def flatten(items: Sequence) -> list:
    """Convert a multidimensional list to a flattened list.

    :param items: The list to be flattened.
    :return: Flat list.
    :example:
        flatten([1, [2, [3]], 4, [5, [6]]]) -> [1, 2, 3, 4, 5, 6]
    """
    return list(_flatten(items))


def _flatten(items: Sequence, ignore_types=(str, bytes)) -> Generator:
    """Convert a multidimensional list to a flattened generator.

    :param items: The list to be flattened.
    :param ignore_types: Types to be ignored during flattening, defaults to (str, bytes)
    :return: A generator that yields the flattened list.
    """
    for item in items:
        if isinstance(item, Sequence) and not isinstance(item, ignore_types):
            yield from _flatten(item)
        else:
            yield item


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
    punctuation_ = fr"[\s{punctuation_}]+"
    items: LStr = re.split(punctuation_, text)
    items = [s for s in items if s]
    return items


def to_list(items: Any) -> list:
    """Convert the input items from any into a list.

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


def to_multi(items: LAny, count: int) -> LLAny:
    """Convert a flat list into a multidimensional list.

    Convert a list with the specified number of items in each inner list.

    :param items: The flat list to convert.
    :param count: The number of items to include in each inner list.
    :return: A multidimensional list with the specified number of items in each inner list.
    :example:
        to_multi(items=[1, 2, 3, 4, 5], count=2) -> [[1, 2], [3, 4], [5]]
    """
    output_items = []
    for i in range(0, len(items), count):
        output_items.append(items[i:i + count])
    return output_items
