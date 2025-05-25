"""Examples vdict.py."""
from pathlib import Path

from vhelpers import vdict

# Filter the data to only required keys by include/exclude parameters.
assert vdict.filter_keys(data={"a": "A", "b": "B"}, include=["a"]) == {"a": "A"}
assert vdict.filter_keys(data={"a": "A", "b": "B"}, exclude=["a"]) == {"b": "B"}

# Convert the input data to a format suitable for JSON serialization.
data = vdict.for_json(data={1: {2, 3}})
assert data == {1: [2, 3]}

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

# Remove empty values from a multidimensional dictionary recursively.
data = vdict.remove_empty(data={1: 1, 2: 0})
assert data == {1: 1}

# ============================ get typed =============================

# Retrieve a nested value from a dictionary using a sequence of keys.
value = vdict.get_any({"a": {"b": "B"}}, "a", "b")
assert value == "B"
value = vdict.get_any({"a": {"b": "B"}}, "a", "c")
assert value is None

value = vdict.get_bool({"a": {"b": True}}, "a", "b")
assert value is True
value = vdict.get_bool({"a": {"b": "B"}}, "a", "b")
assert value is False

value = vdict.get_dict({"a": {"b": {"c": "C"}}}, "a", "b")
assert value == {"c": "C"}
value = vdict.get_dict({"a": {"b": "B"}}, "a", "b")
assert value == {}

value = vdict.get_int({"a": {"b": "1"}}, "a", "b")
assert value == 1
value = vdict.get_int({"a": {"b": "B"}}, "a", "b")
assert value == 0

value = vdict.get_list({"a": {"b": ["B"]}}, "a", "b")
assert value == ["B"]
value = vdict.get_list({"a": {"b": "B"}}, "a", "b")
assert value == []

value = vdict.get_str({"a": {"b": "B"}}, "a", "b")
assert value == "B"
value = vdict.get_str({"a": {"b": 1}}, "a", "b")
assert value == ""