
vhelpers
========

Often used functions in vladimirs-git projects.


Requirements
------------

Python >=3.8


Installation
------------

Install the package from pypi.org release

.. code:: bash

    pip install vhelpers

or install the package from github.com release

.. code:: bash

    pip install https://github.com/vladimirs-git/vhelpers/archive/refs/tags/0.2.2.tar.gz

or install the package from github.com repository

.. code:: bash

    pip install git+https://github.com/vladimirs-git/vhelpers


Usage
-----
For easy navigation, functions are grouped by some key concept, mostly based on their return data type.
For more details, please refer to the `./examples`_ directory where you will find numerous examples.

.. contents::


vdate
=====


delta(start, end)
-----------------
Calculate the elapsed days, hours, minutes and seconds between two datetime objects.

=========== ========== =============================================================================
Parameter   Type       Description
=========== ========== =============================================================================
start       *datetime* The starting datetime object.
end         *datetime* The ending datetime object. If None, the current datetime is used.
=========== ========== =============================================================================

Return
      *DInt* A dictionary containing the elapsed hours, minutes, and seconds. If end is None, update data in object.

.. code:: python

    from datetime import datetime
    from vhelpers import vdate

    start = datetime.strptime("2001-01-02 2:3:4", "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime("2002-02-03 3:4:5", "%Y-%m-%d %H:%M:%S")
    print(vdate.delta(start, end))  # {'hours': 9529, 'minutes': 1, 'seconds': 1}


delta_s(args, kwargs)
---------------------
Calculate the elapsed time in the format %H:%M:%S.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
args               The arguments for calculating the time delta.
kwargs             The keyword arguments for calculating the time delta.
=========== ====== =================================================================================

Return
      *str* The elapsed time in the format %H:%M:%S.

.. code:: python

    from datetime import datetime
    from vhelpers import vdate

    start = datetime.strptime("2001-01-02 2:3:4", "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime("2002-02-03 3:4:5", "%Y-%m-%d %H:%M:%S")
    print(vdate.delta_s(start, end))  # 9529:01:01


vdict
=====
Helpers for dictionary processing.


filter_keys(data, include, exclude)
-----------------------------------
Filter the data to only required keys by include/exclude parameters.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
data        *dict* Dictionary to be filtered.
include     *list* Keys that should be present in the filtered dictionary.
exclude     *list* Keys that should not be present in the filtered dictionary.
=========== ====== =================================================================================

Return
      *dict* New dictionary containing only the required keys.

.. code:: python

    from vhelpers import vdict

    assert vdict.filter_keys(data={"a": "A", "b": "B"}, include=["a"]) == {"a": "A"}
    assert vdict.filter_keys(data={"a": "A", "b": "B"}, exclude=["a"]) == {"b": "B"}


invert(data)
------------
Invert keys and values.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
data        *dict* Dictionary to invert.
=========== ====== =================================================================================

Return
      *dict* Dictionary with keys and values inverted.

.. code:: python

    from vhelpers import vdict

    assert vdict.invert(data={1: 2}) == {2: 1}


md5hash(data)
-------------
Create MD5 hash of a dictionary.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
data        *dict* Dictionary to be hashed.
=========== ====== =================================================================================

Return
      *str* String representing the MD5 hash of the dictionary.


pop(key, data)
--------------
Pop the specified item from the data by key.  If key is absent in data, do nothing and return None.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
data        *dict* The dictionary from which the key is to be popped.
key         *str*  The key to be popped from the data.
=========== ====== =================================================================================

Return
      *str* The popped item if key is present in data, otherwise None.

.. code:: python

    from vhelpers import vdict

    data = {1: "a", 2: "b"}
    assert vdict.pop(data=data, key=3) is None
    assert vdict.pop(key=1, data=data) == "a"
    assert data == {2: "b"}


pyproject_d(root)
-----------------
Convert pyproject.toml to a dictionary.

=========== =================== ====================================================================
Parameter   Type                Description
=========== =================== ====================================================================
root        *Union[Path, str]*  The root directory or path to the pyproject.toml file.
=========== =================== ====================================================================

Return
      *Dict[str, Any]* A dictionary containing the data from pyproject.toml.

.. code:: python

    from vhelpers import vdict
    from pathlib import Path

    root = Path(__file__).parent.parent
    data = vdict.pyproject_d(root)
    assert data["tool"]["poetry"]["name"] == "vhelpers"


sha256hash(data)
----------------
Create SHA-256 hash of a dictionary.

=========== =================== ====================================================================
Parameter   Type                Description
=========== =================== ====================================================================
root        *dict*              Dictionary to be hashed.
=========== =================== ====================================================================

Return
      *int* Integer representing the SHA-256 hash of the dictionary.


vint
====
Helpers for int processing.


to_int(digit)
-------------
Convert string digit to integer.

=========== ================= ======================================================================
Parameter   Type              Description
=========== ================= ======================================================================
digit       *Union[int, str]* Digit, string ot integer.
=========== ================= ======================================================================

Return
      *int* Integer or 0 if value is not digit.

.. code:: python

    from vhelpers import vint

    assert vint.to_int(digit="1") == 1
    assert vint.to_int(digit="a") == 0


vip
===
Helpers for ip addresses processing.


ip_prefixlen(address)
---------------------
Convert IPv4 address with mask to address with prefix length.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
address     *str*  IP addresses with mask.
=========== ====== =================================================================================

Return
      *str* IP addresses with prefix length.

.. code:: python

    from vhelpers import vip

    assert vip.ip_prefixlen(address="10.0.0.1 255.255.255.0") == "10.0.0.1/24"


ips_prefixlen(addresses)
------------------------
Convert IPv4 addresses with mask to addresses with prefix length.

=========== ============ ===========================================================================
Parameter   Type         Description
=========== ============ ===========================================================================
addresses   *List[str]*  A list of IP addresses with mask.
=========== ============ ===========================================================================

Return
      *List[str]* A list of IP addresses with prefix length.

.. code:: python

    from vhelpers import vip

    assert vip.ips_prefixlen(addresses=["10.0.0.1 255.255.255.0"]) == ["10.0.0.1/24"]


vlist
=====
Helpers for list processing.


dupl(items)
-----------
Find duplicates of the items.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
items       *list* A list of items where need to find duplicates.
=========== ====== =================================================================================

Return
      *list* A list of items with duplicates.

.. code:: python

    from vhelpers import vlist

    assert vlist.dupl([1, 2, 1]) == [1]
    assert vlist.dupl([{1}, {2}, {1}]) == [{1}]


flatten(items, ignore_types)
----------------------------
Convert a multidimensional list to a flattened list.

============ ============ ==========================================================================
Parameter    Type         Description
============ ============ ==========================================================================
items        *Sequence*   The list to be flattened.
ignore_types  Tuple[Type] Types to be ignored during flattening, defaults to (str, bytes)
============ ============ ==========================================================================

Return
      *Generator* A generator that yields the flattened list.

.. code:: python

    from vhelpers import vlist

    assert vlist.flatten([1, [2, [3]], 4, [5, [6]]]) == [1, 2, 3, 4, 5, 6]


is_in(items1, items2)
---------------------
Check if any item in items1 is present in items2.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
items1      *list* A list of items.
items2      *list* A list of items.
=========== ====== =================================================================================

Return
      *bool* True if any item in items1 is present in items2, False otherwise.


no_dupl(items)
--------------
Remove duplicates from a list of items.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
items       *list* A list of items.
=========== ====== =================================================================================

Return
      *list* A list of items without duplicates.

.. code:: python

    from vhelpers import vlist

    assert vlist.no_dupl(items=[1, 2, 1]) == [1, 2]


replace(items, old, new)
------------------------
Replace one item with another.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
items       *list* The list of items where need replace item.
old         *Any*  The item to be replaced.
new         *Any*  The item to replace with.
=========== ====== =================================================================================

Return
      *None* Update items.

.. code:: python

    from vhelpers import vlist

    assert vlist.replace(items=[1, 2, 3], old=2, new=4) == [1, 4, 3]


split(text, chars, ignore)
--------------------------
Split string by punctuation chars.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
text        *str*  Text to split by punctuation.
chars       *str*  Extra punctuation chars.
ignore      *str*  Ignore punctuation chars.
=========== ====== =================================================================================

Return
      *List[str]* Values without punctuation.

.. code:: python

    from vhelpers import vlist

    assert vlist.split(text="1; 2_3-4X5,6", chars="_X", ignore=",") == ["1", "2", "3", "4", "5,6"]


to_list(items)
--------------
Convert the input items from any into a list.
If items is a list, set or tuple, simply change its type to list.
Otherwise, create a list with the value as its first item.
If items is None return an empty list.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
items       *list* The items to be converted into a list.
=========== ====== =================================================================================

Return
      *list* The converted list.

.. code:: python

    from vhelpers import vlist

    # Convert the input items into a list.
    #  If items is a list, set or tuple, simply change its type to list
    assert vlist.to_list(items=(1, 2)) == [1, 2]
    # Otherwise, create a list with the value as its first item.
    assert vlist.to_list(items=1) == [1]
    # If items is None return an empty list.
    assert vlist.to_list(items=None) == []


to_lists(items, count)
----------------------
Convert a flat list into a multidimensional list with a fixed number of inner lists.

=========== ============ ===========================================================================
Parameter   Type         Description
=========== ============ ===========================================================================
items       *list*       The flat list to convert.
count       *int*        The number of inner lists.
=========== ============ ===========================================================================

Return
      *List[List[Any]* A multidimensional list.

.. code:: python

    from vhelpers import vlist

    assert vlist.to_lists(items=[1, 2, 3, 4, 5], count=2) == [[1, 2, 3], [4, 5]]
    assert vlist.to_lists(items=(1, 2, 3, 4, 5), count=3) == [[1, 2], [3, 4], [5]]


to_lstr(items)
--------------
Convert the input items from any into a list of string.
If items is a list, set or tuple, simply change its type to list.
If items is None or empty string return an empty list.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
items       *Any*  The items to be converted into a list of string.
=========== ====== =================================================================================

Return
      *list* The converted list.

.. code:: python

    from vhelpers import vlist

    assert vlist.to_lstr(items=[1, "2"]) == ["1", "2"]
    assert vlist.to_lstr(1) == ["1"]
    assert vlist.to_lstr("") == []


to_multi(items, count)
----------------------
Convert a flat list into a multidimensional list. Convert a list with the specified number of items
in each inner list.

=========== ============ ===========================================================================
Parameter   Type         Description
=========== ============ ===========================================================================
items       *list*       The flat list to convert.
count       *int*        The number of items to include in each inner list.
=========== ============ ===========================================================================

Return
      *LLAny* A multidimensional list with the specified number of items in each inner list.

.. code:: python

    from vhelpers import vlist

    assert vlist.to_multi(items=[1, 2, 3, 4, 5], count=2) == [[1, 2], [3, 4], [5]]


vparam
======
Helpers for parameters processing.
Parameters are typically included in the query string of a URL,
which is the part of a URL that comes after the question mark "?" character.


from_dict(params_d)
-------------------
Convert a dictionary to a list of parameters.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
params_d    *dict* A dictionary with keys and values.
=========== ====== =================================================================================

Return
      *list[tuple[str, Any]]* A list of parameters. If params_d is empty, returns an empty list.

.. code:: python

    from vhelpers import vparam

    assert vparam.from_dict(params_d={"a": [1, 1]}) == [("a", 1), ("a", 1)]


to_dict(params)
---------------
Convert a list of parameters to a dictionary.

=========== ======================== ===============================================================
Parameter   Type                     Description
=========== ======================== ===============================================================
params      *list[tuple[str, Any]]*  A list of parameters.
=========== ======================== ===============================================================

Return
      *dict* A dictionary where key is param name.


vpath
=====
Helpers for path processing.

get_files(root, ext)
--------------------
Get paths to files with interested extension in root directory.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
root        *str*  Root directory to search for files with required extension.
ext         *str*  Extension, end of file name.
=========== ====== =================================================================================

Return
      *List[str]* A list of paths with required extension.


from_dict(params_d)
-------------------
Convert a dictionary to a list of parameters.



vre
===
Helpers for regex processing.


between(text, start, end, w_start, w_end, strict)
-------------------------------------------------
Find all substrings between the start and end regexes.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
text        *str*  Text where need to find start and end.
start       *str*  Regex of start.
end         *str*  Regex of end.
w_start     *bool* True  - Returns text with matched start text, False - (default) Returns text without matched start text.
w_end       *bool* True  - Returns text with matched end text, False - (default) Returns text without matched end text.
strict      *bool* True  - Raises ValueError if absent start or end, False - Returns empty string if absent start or end.
=========== ====== =================================================================================

Return
      *str* Text between start and end.

.. code:: python

    from vhelpers import vre

    TEXT = "a1\nb2\nc3\nd4"
    assert vre.between(text=TEXT, start="b2", end="c3", w_start=True, w_end=True) == "b2\nc3"


find1(pattern, string, flags)
-----------------------------
Parse 1 item using findall. 1 group with parentheses in pattern is required. If nothing is found,
return 1 empty string.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
pattern     *str*  The regular expression pattern to search for.
string      *str*  The string to search within.
flags       *int*  Optional flags to modify the behavior of the search.
=========== ====== =================================================================================

Return
      *str* The interested substring, or an empty string if nothing is found.

.. code:: python

    from vhelpers import vre

    assert vre.find1(pattern="a(b)cde", string="abcde") == "b"
    assert vre.find1(pattern="a(b)cde", string="acde") == ""


find2(pattern, string, flags)
-----------------------------
Parse 2 items using findall. 2 groups with parentheses in pattern is required. If nothing is found,
return 2 empty strings.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
pattern     *str*  The regular expression pattern.
string      *str*  The string to search within.
flags       *int*  Optional flags to modify the behavior of the search.
=========== ====== =================================================================================

Return
      *Tuple[str, str]* A tuple with two interested substrings, or empty strings if nothing is found.


.. code:: python

    from vhelpers import vre

    assert vre.find2(pattern="a(b)(c)de", string="abcde") == ("b", "c")
    assert vre.find2(pattern="a(b)(c)de", string="acde") == ("", "")


find3(pattern, string, flags)
-----------------------------
Parse 3 items using findall. 3 groups with parentheses in pattern is required. If nothing is found,
returns 3 empty strings.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
pattern     *str*  The regular expression pattern.
string      *str*  The string to search within.
flags       *int*  Optional flags to modify the behavior of the search.
=========== ====== =================================================================================

Return
      *Tuple[str, str, str]* A tuple with three interested substrings, or empty strings if nothing is found.

.. code:: python

    from vhelpers import vre

    assert vre.find3(pattern="a(b)(c)(d)e", string="abcde") == ("b", "c", "d")
    assert vre.find3(pattern="a(b)(c)(d)e", string="acde") == ("", "", "")


find4(pattern, string, flags)
-----------------------------
Parse 4 items using findall. 4 groups with parentheses in pattern is required. If nothing is found,
return 4 empty strings.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
pattern     *str*  The regular expression pattern.
string      *str*  The string to search within.
flags       *int*  Optional flags to modify the behavior of the search.
=========== ====== =================================================================================

Return
      *Tuple[str, str, str, str]* A tuple with three interested substrings, or empty strings if nothing is found.

.. code:: python

    from vhelpers import vre

    assert vre.find4(pattern="a(b)(c)(d)(e)", string="abcde") == ("b", "c", "d", "e")
    assert vre.find4(pattern="a(b)(c)(d)(e)", string="acde") == ("", "", "", "")



find1i(pattern, string, flags)
------------------------------
Parse 1 digit using findall. 1 group with parentheses in pattern is required. If nothing is found,
return 0.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
pattern     *str*  The regular expression pattern to search for.
string      *str*  The string to search within.
flags       *int*  Optional flags to modify the behavior of the search.
=========== ====== =================================================================================

Return
      *int* The interested integer, or 0 if nothing is found.

.. code:: python

    from vhelpers import vre

    assert vre.find1i(pattern="a([0-9]+)b", string="a123b") == 123
    assert vre.find1i(pattern="a([0-9]+)b", string="ab") == 0


find2i(pattern, string, flags)
------------------------------
Parse 2 digits using findall. 2 groups with parentheses in pattern is required. If nothing is found,
return tuple of 0.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
pattern     *str*  The regular expression pattern to search for.
string      *str*  The string to search within.
flags       *int*  Optional flags to modify the behavior of the search.
=========== ====== =================================================================================

Return
      *T2Int* The interested integers, or tuple of 0 if nothing is found.

.. code:: python

    from vhelpers import vre

    assert vre.find2i(pattern="a([0-9])b([0-9])c", string="a1b2c") == (1, 2)
    assert vre.find2i(pattern="a([0-9])b([0-9])c", string="a1bc") == (0, 0)


find1s(patterns, string, flags)
-------------------------------
Parse 1st item that match one of regex in patterns. 1 group with parentheses in pattern is required.
If nothing is found, return 1 empty string.

=========== ======== ===============================================================================
Parameter   Type     Description
=========== ======== ===============================================================================
patterns    *SeqStr* The list of regular expression patterns to search for.
string      *str*    The string to search within.
flags       *int*    Optional flags to modify the behavior of the search.
=========== ======== ===============================================================================

Return
      *str* The interested substring, or an empty string if nothing is found.

.. code:: python

    from vhelpers import vre

    assert vre.find1s(patterns=["a(a)cde", "a(b)cde"], string="abcde") == "b"


ip(string)
----------
Parse 1st IP address from string. If nothing is found, returns an empty string.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
string      *str*  String where need to find IP address.
=========== ====== =================================================================================

Return
      *str* IP address.

.. code:: python

    from vhelpers import vre

    assert vre.ip("text 10.0.0.1/24 10.0.0.2/24 text") == "10.0.0.1"


prefix(string)
--------------
Parse 1st prefix from string. If nothing is found, returns an empty string.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
string      *str*  String where need to find prefix.
=========== ====== =================================================================================

Return
      *str* Prefix.

.. code:: python

    from vhelpers import vre

    assert vre.prefix("text 10.0.0.1/24 10.0.0.2/24 text") == "10.0.0.1/24"


vstr
====

join(args)
----------
Join args by delimiter that is first argument, skipping empty strings.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
args        list   Items that need to be joined.
=========== ====== =================================================================================

Return
      *str* Joined line.

.. code:: python

    from vhelpers import vstr

    assert vstr.join(",", " a ", " ", 0, 1) == "a,0,1"


join_lines(args)
----------------
Join args by '\n' character, skipping empty strings.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
args        list   Items that need to be joined.
=========== ====== =================================================================================

Return
      *str* Joined line.

.. code:: python

    from vhelpers import vstr

    assert vstr.join_lines(" a ", " ", 0, 1) == "a\n0\n1"


repr_info(args, kwargs)
-----------------------
Create info without qutes for the __repr__() method.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
args               The positional arguments.
kwargs             The keyword arguments.
=========== ====== =================================================================================

Return
      *str* A string representation of the parameters.

.. code:: python

    from vhelpers import vstr

    assert vstr.repr_params("a", "b", c="c", d="d") == "a, b, c=c, d=d"


repr_params(args, kwargs)
-------------------------
Create parameters for the __repr__() method.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
args               The positional arguments.
kwargs             The keyword arguments.
=========== ====== =================================================================================

Return
      *str* A string representation of the parameters.

.. code:: python

    from vhelpers import vstr

    assert vstr.repr_params("a", "b", c="c", d="d") == "'a', 'b', c='c', d='d'"


reverse(line)
-------------
Reverse the characters in a string.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
line        *str*  The input string.
=========== ====== =================================================================================

Return
      *str* The reversed string.

.. code:: python

    from vhelpers import vstr

    assert vstr.reverse("abc") == "cba"


split_idx(text, idx)
--------------------
Split the text at the specified index.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
text        *str*  Text to split.
idx         *int*  Index at which to split the text.
=========== ====== =================================================================================

Return
      *Tuple[str, str]* Tuple containing the text before the index and the text after the index.

.. code:: python

    from vhelpers import vstr

    assert vstr.split_idx(text="before_after", idx=7) == ("before_", "after")


vyml
====
Helpers for YAML processing.


host_cmds(items)
----------------
Create commands in YAML format. Where the hostname is the key and the list of commands is the value.

=========== ======================================== ===============================================
Parameter   Type                                     Description
=========== ======================================== ===============================================
items       *List[Tuple[str, str, Union[str, List]*  List of tuples that contain: hostname, parent command, children commands.
=========== ======================================== ===============================================

Return
      *str* YAML formatted commands.

.. code:: python

    from vhelpers import vyml

    items = [("router1", "interface Ethernet1/1", ["description text", "shutdown"])]
    result = """
    ---
    router1: |
     interface Ethernet1/1
      description text
      shutdown
    """.strip()
    assert vyml.host_cmds(items) == result


cmd_cmds(cmd, cmds)
-------------------
Join parent command and children commands using indentation.

=========== ================== =====================================================================
Parameter   Type               Description
=========== ================== =====================================================================
cmd         *str*              Parent command.
cmds        *Union[str, List]* Children commands.
=========== ================== =====================================================================

Return
      *str* YAML formatted commands with indentation.

.. code:: python

    from vhelpers import vyml

    result = """ interface Ethernet1/1\n  description text\n  shutdown"""
    assert vyml.cmd_cmds(cmd="interface Ethernet1/1", cmds=["description text", "shutdown"]) == result


.. _`./examples`: ./examples
