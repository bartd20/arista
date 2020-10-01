import pyeapi
from pprint import pprint
import yaml
from my_funcs import read_yaml,print_out

yaml_device = read_yaml("device.yaml")

connection = pyeapi.client.connect(**yaml_device)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

print_out(output)

