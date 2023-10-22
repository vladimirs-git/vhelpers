"""Helpers for parameters processing.

Parameters are typically included in the query string of a URL,
which is the part of a URL that comes after the question mark "?" character.
"""

from vhelpers.types_ import DAny, LParam, TList, UParam


def from_dict(params_d: DAny) -> LParam:
    """Convert a dictionary to a list of parameters.
    
    :param params_d: A dictionary with keys and values.
    :return:  A list of parameters. If params_d is empty, returns an empty list.
    :example:
        from_dict(params_d={"a": [1, 1]}) -> [("a", 1), ("a", 1)]
    """
    params: LParam = []
    for key, value in params_d.items():
        if isinstance(value, TList):
            for value_ in value:
                params.append((key, value_))
        else:
            params.append((key, value))
    return params


def to_dict(params: UParam) -> DAny:
    """Convert a list of parameters to a dictionary.

    :param params: A list of parameters.
    :return: A dictionary where key is param name.
    :example:
        to_dict(params=[("a", 1), ("a", 1)]) -> {"a": [1, 1]}
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
