"""Unittests vdict.py."""
from pathlib import Path

import pytest

from vhelpers import vdict

POP = [
    (1, {1: 2}, 2),
    (2, {1: 2}, None),
]

ROOT = Path(__file__).parent.parent
PYPROJECT_D = [
    (ROOT, "vhelpers"),
    (str(ROOT), "vhelpers"),
]


@pytest.mark.parametrize("key, data, expected", POP)
def test_pop(key, data, expected):
    """pop."""
    actual = vdict.pop(key=key, data=data)
    assert actual == expected


@pytest.mark.parametrize("root, expected", PYPROJECT_D)
def test_pyproject_d(root, expected):
    """pyproject_d."""
    data = vdict.pyproject_d(root=root)
    actual = data["tool"]["poetry"]["name"]
    assert actual == expected
