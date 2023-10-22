
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

    pip install https://github.com/vladimirs-git/vhelpers/archive/refs/tags/0.1.0.tar.gz

or install the package from github.com repository

.. code:: bash

    pip install git+https://github.com/vladimirs-git/vhelpers


Usage
-----
For easy navigation, functions are grouped by some key concept, mostly based on their return data type.
For more details, please refer to the `./examples`_ directory where you will find numerous examples.

dict_
=====


pop_d(key, data)
----------------
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

    import vhelpers

    data = {1: "a", 2: "b"}
    assert vhelpers.pop_d(key=1, data=data) == "a"
    assert data == {2: "b"}
    assert vhelpers.pop_d(key=3, data=data) is None
    assert data == {2: "b"}


dict_to_params(params_d)
------------------------
Convert a dictionary to a list of tuples.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
params_d    *dict* A dictionary with keys and values.
=========== ====== =================================================================================

Return
      *list[tuple[str, any]* A list of tuples. If params_d is empty, returns an empty list.

.. code:: python

    import vhelpers

    assert vhelpers.dict_to_params(params_d={"a": [1, 1]}) == [("a", 1), ("a", 1)]


params_to_dict(params)
----------------------
Convert a list of tuples to a dictionary.  If the key already exists in the dictionary and its value
is a list, the new value will be appended to the list. If the key already exists in the dictionary
and its value is not a list, the new value will replace the existing value.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
params      *list* A list of tuples.
=========== ====== =================================================================================

Return
      *dict* A dictionary with keys and values.

.. code:: python

    import vhelpers

    assert vhelpers.params_to_dict(params=[("a", 1), ("a", 1)]) == {"a": [1, 1]}


list_
=====


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

    assert vhelpers.no_dupl(items=[1, 2, 1]) == [1, 2]


to_list(items)
--------------
Convert the input items into a list.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
items       *Any*  The items to be converted into a list.
=========== ====== =================================================================================

Return
      *list* The converted list x.

.. code:: python

    import vhelpers

    assert vhelpers.to_list(items=(1, 2)) == [1, 2]
    assert vhelpers.to_list(items=None) == []
    assert vhelpers.to_list(items=1) == [1]


str_
====


findall1(pattern, string, flags)
--------------------------------
Parse the first item of re.findall.  Group with parentheses in pattern is required. If nothing is
found, return 1 empty string.

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

    import vhelpers

    assert vhelpers.findall1(pattern="a(b)cde", string="abcde") == "b"

findall2(pattern, string, flags)
--------------------------------
Parse 2 items of re.findall(). Group with parentheses in pattern is required. If nothing is found,
return 2 empty strings.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
pattern     *str*  The regular expression pattern.
string      *str*  The string to search within.
flags       *int*  Optional flags to modify the behavior of the search.
=========== ====== =================================================================================

Return
      *tuple[str, str]* A tuple with two interested substrings, or empty strings if nothing is found.

.. code:: python

    import vhelpers

    assert vhelpers.findall2(pattern="a(b)(c)de", string="abcde") == ("b", "c")


findall3(pattern, string, flags)
--------------------------------
Parse 3 items of re.findall(). Group with parentheses in pattern is required. If nothing is found,
returns 3 empty strings.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
pattern     *str*  The regular expression pattern.
string      *str*  The string to search within.
flags       *int*  Optional flags to modify the behavior of the search.
=========== ====== =================================================================================

Return
      *tuple[str, str, str]* A tuple with three interested substrings, or empty strings if nothing is found.

.. code:: python

    import vhelpers

    assert vhelpers.findall3(pattern="a(b)(c)(d)e", string="abcde") == ("b", "c", "d")


findall4(pattern, string, flags)
--------------------------------
Parse 4 items of re.findall(). Group with parentheses in pattern is required. If nothing is found,
return 4 empty strings.

=========== ====== =================================================================================
Parameter   Type   Description
=========== ====== =================================================================================
pattern     *str*  The regular expression pattern.
string      *str*  The string to search within.
flags       *int*  Optional flags to modify the behavior of the search.
=========== ====== =================================================================================

Return
      *tuple[str, str, str, str]* A tuple with three interested substrings, or empty strings if nothing is found.

.. code:: python

    import vhelpers

    assert vhelpers.findall4(pattern="a(b)(c)(d)(e)", string="abcde") == ("b", "c", "d", "e")


.. _`./examples`: ./examples
