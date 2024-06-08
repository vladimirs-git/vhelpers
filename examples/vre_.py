"""Examples vre.py."""
from vhelpers import vre

# Find value in list of commands by required key.
assert vre.cmd_value(".+description ", [" description VALUE"]) == "VALUE"

# Find all substrings between the start and end regexes.
TEXT = "a1\nb2\nc3\nd4"
assert vre.between(text=TEXT, start="b2", end="c3", w_start=True, w_end=True) == "b2\nc3"

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

# Parse 1st IP address from string. If nothing is found, returns an empty string.
assert vre.ip("text 10.0.0.1/24 10.0.0.2/24 text") == "10.0.0.1"
assert vre.prefix("text 10.0.0.1/24 10.0.0.2/24 text") == "10.0.0.1/24"
