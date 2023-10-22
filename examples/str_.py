"""Examples str_."""
import vhelpers

# Parse items of re.findall.
assert vhelpers.findall1(pattern="a(b)cde", string="abcde") == "b"
assert vhelpers.findall2(pattern="a(b)(c)de", string="abcde") == ("b", "c")
assert vhelpers.findall3(pattern="a(b)(c)(d)e", string="abcde") == ("b", "c", "d")
assert vhelpers.findall4(pattern="a(b)(c)(d)(e)", string="abcde") == ("b", "c", "d", "e")
