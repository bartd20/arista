import yaml
from pprint import pprint

def read_yaml(filename):
    f = open(filename)
    device = yaml.load(f)
    f.close()
    return device


def print_out(output):
    arp_table = []
    for elem in output[0]["result"]["ipV4Neighbors"]:
        ip_addr = elem["address"]
        mac_addr = elem["hwAddress"]
        mapping = {
            "ip_addr": ip_addr,
            "mac_addr": mac_addr
        }
        arp_table.append(mapping)   
    pprint(arp_table)

