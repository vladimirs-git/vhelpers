"""Helpers for dictionary processing."""

from typing import Any

from vhelpers.types_ import DAny, LParam, TList, UParam


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


def dict_to_params(params_d: DAny) -> LParam:
    """Convert a dictionary to a list of tuples.
    
    :param params_d: A dictionary with keys and values.
    :return:  A list of tuples. If params_d is empty, returns an empty list.
    :example:
        dict_to_params(params_d={"a": [1, 1]}) -> [("a", 1), ("a", 1)]
    """
    params: LParam = []
    for key, value in params_d.items():
        if isinstance(value, TList):
            for value_ in value:
                params.append((key, value_))
        else:
            params.append((key, value))
    return params


def params_to_dict(params: UParam) -> DAny:
    """Convert a list of tuples to a dictionary.

     If the key already exists in the dictionary and its value is a list,
     the new value will be appended to the list.
     If the key already exists in the dictionary and its value is not a list,
     the new value will replace the existing value.

    :param params: A list of tuples.
    :return: A dictionary with keys and values.
    :example:
        params_to_dict(params=[("a", 1), ("a", 1)]) -> {"a": [1, 1]}
    """
    params_d: DAny = {}
    for key, value in params:
        if key in params_d:
            if isinstance(params_d[key], list):
                params_d[key].append(value)
            else:
                params_d[key] = [params_d[key], value]
        else:
            params_d[key] = value
    return params_d
