"""Examples vdict.py."""
from pathlib import Path

from vhelpers import vdict

# Filters the data to only include the specified required keys.
keys = ["a"]
data = {"a": "A", "b": "B"}
assert vdict.filter_keys(data=data, keys=keys) == {"a": "A"}

# Invert keys and values.
assert vdict.invert(data={1: 2}) == {2: 1}

# Pop the specified item from the data by key.
data = {1: "a", 2: "b"}
assert vdict.pop(data=data, key=3) is None
assert vdict.pop(key=1, data=data) == "a"
assert data == {2: "b"}

# Convert pyproject.toml to a dictionary.
root = Path(__file__).parent.parent
data = vdict.pyproject_d(root)
assert data["tool"]["poetry"]["name"] == "vhelpers"
