"""Unittests vlist.py."""

import pytest

from vhelpers import vcfg


@pytest.mark.parametrize("config, expected", [
    # str
    ("", ""),
    ("shutdown\nTYPO", "shutdown"),
    ("shutdown TYPO", ""),
    ("    shutdown SPACES", ""),
    # list
    ([], ""),
    (["shutdown", "TYPO"], "shutdown"),
    (["shutdown TYPO"], ""),
    (["    shutdown SPACES"], ""),
])
def test__cmd_key(config, expected):
    """vcfg.cmd_key()."""
    actual = vcfg.cmd_key(key="shutdown", config=config)
    assert actual == expected


@pytest.mark.parametrize("config, expected", [
    # str
    ("", ""),
    ("description VALUE\ndescriptionTYPO", "VALUE"),
    ("description \tVALUE\t", "\tVALUE\t"),
    ("descriptionTYPO", ""),
    ("    description SPACES", ""),
    # list
    ([], ""),
    (["description VALUE", "descriptionTYPO"], "VALUE"),
    (["description \tVALUE\t"], "\tVALUE\t"),
    (["descriptionTYPO"], ""),
    (["    description SPACES"], ""),
])
def test__cmd_value(config, expected):
    """vcfg.cmd_value()."""
    actual = vcfg.cmd_value(key="description ", config=config)
    assert actual == expected
