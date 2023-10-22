"""Examples vlist.py."""
from vhelpers import vlist

# Convert the input items into a list.
#  If items is a list, set or tuple, simply change its type to list
assert vlist.from_any(items=(1, 2)) == [1, 2]
# Otherwise, create a list with the value as its first item.
assert vlist.from_any(items=1) == [1]
# If items is None return an empty list.
assert vlist.from_any(items=None) == []

# Remove duplicates from a list of items.
assert vlist.no_dupl(items=[1, 2, 1]) == [1, 2]
