"""Tests vdict.py."""
import hashlib
from pathlib import Path

import pytest

from vhelpers import vdict

ROOT = Path(__file__).parent.parent


@pytest.mark.parametrize("keys, data, expected", [
    ([], {}, {}),
    (["a"], {}, {}),
    ([], {1: 11, "a": "A"}, {}),
    ([1], {1: 11, "a": "A"}, {1: 11}),
    (["a"], {1: 11, "a": "A"}, {"a": "A"}),
])
def test__filter_keys(keys, data, expected):
    """vdict.filter_keys()."""
    actual = vdict.filter_keys(keys=keys, data=data)
    assert actual == expected


@pytest.mark.parametrize("keys, data, expected", [
    ([], {}, {}),
])
def test__filter_keys(keys, data, expected):
    """vdict.filter_keys()."""
    actual = vdict.filter_keys(keys=keys, data=data)
    assert actual == expected


@pytest.mark.parametrize("data, expected", [
    ({}, "99914b932bd37a50b983c5e7c90ae93b"),
    ({1: 2}, "9655ff2d2a8e0d3ed0fa76bf198e5c9a"),
])
def test__md5hash(data, expected):
    """vdict.md5hash()."""
    actual = vdict.md5hash(data=data)

    assert actual == expected


@pytest.mark.parametrize("key, data, expected", [
    (1, {1: 2}, 2),
    (2, {1: 2}, None),
])
def test__pop(key, data, expected):
    """vdict.pop()."""
    actual = vdict.pop(key=key, data=data)
    assert actual == expected


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
    ({}, 35880782557768839320141082861857074615369399329199884041472448612899930421573),
    ({1: 2}, 7056226925880052529895136741807659295326470122191746861533752402396562224103),
])
def test__sha256hash(data, expected):
    """vdict.sha256hash()."""
    actual = vdict.sha256hash(data=data)

    assert actual == expected
