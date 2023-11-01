"""Examples vstr.py."""

from vhelpers import vstr

# Create parameters for the __repr__() method.
assert vstr.repr_info("a", "b", c="c", d="d") == "a, b, c=c, d=d"
assert vstr.repr_params("a", "b", c="c", d="d") == "'a', 'b', c='c', d='d'"

# Reverse the characters in a string.
assert vstr.reverse("abc") == "cba"
