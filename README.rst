
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

    pip install https://github.com/vladimirs-git/vhelpers/archive/refs/tags/0.1.9.tar.gz

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

=========== ========== ===============================================================================
Parameter   Type       Description
=========== ========== ===============================================================================
start       *datetime* The starting datetime object.
end         *datetime* The ending datetime object. If None, the current datetime is used.
=========== ========== ===============================================================================

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

=========== ====== =========================================================================================
Parameter   Type   Description
=========== ====== =========================================================================================
args               The arguments for calculating the time delta.
kwargs             The keyword arguments for calculating the time delta.
=========== ====== =========================================================================================

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


pop(key, data)
--------------
Pop the specified item from the data by key.  If key is absent in data, do nothing and return None.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
key         *str*  The key to be popped from the data.
data        *dict* The data from which the key is to be popped.
=========== ====== =================================================================================

Return
      *str* The popped item if key is present in data, otherwise None.

.. code:: python

    from vhelpers import vdict

    # Pop the specified item from the data by key.
    data = {1: "a", 2: "b"}
    assert vdict.pop(key=1, data=data) == "a"
    assert data == {2: "b"}
    # If key is absent in data, do nothing and return None.
    assert vdict.pop(key=3, data=data) is None
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


vlist
=====
Helpers for list processing.


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

    # Remove duplicates from a list of items.
    assert vlist.no_dupl(items=[1, 2, 1]) == [1, 2]


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
      *LStr* Values without punctuation.

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


to_multi(items, count)
----------------------
Convert a flat list into a multidimensional list. Convert a list with the specified number of items
in each inner list.

=========== ============ ===========================================================================
Parameter   Type         Description
=========== ============ ===========================================================================
items       *list* The   flat list to convert.
count       *Lis[list]*  The number of items to include in each inner list.
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

    # Convert a dictionary to a list of parameters.
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


find_ip(string)
---------------
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

    assert vre.find_ip("text 10.0.0.1/24 10.0.0.2/24 text") == "10.0.0.1"


find_prefix(string)
-------------------
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

    assert vre.find_prefix("text 10.0.0.1/24 10.0.0.2/24 text") == "10.0.0.1/24"


vstr
====

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

    # Create commands in YAML format.
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
