"""Tests vdict.py."""

from pathlib import Path
from typing import Any

import pytest

from vhelpers import vdict
from vhelpers.types_ import LStr

ROOT = Path(__file__).parent.parent


@pytest.mark.parametrize("data, include, exclude, expected", [
    # include
    ({1: 11, "a": "A", "b": "B"}, [1], None, {1: 11}),
    ({1: 11, "a": "A", "b": "B"}, ["a"], None, {"a": "A"}),
    ({1: 11, "a": "A", "b": "B"}, [1, "a"], None, {1: 11, "a": "A"}),
    # exclude
    ({1: 11, "a": "A", "b": "B"}, None, [1], {"a": "A", "b": "B"}),
    ({1: 11, "a": "A", "b": "B"}, None, ["a"], {1: 11, "b": "B"}),
    ({1: 11, "a": "A", "b": "B"}, None, [1, "a"], {"b": "B"}),
    # combo
    ({1: 11, "a": "A", "b": "B"}, [1, "a"], ["a"], {1: 11}),
    # any
    ({1: 11, "a": "A", "b": "B"}, None, None, {1: 11, "a": "A", "b": "B"}),
    ({1: 11, "a": "A", "b": "B"}, [], [], {1: 11, "a": "A", "b": "B"}),
    ({}, [], [], {}),
])
def test__filter_keys(data, include, exclude, expected):
    """vdict.filter_keys()."""
    actual = vdict.filter_keys(data=data, include=include, exclude=exclude)
    assert actual == expected


@pytest.mark.parametrize("data, expected", [
    # level1
    ({"k1": "v"}, {"k1": "v"}),
    ({"k1": ["v"]}, {"k1": ["v"]}),
    ({"k1": {"v"}}, {"k1": ["v"]}),
    ({0: 0}, {0: 0}),
    ({0: None}, {0: None}),
    # level2
    ({"k1": {"k2": "v"}}, {"k1": {"k2": "v"}}),
    ({"k1": {"k2": ["v"]}}, {"k1": {"k2": ["v"]}}),
    ({"k1": {"k2": {"v"}}}, {"k1": {"k2": ["v"]}}),
    # # level3
    ({"k1": {"k2": {"k3": "v"}}}, {"k1": {"k2": {"k3": "v"}}}),
    ({"k1": {"k2": {"k3": ["v"]}}}, {"k1": {"k2": {"k3": ["v"]}}}),
    ({"k1": {"k2": {"k3": {"v"}}}}, {"k1": {"k2": {"k3": ["v"]}}}),
    ({}, {}),
])
def test__for_json(data, expected):
    """helpers.for_json()"""
    actual = vdict.for_json(data=data)

    assert actual == expected


@pytest.mark.parametrize("data, expected", [
    ({}, "99914b932bd37a50b983c5e7c90ae93b"),
    ({1: 2}, "9655ff2d2a8e0d3ed0fa76bf198e5c9a"),
])
def test__md5hash(data, expected):
    """vdict.md5hash()."""
    actual = vdict.md5hash(data=data)

    assert actual == expected


@pytest.mark.parametrize("key, expected", [
    (1, 2),
    (2, None),
])
def test__pop(key, expected):
    """vdict.pop()."""
    data = {1: 2}

    actual = vdict.pop(data=data, key=key)

    assert actual == expected
    assert data.get(key) is None


@pytest.mark.parametrize("root, expected", [
    (ROOT, "vhelpers"),
    (str(ROOT), "vhelpers"),
])
def test__pyproject_d(root, expected):
    """vdict.pyproject_d()."""
    data = vdict.pyproject_d(root=root)
    actual = data["tool"]["poetry"]["name"]
    assert actual == expected


@pytest.mark.parametrize("data, expected", [
    # level1
    ({}, {}),
    ({"a": "a"}, {"a": "a"}),
    ({"a": ""}, {}),
    ({"a": 0}, {}),
    ({"a": []}, {}),
    ({"a": None}, {}),
    ({1: 1}, {1: 1}),
    ({1: 0}, {}),
    # level2
    ({"a": {"b": "b"}}, {"a": {"b": "b"}}),
    ({"a": {"b": "b", "c": ""}}, {"a": {"b": "b"}}),
    ({"a": {"b": ""}}, {}),
    # level3
    ({"a": {"b": {"c": "c"}}}, {"a": {"b": {"c": "c"}}}),
    ({"a": {"b": {"c": "c", "d": ""}}}, {"a": {"b": {"c": "c"}}}),
    ({"a": {"b": {"c": ""}}}, {}),
])
def test__remove_empty_values(data, expected):
    """helpers.remove_empty_values()."""
    actual = vdict.remove_empty(data)

    assert actual == expected


@pytest.mark.parametrize("data, expected", [
    ({}, 35880782557768839320141082861857074615369399329199884041472448612899930421573),
    ({1: 2}, 7056226925880052529895136741807659295326470122191746861533752402396562224103),
])
def test__sha256hash(data, expected):
    """vdict.sha256hash()."""
    actual = vdict.sha256hash(data=data)

    assert actual == expected


@pytest.mark.parametrize("keys, data, expected", [
    (["a"], {"a": None}, None),
    (["a"], {"a": "A"}, "A"),
    (["a"], {"a": 1}, 1),
    (["a"], {"a": {}}, {}),
    (["a"], {"a": {"k": "A"}}, {"k": "A"}),
    (["a", "b"], {"a": {"b": None}}, None),
    (["a", "b"], {"a": {"b": "A"}}, "A"),
    (["a", "b"], {"a": {"b": 1}}, 1),
    (["a", "b"], {"a": {"b": {"k": "B"}}}, {"k": "B"}),
    (["a", "b", "c"], {"a": {"b": {"c": None}}}, None),
    (["a", "b", "c"], {"a": {"b": {"c": "A"}}}, "A"),
    (["a", "b", "c"], {"a": {"b": {"c": 1}}}, 1),
    (["a", "b", "c"], {"a": {"b": {"c": {}}}}, {}),
    (["a", "b", "c"], {"a": {"b": {"c": {"k": "C"}}}}, {"k": "C"}),
    # list
    (["a", 0, "b"], {"a": [{"b": None}]}, None),
    (["a", 0, "b"], {"a": [{"b": "B"}]}, "B"),
    (["a", 0, "b"], {"a": {"b": "B"}}, None),
])
def test__get_any(keys: LStr, data: dict, expected: Any):
    """vdict.get_any()."""
    actual = vdict.get_any(data, *keys)

    assert actual == expected


@pytest.mark.parametrize("keys, data, expected", [
    (["a"], {"a": None}, False),
    (["a"], {"a": 1}, False),
    (["a"], {"a": True}, True),
    (["a"], {"a": False}, False),
    (["a", "b"], {"a": {"b": True}}, True),
    (["a", "b"], {"a": {"b": None}}, False),
    (["a", "b", "c"], {"a": {"b": {"c": True}}}, True),
    (["a", "b", "c"], {"a": {"b": {"c": None}}}, False),
    # list
    (["a", 0, "b"], {"a": [{"b": None}]}, False),
    (["a", 0, "b"], {"a": [{"b": True}]}, True),
    (["a", 0, "b"], {"a": {"b": True}}, False),
])
def test__get_bool(keys: LStr, data: dict, expected: Any):
    """vdict.get_bool()."""
    actual = vdict.get_bool(data, *keys)

    assert actual == expected


@pytest.mark.parametrize("keys, data, expected", [
    (["a"], {"a": None}, {}),
    (["a"], {"a": 1}, {}),
    (["a"], {"a": {}}, {}),
    (["a"], {"a": {"k": "A"}}, {"k": "A"}),
    (["a", "b"], {"a": {"b": {"k": "B"}}}, {"k": "B"}),
    (["a", "b", "c"], {"a": {"b": {"c": {"k": "C"}}}}, {"k": "C"}),
    # list
    (["a", 0, "b"], {"a": [{"b": None}]}, {}),
    (["a", 0, "b"], {"a": [{"b": {"k": "B"}}]}, {"k": "B"}),
    (["a", 0, "b"], {"a": {"b": {"k": "B"}}}, {}),
])
def test__get_dict(keys: LStr, data: dict, expected: Any):
    """vdict.get_dict()."""
    actual = vdict.get_dict(data, *keys)

    assert actual == expected


@pytest.mark.parametrize("keys, data, expected", [
    (["id"], {"id": "1"}, 1),
    (["id"], {"id": 0}, 0),
    (["id"], {"id": "0"}, 0),
    (["a", "b"], {"a": {"b": 1}}, 1),
    (["a", "b"], {"a": {"b": None}}, 0),
    (["a", "b"], {"a": {"b": "1"}}, 1),
    (["a", "b", "c"], {"a": {"b": {"c": 3}}}, 3),
    (["a", "b", "c"], {"a": {"b": {"c": None}}}, 0),
    (["id"], None, 0),
    # list
    (["a", 0, "b"], {"a": [{"b": None}]}, 0),
    (["a", 0, "b"], {"a": [{"b": 1}]}, 1),
    (["a", 0, "b"], {"a": {"b": 1}}, 0),
])
def test__get_int(keys: LStr, data: dict, expected: Any):
    """vdict.get_int()."""
    actual = vdict.get_int(data, *keys)

    assert actual == expected


@pytest.mark.parametrize("keys, data, expected", [
    (["a"], {"a": None}, []),
    (["a"], {"a": 1}, []),
    (["a"], {"a": ["A"]}, ["A"]),
    (["a"], {"a": [""]}, [""]),
    (["a", "b"], {"a": {"b": ["B"]}}, ["B"]),
    (["a", "b"], {"a": {"b": None}}, []),
    (["a", "b", "c"], {"a": {"b": {"c": ["C"]}}}, ["C"]),
    (["a", "b", "c"], {"a": {"b": {"c": None}}}, []),
    # list
    (["a", 0, "b"], {"a": [{"b": "B"}]}, []),
    (["a", 0, "b"], {"a": [{"b": ["B"]}]}, ["B"]),
    (["a", 0, "b"], {"a": {"b": ["B"]}}, []),
])
def test__get_list(keys: LStr, data: dict, expected: Any):
    """vdict.get_list()."""
    actual = vdict.get_list(data, *keys)

    assert actual == expected


@pytest.mark.parametrize("keys, data, expected", [
    (["a"], {"a": None}, ""),
    (["a"], {"a": 1}, ""),
    (["a"], {"a": "A"}, "A"),
    (["a"], {"a": ""}, ""),
    (["a", "b"], {"a": {"b": "B"}}, "B"),
    (["a", "b"], {"a": {"b": None}}, ""),
    (["a", "b", "c"], {"a": {"b": {"c": "C"}}}, "C"),
    (["a", "b", "c"], {"a": {"b": {"c": None}}}, ""),
    # list
    (["a", 0, "b"], {"a": [{"b": None}]}, ""),
    (["a", 0, "b"], {"a": [{"b": "B"}]}, "B"),
    (["a", 0, "b"], {"a": {"b": "B"}}, ""),
])
def test__get_str(keys: LStr, data: dict, expected: Any):
    """vdict.get_str()."""
    actual = vdict.get_str(data, *keys)

    assert actual == expected


@pytest.mark.parametrize("keys, data, type_, expected", [
    (["a"], {"a": None}, str, ""),
    (["a"], {"a": 1}, str, ""),
    (["a"], {"a": None}, int, 0),
    (["a"], {"a": 1}, int, 1),
])
def test__get_keys(keys: LStr, data: dict, type_, expected: Any):
    """vdict._get_keys()."""
    actual = vdict._get_keys(data, *keys, type_=type_)

    assert actual == expected
