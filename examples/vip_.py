"""Examples vip.py."""
from vhelpers import vip

# Convert IPv4 address with mask to address with prefix length.
assert vip.ip_prefixlen(address="10.0.0.1 255.255.255.0") == "10.0.0.1/24"
assert vip.ips_prefixlen(addresses=["10.0.0.1 255.255.255.0"]) == ["10.0.0.1/24"]
