"""Helpers for dictionary processing."""

from typing import Any


def pop_d(key: Any, data: dict) -> Any:
    """Pop the specified item from the data by key.

    If key is absent in data, do nothing and return None.

    :param key: The key to be popped from the data.
    :param data: The data from which the key is to be popped.
    :return: The popped item if key is present in data, otherwise None.
    :example:
        pop_d(key=1, data={1: 2}) -> 2
        pop_d(key=2, data={1: 2}) -> None
    """
    if key in data:
        return data.pop(key)
    return None
