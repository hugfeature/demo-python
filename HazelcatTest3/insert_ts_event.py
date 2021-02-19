# author:丑牛
# datetime:2020/8/12 14:42
import datetime
import json

import hazelcast
from dateutil.relativedelta import relativedelta

if __name__ == "__main__":
    host_list = ["192.168.175.234:5701", "192.168.175.235:5701", "192.168.175.236:5701"]
    map_name = "test"
    config = hazelcast.ClientConfig()
    config.group_config.name = "dev"
    # config.set_property(ClientProperties.INVOCATION_TIMEOUT_SECONDS.name, -1)
    for host in host_list:
        config.network_config.addresses.append(host)
    client = hazelcast.HazelcastClient(config)
    ts_map = client.get_map(map_name)
    num = 0
    while True:
        msg_time = datetime.datetime.now() + relativedelta(years=1, months=1)
        key = "260001010001000100010090010002"
        value_list = {'id': key, 'c': "001001", 'ns': "test", 'vt': "F",
                      'u': 1, 's': 1, 'v': 1, 't': int(msg_time.timestamp() * 1000)}
        value = json.dumps(value_list)
        ts_map.put(key, value)
        ts_map.size()
