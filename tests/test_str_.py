"""Unittests str_.py."""
import pytest

from tests import params_str_ as params
from vhelpers import str_


@pytest.mark.parametrize("pattern, string, flags, expected", params.FINDALL1)
def test_findall1(pattern, string, flags, expected):
    """findall1."""
    actual = str_.findall1(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, error", params.FINDALL_ERR)
def test_findall1__invalid(pattern, string, flags, error):
    """findall1."""
    with pytest.raises(error):
        str_.findall1(pattern=pattern, string=string, flags=flags)


@pytest.mark.parametrize("pattern, string, flags, expected", params.FINDALL2)
def test_findall2(pattern, string, flags, expected):
    """findall2."""
    actual = str_.findall2(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, error", params.FINDALL_ERR)
def test_findall2__invalid(pattern, string, flags, error):
    """findall2."""
    with pytest.raises(error):
        str_.findall2(pattern=pattern, string=string, flags=flags)


@pytest.mark.parametrize("pattern, string, flags, expected", params.FINDALL3)
def test_findall3(pattern, string, flags, expected):
    """findall3."""
    actual = str_.findall3(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, error", params.FINDALL_ERR)
def test_findall3__invalid(pattern, string, flags, error):
    """findall3."""
    with pytest.raises(error):
        str_.findall3(pattern=pattern, string=string, flags=flags)


@pytest.mark.parametrize("pattern, string, flags, expected", params.FINDALL4)
def test_findall4(pattern, string, flags, expected):
    """findall4."""
    actual = str_.findall4(pattern=pattern, string=string, flags=flags)
    assert actual == expected


@pytest.mark.parametrize("pattern, string, flags, error", params.FINDALL_ERR)
def test_findall4__invalid(pattern, string, flags, error):
    """findall4."""
    with pytest.raises(error):
        str_.findall4(pattern=pattern, string=string, flags=flags)
