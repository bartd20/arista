import pyeapi
from pprint import pprint
import yaml
from my_funcs import read_yaml
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

yaml_devices = read_yaml("devices.yaml")

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

template_file = 'ex4.j2'
template = env.get_template(template_file)

arista_devs = yaml_devices.keys()

for elem in arista_devs:
    arista_output = template.render(**yaml_devices[elem]["data"])
    cmds = arista_output.splitlines()
    
    connection = pyeapi.client.connect(**yaml_devices[elem])
    device = pyeapi.client.Node(connection)
    device.config(cmds)
    output = device.enable("show ip interface brief")
    pprint(output)

