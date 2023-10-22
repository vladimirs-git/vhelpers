"""Examples vparams.py."""
from vhelpers import vparams

# Convert a dictionary to a list of parameters.
assert vparams.from_dict(params_d={"a": [1, 1]}) == [("a", 1), ("a", 1)]

# Convert a list of parameters to a dictionary.
assert vparams.to_dict(params=[("a", 1), ("a", 1)]) == {"a": [1, 1]}
