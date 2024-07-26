"""Examples vdict.py."""
from pathlib import Path

from vhelpers import vdict

# Filter the data to only required keys by include/exclude parameters.
assert vdict.filter_keys(data={"a": "A", "b": "B"}, include=["a"]) == {"a": "A"}
assert vdict.filter_keys(data={"a": "A", "b": "B"}, exclude=["a"]) == {"b": "B"}

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
