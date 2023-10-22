"""Unittests dict_.py."""
import pytest

from tests import params_dict_ as params
from vhelpers import dict_


@pytest.mark.parametrize("key, data, expected", params.POP_D)
def test_pop_d(key, data, expected):
    """pop_d."""
    actual = dict_.pop_d(key=key, data=data)
    assert actual == expected


@pytest.mark.parametrize("params_d, expected", params.DICT_TO_PARAMS)
def test_dict_to_params(params_d, expected):
    """dict_to_params."""
    actual = dict_.dict_to_params(params_d=params_d)
    assert actual == expected


@pytest.mark.parametrize("params_, expected", params.PARAMS_TO_DICT)
def test_params_to_dict(params_, expected):
    """params_to_dict."""
    actual = dict_.params_to_dict(params=params_)
    assert actual == expected
