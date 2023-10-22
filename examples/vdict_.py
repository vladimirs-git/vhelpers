"""Examples vdict.py."""
from vhelpers import vdict

# Pop the specified item from the data by key.
data = {1: "a", 2: "b"}
assert vdict.pop_d(key=1, data=data) == "a"
assert data == {2: "b"}

# If key is absent in data, do nothing and return None.
assert vdict.pop_d(key=3, data=data) is None
assert data == {2: "b"}
