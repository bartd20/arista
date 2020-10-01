import pyeapi
from pprint import pprint

arp_table = []

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password="PASSWORD",
    port="443"
)

device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

for elem in output[0]["result"]["ipV4Neighbors"]:
    ip_addr = elem["address"]
    mac_addr = elem["hwAddress"]
    mapping = {
        "ip_addr": ip_addr,
        "mac_addr": mac_addr
    }
    arp_table.append(mapping)

pprint(arp_table)
