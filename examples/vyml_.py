"""Examples vdict.py."""

from vhelpers import vyml

# Create commands in YAML format.
items = [("router1", "interface Ethernet1/1", ["description text", "shutdown"])]
result = """
---
router1: |
 interface Ethernet1/1
  description text
  shutdown
""".strip()
assert vyml.host_cmds(items) == result

# Join parent command and children commands using indentation.
result = """ interface Ethernet1/1\n  description text\n  shutdown"""
assert vyml.cmd_cmds(cmd="interface Ethernet1/1", cmds=["description text", "shutdown"]) == result
