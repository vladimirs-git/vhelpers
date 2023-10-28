"""Examples vlist.py."""
from vhelpers import vlist

# Convert a multidimensional list to a flattened list.
assert list(vlist.flatten([1, [2, [3]], 4, [5, [6]]])) == [1, 2, 3, 4, 5, 6]

# Remove duplicates from a list of items.
assert vlist.no_dupl(items=[1, 2, 1]) == [1, 2]

# Split string by punctuation chars.
assert vlist.split(text="1; 2_3-4X5,6", chars="_X", ignore=",") == ["1", "2", "3", "4", "5,6"]

# Convert the input items into a list.
#  If items is a list, set or tuple, simply change its type to list
assert vlist.to_list(items=(1, 2)) == [1, 2]
# Otherwise, create a list with the value as its first item.
assert vlist.to_list(items=1) == [1]
# If items is None return an empty list.
assert vlist.to_list(items=None) == []

# Convert a flat list into a multidimensional list.
assert vlist.to_multi(items=[1, 2, 3, 4, 5], count=2) == [[1, 2], [3, 4], [5]]