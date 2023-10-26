"""Unittests vdict.py."""
from pathlib import Path

import pytest

from vhelpers import vdict

ROOT = Path(__file__).parent.parent


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
