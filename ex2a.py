import pyeapi
from pprint import pprint
import yaml

arp_table = []

f = open("device.yaml")
yaml_device = yaml.load(f)
f.close()

connection = pyeapi.client.connect(**yaml_device)

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
