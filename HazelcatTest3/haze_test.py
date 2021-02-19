# author:丑牛
# datetime:2020/5/17 13:27
from HazelcatTest3 import hazelcast3

if __name__ == "__main__":
    host_list = ["192.168.175.234:5701", "192.168.175.235:5701", "192.168.175.236:5701"]
    map_name = "37082600014020001008"
    hazelcast3.read_map_key_value(host_list, map_name)
    # hazelcast3.remove_map(host_list, "<37082600014020001005>")
