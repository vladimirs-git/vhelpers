
vhelpers
========

Often used functions in vladimirs-git projects.

.. contents::


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

    pip install https://github.com/vladimirs-git/vhelpers/archive/refs/tags/0.1.2.tar.gz

or install the package from github.com repository

.. code:: bash

    pip install git+https://github.com/vladimirs-git/vhelpers


Usage
-----
For easy navigation, functions are grouped by some key concept, mostly based on their return data type.
For more details, please refer to the `./examples`_ directory where you will find numerous examples.


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


vlist
=====
Helpers for list processing.


from_any(items)
---------------
Convert the input items into a list.
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
    assert vlist.from_any(items=(1, 2)) == [1, 2]
    # Otherwise, create a list with the value as its first item.
    assert vlist.from_any(items=1) == [1]
    # If items is None return an empty list.
    assert vlist.from_any(items=None) == []



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

    import vhelpers

    # Remove duplicates from a list of items.
    assert vlist.no_dupl(items=[1, 2, 1]) == [1, 2]


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


.. _`./examples`: ./examples
