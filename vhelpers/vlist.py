"""Helpers for list processing."""

import math
import re
from string import punctuation
from typing import Any, Generator, Sequence

from vhelpers import vstr
from vhelpers.types_ import SeqTy, ListTy, TList, LStr, LAny, LLAny, LListTy


def cmd_value(key: str, cmds: LStr) -> str:
    """Find value in list of commands by required key.

    :param key: Key of required command.
    :param cmds: Commands where need to find value.
    :return: Value if key is found, empty string otherwise.

    :example:
        cmd_value("description", ["description VALUE"]) -> "VALUE"
    """
    value = ""
    for cmd in cmds:
        value = vstr.cmd_value(key, cmd)
        if value:
            break
    return value


def dupl(items: SeqTy) -> ListTy:
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


def is_in(items1: list, items2: list) -> bool:
    """Check if any item in items1 is present in items2.

    :param items1: A list of items.
    :param items2: A list of items.
    :return: True if any item in items1 is present in items2, False otherwise.

    :example:
        is_in(items1=[1, 2], items2=[2, 3]) is True
        is_in(items1=[1, 2], items2=[2, 3]) is True
    """
    for items in items1:
        if items in items2:
            return True
    return False


def no_dupl(items: SeqTy) -> ListTy:
    """Remove duplicates from a list of items.

    :param items: A list of items.
    :return: A list of items without duplicates.

    :example:
        no_dupl([1, 2, 1]) -> [1, 2]
    """
    items_: ListTy = []
    for item in items:
        if item not in items_:
            items_.append(item)
    return items_


def replace(items: list, old: Any, new: Any) -> None:
    """Replace one item with another.

    :param items: The list of items where need replace item.
    :param old: The item to be replaced.
    :param new: The item to replace with.
    :return: None. Update items.

    :example:
        items = [1, 2, 3]
        replace(items=items, old=2, new=4)
        assert items == [1, 4, 3]
    """
    if old in items:
        idx = items.index(old)
        items[idx] = new


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
    punctuation_ = rf"[\s{punctuation_}]+"
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
        to_list((1, 2)) -> [1, 2]
        to_list(1) -> [1]
        to_list(None) -> []
    """
    if items is None:
        return []
    if not isinstance(items, TList):
        return [items]
    return list(items)


def to_lists(items: SeqTy, count: int) -> LListTy:
    """Convert a flat list into a multidimensional list with a fixed number of inner lists.

    :param items: The flat list to convert.
    :param count: The number of inner lists.
    :return: A multidimensional list.

    :example:
        to_lists(items=[1, 2, 3, 4, 5], count=2) -> [[1, 2, 3], [4, 5]]
    """
    count_ = int(count)
    if count_ <= 0:
        return []

    length = int(math.ceil(len(items) / count_))

    items_ = []
    items = list(items)
    while items:
        piece = items[:length]
        items_.append(piece)
        items = items[length:]

    if diff := count - len(items_):
        empty_items: ListTy = [[] for _ in range(diff)]
        items_.extend(empty_items)

    return items_


def to_lstr(items: Any) -> LStr:
    """Convert the input items from any into a list of string.

    If items is a list, set or tuple, simply change its type to list.
    If items is None or empty string return an empty list.

    :param items: The items to be converted into a list of string.
    :return: The converted list.

    :example:
        to_lstr([1, "2"]) -> ["1", "2"]
        to_lstr(1) -> ["1"]
        to_lstr("") -> []
    """
    if items in [None, ""]:
        return []
    if not isinstance(items, TList):
        return [str(items)]
    return [str(i) for i in items]


def to_multi(items: LAny, count: int) -> LLAny:
    """Convert a flat list into a multidimensional list.

    Convert a list with the specified number of items in each inner list.

    :param items: The flat list to convert.
    :param count: The number of items to include in each inner list.
    :return: A multidimensional list with the specified number of items in each inner list.

    :example:
        to_multi(items=[1, 2, 3, 4, 5], count=2) -> [[1, 2], [3, 4], [5]]
    """
    items_ = []
    for i in range(0, len(items), count):
        items_.append(items[i : i + count])
    return items_
