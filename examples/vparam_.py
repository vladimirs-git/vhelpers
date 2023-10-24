"""Examples vparam.py."""
from vhelpers import vparam

# Convert a dictionary to a list of parameters.
assert vparam.from_dict(params_d={"a": [1, 1]}) == [("a", 1), ("a", 1)]

# Convert a list of parameters to a dictionary.
assert vparam.to_dict(params=[("a", 1), ("a", 1)]) == {"a": [1, 1]}
