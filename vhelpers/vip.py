"""Helpers for ip addresses processing."""

from ipaddress import IPv4Network

from vhelpers.types_ import LStr, SeqStr


def ip_prefixlen(address: str) -> str:
    """Convert IPv4 address with mask to address with prefix length.

    :param address: IP addresses with mask.
    :return: IP addresses with prefix length.
    :example:
        ip_prefixlen("10.0.0.1 255.255.255.0") -> "10.0.0.1/24"
    """
    ip, mask = address.split()
    network = IPv4Network(f"{ip}/{mask}", strict=False)
    return f"{ip}/{network.prefixlen}"


def ips_prefixlen(addresses: SeqStr) -> LStr:
    """Convert IPv4 addresses with mask to addresses with prefix length.

    :param addresses: A list of IP addresses with mask.
    :return: A list of IP addresses with prefix length.
    :example:
        ips_prefixlen(["10.0.0.1 255.255.255.0"]) -> ["10.0.0.1/24"]
    """
    ips_: LStr = []
    for address in addresses:
        ip = ip_prefixlen(address)
        ips_.append(ip)
    return ips_
