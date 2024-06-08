"""Examples vcfg.py."""
from vhelpers import vcfg

# Find key in list of commands.
assert vcfg.cmd_key(key="shutdown", config=["shutdown"]) == "shutdown"

# Find value in command by required key.
assert vcfg.cmd_value(key="description ", config=["description VALUE"]) == "VALUE"
