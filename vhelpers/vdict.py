"""Helpers for dictionary processing."""
import hashlib
import json
from pathlib import Path
from typing import Any

import tomli

from vhelpers.types_ import UPath, DAny, OLAny


def filter_keys(data: dict, include: OLAny = None, exclude: OLAny = None) -> dict:
    """Filter the data to only required keys by include/exclude parameters.

    :param data: Dictionary to be filtered.
    :param include: Keys that should be present in the filtered dictionary.
    :param exclude: Keys that should not be present in the filtered dictionary.
    :return: New dictionary containing only the required keys.

    :example:
        filter_keys(data={"a": "A", "b": "B"}, include=["a"]) -> {"a": "A"}
        filter_keys(data={"a": "A", "b": "B"}, exclude=["a"]) -> {"b": "B"}
    """
    data_: dict = {k: v for k, v in data.items()}
    if include:
        data_ = {k: v for k, v in data_.items() if k in include}
    if exclude:
        data_ = {k: v for k, v in data_.items() if k not in exclude}
    return data_


def invert(data: dict) -> dict:
    """Invert keys and values.

    :param data: Dictionary to invert.
    :return: Dictionary with keys and values inverted.
    :example:
        invert(data={1: 2}) -> {2: 1}
    """
    return {v: k for k, v in data.items()}


def md5hash(data: DAny) -> str:
    """Create MD5 hash of a dictionary.

    :param data: Dictionary to be hashed.
    :return: String representing the MD5 hash of the dictionary.
    """
    dhash = hashlib.md5()
    encoded = json.dumps(data, sort_keys=True).encode()
    dhash.update(encoded)
    return dhash.hexdigest()


def pop(data: dict, key: Any) -> Any:
    """Pop the specified item from the data by key.

    If key is absent in data, do nothing and return None.

    :param data: The dictionary from which the key is to be popped.
    :param key: The key to be popped from the data.
    :return: The popped item if key is present in data, otherwise None.

    :example:
        pop(data={1: 2}, key=1) -> 2
        pop(data={1: 2}, key=3) -> None
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


def sha256hash(data: dict) -> int:
    """Create SHA-256 hash of a dictionary.

    :param data: Dictionary to be hashed.
    :return: Integer representing the SHA-256 hash of the dictionary.
    """
    items = tuple(sorted(data.items()))
    json_string = json.dumps(items)
    json_bytes = json_string.encode("utf-8")
    hash_object = hashlib.sha256()
    hash_object.update(json_bytes)
    return int(hash_object.hexdigest(), 16)
