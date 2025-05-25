"""Helpers for dictionary processing."""
import hashlib
import json
from pathlib import Path
from typing import Any, Type

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
    data_ = data.copy()
    if include:
        data_ = {k: v for k, v in data_.items() if k in include}
    if exclude:
        data_ = {k: v for k, v in data_.items() if k not in exclude}
    return data_


def for_json(data: dict) -> dict:
    """Convert the input data to a format suitable for JSON serialization.

    Replace set with list.

    :param data: Input data to be converted.
    :return: Data converted to a format suitable for JSON serialization.
    :raises TypeError: If input data is not a dictionary.

    :example:
        for_json(data={1: {2, 3}}) -> {1: [2, 3]}
    """
    if not isinstance(data, dict):
        raise TypeError(f"Invalid {type(data)}, expected dict")
    return _for_json(data)


def _for_json(data: Any) -> Any:
    """Convert the input data to a format suitable for JSON serialization.

    Replace set with list.

    :param data: Input data to be converted.
    :return: Data converted to a format suitable for JSON serialization.
    """
    if isinstance(data, set):
        return list(data)  # Convert set to list
    if isinstance(data, dict):
        return {key: _for_json(value) for key, value in data.items()}
    if isinstance(data, list):
        return [_for_json(item) for item in data]
    return data


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


def remove_empty(data: dict) -> dict:
    """Remove empty values from a multidimensional dictionary recursively.

    :param data: Dictionary with empty values.
    :return: Dictionary without empty values.

    :example:
        remove_empty(data={1: 1, 2: 0}) -> {1: 1}
    """
    if isinstance(data, dict):
        return {k: remove_empty(v) for k, v in data.items() if v and remove_empty(v) != {}}
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


# ============================ get typed =============================

def get_any(*args) -> Any:
    """Retrieve a nested value from a dictionary using a sequence of keys.

    :param args: Arguments where the first is the dictionary and the rest are keys
        used to retrieve the desired nested value.
    :return: Value corresponding to the sequence of keys, or None if any key
             is not found or if the access fails.

    :example:
        get_any({"a": {"b": "B"}}, "a", "b") -> "B"
        get_any({"a": {"b": "B"}}, "a", "c") -> None
    """
    try:
        return _get_keys(*args, type_=type(None))
    except (KeyError, IndexError, TypeError):
        return None


def get_bool(*args) -> bool:
    """Retrieve a nested boolean value from a dictionary using a sequence of keys.

    :param args: Arguments where the first is the dictionary and the rest are keys
        used to retrieve the desired nested value.
    :return: Boolean value corresponding to the sequence of keys, or False if any key
             is not found or if the access fails.

    :example:
        get_bool({"a": {"b": True}}, "a", "b") -> True
        get_bool({"a": {"b": "B"}}, "a", "b") -> False
    """
    return _get_keys(*args, type_=bool)


def get_dict(*args) -> dict:
    """Retrieve a nested dictionary value from a dictionary using a sequence of keys.

    :param args: Arguments where the first is the dictionary and the rest are keys
        used to retrieve the desired nested value.
    :return: Dictionary value corresponding to the sequence of keys, or empty dictionary if any key
             is not found or if the access fails.

    :example:
        get_dict({"a": {"b": {"c": "C"}}}, "a", "b") -> {"c": "C"}
        get_dict({"a": {"b": "B"}}, "a", "b") -> {}
    """
    return _get_keys(*args, type_=dict)


def get_int(*args) -> int:
    """Retrieve a nested integer value from a dictionary using a sequence of keys.

    :param args: Arguments where the first is the dictionary and the rest are keys
        used to retrieve the desired nested value.
    :return: Integer value corresponding to the sequence of keys, or 0 if any key
             is not found or if the access fails.

    :example:
        get_int({"a": {"b": "1"}}, "a", "b") -> 1
        get_int({"a": {"b": "B"}}, "a", "b") -> 0
    """
    data, *keys = args
    try:
        for key in keys:
            data = data[key]
    except (KeyError, TypeError):
        return 0

    if isinstance(data, int):
        return data

    if isinstance(data, str) and data.isdigit():
        return int(data)

    return 0


def get_list(*args) -> list:
    """Retrieve a nested list value from a dictionary using a sequence of keys.

    :param args: Arguments where the first is the dictionary and the rest are keys
        used to retrieve the desired nested value.
    :return: List value corresponding to the sequence of keys, or empty list if any key
             is not found or if the access fails.

    :example:
        get_list({"a": {"b": ["B"]}}, "a", "b") -> ["B"]
        get_list({"a": {"b": "B"}}, "a", "b") -> []
    """
    return _get_keys(*args, type_=list)


def get_str(*args) -> str:
    """Retrieve a nested string value from a dictionary using a sequence of keys.

    :param args: Arguments where the first is the dictionary and the rest are keys
        used to retrieve the desired nested value.
    :return: String value corresponding to the sequence of keys, or empty string if any key
             is not found or if the access fails.

    :example:
        get_str({"a": {"b": "B"}}, "a", "b") -> "B"
        get_str({"a": {"b": 1}}, "a", "b") -> ""
    """
    return _get_keys(*args, type_=str)


def _get_keys(*args, type_: Type) -> Any:
    """Retrieve values from data using keys and check their data types.

    :param keys: Chaining dictionary keys to retrieve the desired value.
    :param type_: Data type.
    :param data: Dictionary.

    :return: Value with proper data type.
    """
    data, *keys = args
    try:
        for key in keys:
            data = data[key]  # type: ignore
    except (KeyError, IndexError, TypeError):
        return type_()

    if type_ is type(None):
        return data
    if not isinstance(data, type_):
        return type_()

    return data
