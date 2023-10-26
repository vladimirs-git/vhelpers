"""Examples vre.py."""
from vhelpers import vint

# Convert string digit to int.
assert vint.to_int(digit="1") == 1
assert vint.to_int(digit="a") == 0
