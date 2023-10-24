"""Helpers for dictionary processing."""
from pathlib import Path
from typing import Any

import tomli

from vhelpers.types_ import UPath, DAny


def pop(key: Any, data: dict) -> Any:
    """Pop the specified item from the data by key.

    If key is absent in data, do nothing and return None.

    :param key: The key to be popped from the data.
    :param data: The data from which the key is to be popped.
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
