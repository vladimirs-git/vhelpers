"""Examples dict_."""
import vhelpers

# Pop the specified item from the data by key.
data = {1: "a", 2: "b"}
assert vhelpers.pop_d(key=1, data=data) == "a"
assert data == {2: "b"}
assert vhelpers.pop_d(key=3, data=data) is None
assert data == {2: "b"}

# Convert a dictionary to a list of tuples.
assert vhelpers.dict_to_params(params_d={"a": [1, 1]}) == [("a", 1), ("a", 1)]

# Convert a list of tuples to a dictionary.
assert vhelpers.params_to_dict(params=[("a", 1), ("a", 1)]) == {"a": [1, 1]}
