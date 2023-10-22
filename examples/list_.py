"""Examples list_."""
import vhelpers

# Remove duplicates from a list of items.
assert vhelpers.no_dupl(items=[1, 2, 1]) == [1, 2]

# Convert the input items into a list.
assert vhelpers.to_list(items=(1, 2)) == [1, 2]
assert vhelpers.to_list(items=None) == []
assert vhelpers.to_list(items=1) == [1]
