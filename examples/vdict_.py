"""Examples vdict.py."""
from pathlib import Path

from vhelpers import vdict

# Pop the specified item from the data by key.
data = {1: "a", 2: "b"}
assert vdict.pop(key=1, data=data) == "a"
assert data == {2: "b"}

# If key is absent in data, do nothing and return None.
assert vdict.pop(key=3, data=data) is None
assert data == {2: "b"}

# Convert pyproject.toml to a dictionary.
root = Path(__file__).parent.parent
data = vdict.pyproject_d(root)
assert data["tool"]["poetry"]["name"] == "vhelpers"
