"""Examples vre.py."""
from vhelpers import vre

# Parse items using findall.
assert vre.find1(pattern="a(b)cde", string="abcde") == "b"
assert vre.find2(pattern="a(b)(c)de", string="abcde") == ("b", "c")
assert vre.find3(pattern="a(b)(c)(d)e", string="abcde") == ("b", "c", "d")
assert vre.find4(pattern="a(b)(c)(d)(e)", string="abcde") == ("b", "c", "d", "e")
