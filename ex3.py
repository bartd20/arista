import pyeapi
from pprint import pprint
import yaml
from my_funcs import read_yaml

yaml_device = read_yaml("device.yaml")

connection = pyeapi.client.connect(**yaml_device)
device = pyeapi.client.Node(connection)
output = device.enable("show ip route")

route_table = []
routes = output[0]["result"]["vrfs"]["default"]["routes"].items()

for k,v in routes:
    route = k
    route_type = v["routeType"]
    if route_type == "static":
        next_hop = v["vias"][0]["nexthopAddr"]
    else: 
        next_hop = "connected"
    entry = {
        "route": route,
        "route_type": route_type,
        "next_hop": next_hop
    }
    route_table.append(entry)

pprint(route_table)

