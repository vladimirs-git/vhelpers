"""Tests vpath.py."""
import os
from pathlib import Path
from typing import Any

import pytest

from vhelpers import vpath


@pytest.mark.parametrize("pattern, expected", [
    ("test[s]", True),
    ("test1", False),
])
def test__get_dirs(pattern, expected):
    """vpath.get_dirs()"""
    root = Path(__file__).parent.parent

    paths = vpath.get_dirs(root=root, pattern=pattern)

    actual = bool(paths)
    assert actual == expected


@pytest.mark.parametrize("pattern, expected", [
    (r"test_vpath\.py", True),
    ("test_vpath1", False),
])
def test__get_files(pattern, expected):
    """vpath.get_files()"""
    root = Path(__file__).parent

    paths = vpath.get_files(root=root, pattern=pattern)

    actual = bool(paths)
    assert actual == expected


@pytest.mark.parametrize("path, name, expected", [
    ("", "", ""),
    (os.path.abspath(__file__), "", ""),
    (os.path.abspath(__file__), "vhelpers", "vhelpers"),
    (Path(os.path.abspath(__file__)), "vhelpers", "vhelpers"),
    (os.path.abspath(__file__), "typo", ValueError),
    ([os.path.abspath(__file__)], "", TypeError),
])
def test__to_dir(path: Any, name, expected: Any):
    """vpath.to_dir()"""
    if isinstance(expected, (str, Path)):
        path_o = vpath.to_dir(path=path, name=name)
        actual = path_o.name
        assert actual == expected
    else:
        with pytest.raises(expected):
            vpath.to_dir(path=path, name=name)
