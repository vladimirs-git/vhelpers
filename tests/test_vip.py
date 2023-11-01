"""Unittests vip.py."""
from typing import Any

import pytest

from vhelpers import vip
from vhelpers.types_ import TList


@pytest.mark.parametrize("address, expected", [
    ("10.0.0.1 255.255.255.0", "10.0.0.1/24"),
    ("10.0.0.1", ValueError),
    ("", ValueError),
    ("typo", ValueError),
])
def test__ip_prefixlen(address: str, expected: Any):
    """vip.ip_prefixlen()"""
    if isinstance(expected, str):
        actual = vip.ip_prefixlen(address=address)
        assert actual == expected
    else:
        with pytest.raises(expected):
            vip.ip_prefixlen(address=address)


@pytest.mark.parametrize("ips, expected", [
    ([], []),
    (["10.0.0.1 255.255.255.0"], ["10.0.0.1/24"]),
    ({"10.0.0.1 255.255.255.0"}, ["10.0.0.1/24"]),
    (["10.0.0.1"], ValueError),
    ("10.0.0.1 255.255.255.0", ValueError),
])
def test__ips_prefixlen(ips: Any, expected: Any):
    """vip.ips_prefixlen()"""
    if isinstance(expected, TList):
        actual = vip.ips_prefixlen(addresses=ips)
        assert actual == expected
    else:
        with pytest.raises(expected):
            vip.ips_prefixlen(addresses=ips)
