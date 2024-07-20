"""Helpers for dictionary processing."""
import hashlib
import json
from pathlib import Path
from typing import Any

import tomli

from vhelpers.types_ import UPath, DAny


def filter_keys(data: dict, keys: list) -> dict:
    """Filters the data to only include the specified required keys.

    :param data: The original dictionary to filter.
    :param keys: A list of keys that should be present in the filtered dictionary.
    :return: A new dictionary containing only the required keys.

    :example:
        filter_keys(data={"a": "A", "b": "B"}, keys=["a"]) -> {"a": "A"}
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
