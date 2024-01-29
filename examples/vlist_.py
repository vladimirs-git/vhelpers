"""Examples vlist.py."""
from vhelpers import vlist

# Find duplicates of the items.
assert vlist.dupl([1, 2, 1]) == [1]
assert vlist.dupl([{1}, {2}, {1}]) == [{1}]

# Convert a multidimensional list to a flattened list.
assert vlist.flatten([1, [2, [3]], 4, [5, [6]]]) == [1, 2, 3, 4, 5, 6]

# Check is one of items in the items1 is present in the items2.
assert vlist.is_in(items1=[1, 2], items2=[2, 3]) is True
assert vlist.is_in(items1=[1, 2], items2=[3, 4]) is False

# Remove duplicates from a list of items.
assert vlist.no_dupl(items=[1, 2, 1]) == [1, 2]

# Replace one item with another.
items = [1, 2, 3]
vlist.replace(items=items, old=2, new=4)
assert items == [1, 4, 3]

# Split string by punctuation chars.
assert vlist.split(text="1; 2_3-4X5,6", chars="_X", ignore=",") == ["1", "2", "3", "4", "5,6"]

# Convert the input items into a list.
#  If items is a list, set or tuple, simply change its type to list
assert vlist.to_list(items=(1, 2)) == [1, 2]
# Otherwise, create a list with the value as its first item.
assert vlist.to_list(items=1) == [1]
# If items is None return an empty list.
assert vlist.to_list(items=None) == []

# Convert a flat list into a multidimensional list with a fixed number of inner lists.
assert vlist.to_lists(items=[1, 2, 3, 4, 5], count=2) == [[1, 2, 3], [4, 5]]
assert vlist.to_lists(items=(1, 2, 3, 4, 5), count=3) == [[1, 2], [3, 4], [5]]

# Convert the input items from any into a list of string.
assert vlist.to_lstr(items=[1, "2"]) == ["1", "2"]
assert vlist.to_lstr(1) == ["1"]
assert vlist.to_lstr("") == []

# Convert a flat list into a multidimensional list.
assert vlist.to_multi(items=[1, 2, 3, 4, 5], count=2) == [[1, 2], [3, 4], [5]]
