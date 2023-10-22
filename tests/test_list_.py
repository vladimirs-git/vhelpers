"""Unittests str_.py."""
import pytest

from tests import params_list_ as params
from vhelpers import list_


@pytest.mark.parametrize("items, expected", params.NO_DUPL)
def test_no_dupl(items, expected):
    """no_dupl."""
    actual = list_.no_dupl(items=items)
    assert actual == expected


@pytest.mark.parametrize("items, expected", params.LIST_)
def test_lst(items, expected):
    """lst."""
    actual = list_.to_list(items=items)
    if isinstance(items, set):
        actual.sort()
    assert actual == expected
