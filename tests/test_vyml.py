"""Unittests vyml.py."""

import pytest

from vhelpers import vyml
from vhelpers.types_ import UStr, LT3Strs


@pytest.mark.parametrize("items, expected", [
    ([], "---"),
    ([("host1", "cmdA", "cmd1\ncmd2")],
     "---\nhost1: |\n cmdA\n  cmd1\n  cmd2"),
    ([("host1", "cmdA", ["cmd1", "cmd2"])],
     "---\nhost1: |\n cmdA\n  cmd1\n  cmd2"),
    ([("host1", "cmdA", ["cmd1"]), ("host1", "cmdA", ["cmd2"])],
     "---\nhost1: |\n cmdA\n  cmd1\n cmdA\n  cmd2"),
    ([("host1", "cmdA", ["cmd1", "cmd2"]), ("host2", "cmdB", ["cmd3", "cmd4"])],
     "---\nhost1: |\n cmdA\n  cmd1\n  cmd2\nhost2: |\n cmdB\n  cmd3\n  cmd4"),
])
def test___host_cmds(items: LT3Strs, expected: str):
    """vyml.host_cmds()."""
    actual = vyml.host_cmds(items=items)
    assert actual == expected


@pytest.mark.parametrize("cmd, cmds, expected", [
    ("", [], ""),
    ("", ["cmd1"], "  cmd1"),
    ("cmdA", ["cmd1"], " cmdA\n  cmd1"),
    ("cmdA", ["cmd1", "cmd2"], " cmdA\n  cmd1\n  cmd2"),
])
def test___cmd_cmds(cmd: str, cmds: UStr, expected: str):
    """vyml.cmd_cmds()."""
    actual = vyml.cmd_cmds(cmd=cmd, cmds=cmds)
    assert actual == expected
