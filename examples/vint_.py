"""Examples vre.py."""
from vhelpers import vint

# Convert string digit to int.
assert vint.to_int(digit="1") == 1
assert vint.to_int(digit="a") == 0

# Convert an integer or numeric string to its ordinal representation.
assert vint.to_ordinal(digit=1) == "1st"
assert vint.to_ordinal(digit=2) == "2nd"
assert vint.to_ordinal(digit=21) == "21st"
