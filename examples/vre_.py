"""Examples vre.py."""
from vhelpers import vre

# Parse string items using findall.
assert vre.find1(pattern="a(b)cde", string="abcde") == "b"
assert vre.find1(pattern="a(b)cde", string="acde") == ""
assert vre.find2(pattern="a(b)(c)de", string="abcde") == ("b", "c")
assert vre.find2(pattern="a(b)(c)de", string="acde") == ("", "")
assert vre.find3(pattern="a(b)(c)(d)e", string="abcde") == ("b", "c", "d")
assert vre.find3(pattern="a(b)(c)(d)e", string="acde") == ("", "", "")
assert vre.find4(pattern="a(b)(c)(d)(e)", string="abcde") == ("b", "c", "d", "e")
assert vre.find4(pattern="a(b)(c)(d)(e)", string="acde") == ("", "", "", "")

# Parse integer items using findall.
assert vre.find1i(pattern="a([0-9]+)b", string="a123b") == 123
assert vre.find1i(pattern="a([0-9]+)b", string="ab") == 0
assert vre.find2i(pattern="a([0-9])b([0-9])c", string="a1b2c") == (1, 2)
assert vre.find2i(pattern="a([0-9])b([0-9])c", string="a1bc") == (0, 0)

# Parse string item that match one of regex in patterns.
assert vre.find1s(patterns=["a(a)cde", "a(b)cde"], string="abcde") == "b"
