"""Tests helpers.py."""

import pytest

from vhelpers import helpers


@pytest.mark.parametrize("config, expected", [
    ("", []),
    ("a\nb", ["a", "b"]),
    ([], []),
    (["a"], ["a"]),
])
def test__cmd_key(config, expected):
    """helpers.cmd_key()."""
    actual = helpers.init_cmds(config=config)
    assert actual == expected
