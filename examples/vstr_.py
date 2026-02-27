"""Examples vstr.py."""

from vhelpers import vstr

# Join args by delimiter that is first argument, skipping empty strings.
assert vstr.join(",", "a", "", 0, 1) == "a,0,1"

# Join args by '\n' character, skipping empty strings.
assert vstr.join_lines("a", "", 0, 1) == "a\n0\n1"

# Create parameters for the __repr__() method.
assert vstr.repr_info("a", "b", c="c", d="d") == "a, b, c=c, d=d"
assert vstr.repr_params("a", "b", c="c", d="d") == "'a', 'b', c='c', d='d'"

# Reverse the characters in a string.
assert vstr.quoted("a", "'") == "'a'"

# Reverse the characters in a string.
assert vstr.reverse("abc") == "cba"

# Split the text at the specified index.
assert vstr.split_idx(text="before_after", idx=7) == ("before_", "after")
