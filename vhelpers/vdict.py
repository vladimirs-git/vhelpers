"""Helpers for dictionary processing."""
from pathlib import Path
from typing import Any

import tomli

from vhelpers.types_ import UPath, DAny


def filter_keys(keys: list, data: dict) -> dict:
    """Filters the data to only include the specified required keys.

    :param keys: A list of keys that should be present in the filtered dictionary.
    :param data: The original dictionary to filter.
    :return: A new dictionary containing only the required keys.

    :example:
        filter_keys(keys=["a"], data={"a": "A", "b": "B"}) -> {"a": "A"}
    """
    return {key: data[key] for key in keys if key in data}


def invert(data: dict) -> dict:
    """Invert keys and values.

    :param data: Dictionary to invert.
    :return: Dictionary with keys and values inverted.
    :example:
        invert(data={1: 2}) -> {2: 1}
    """
    return {v: k for k, v in data.items()}


# def dld(key: Any, items: List[dict]) -> dict:
#     """Create a multidimensional dictionary from a list of dictionaries based on a specified key.
#
#     :param key: The key to use for grouping the dictionaries.
#     :param items: A list of dictionaries to be grouped.
#     :return: Grouped dictionary of list of dictionaries.
#     """
#     data_dld = {}
#     for data in items:
#         data_dld.setdefault(data[key], []).append(data)
#     return data_dld
#
#
# def dlo(key: Any, items: list) -> dict:
#     """Create a multidimensional dictionary from a list of objects based on a specified attribute.
#
#     :param key: Attribute to use for grouping the dictionaries.
#     :param items: A list of objects to be grouped.
#     :return: Grouped dictionary of lists of objects.
#     """
#     data_dlo = {}
#     for obj in items:
#         data_dlo.setdefault(getattr(obj, key), []).append(obj)
#     return data_dlo


def pop(key: Any, data: dict) -> Any:
    """Pop the specified item from the data by key.

    If key is absent in data, do nothing and return None.

    :param key: The `key` to be popped from the `data`.
    :param data: The dictionary from which the key is to be popped.
    :return: The popped item if key is present in data, otherwise None.

    :example:
        pop(key=1, data={1: 2}) -> 2
        pop(key=3, data={1: 2}) -> None
    """
    if key in data:
        return data.pop(key)
    return None


def pyproject_d(root: UPath) -> DAny:
    """Convert pyproject.toml to a dictionary.

    :param root: The root directory or path to the pyproject.toml file.
    :return: A dictionary containing the data from pyproject.toml.
    """
    if isinstance(root, str):
        root = Path(root)
    path = Path.joinpath(root, "pyproject.toml")
    with path.open(mode="rb") as file_:
        data = tomli.load(file_)
    return data
