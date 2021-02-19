# author:丑牛
# datetime:2020/5/17 10:23
import hazelcast


def connect(host_list):
    """
    建立hazelcast连接
    """
    config = hazelcast.ClientConfig()
    config.group_config.name = "dev"
    # config.set_property(ClientProperties.INVOCATION_TIMEOUT_SECONDS.name, -1)
    for host in host_list:
        config.network_config.addresses.append(host)
    client = hazelcast.HazelcastClient(config)
    return client


def read_map_key(host_list, map_name):
    """
    获取map中所有的key并写入本地文件
    :param host_list:
    :param map_name:
    :return:
    """
    client = connect(host_list)
    map_read = client.get_map(map_name)
    # print(map_read.size().result())
    keys = map_read.key_set().result()
    # file = open("test.txt", "w+")
    for key in keys:
        # file.writelines(key + '\n')
        print(key)
    # file.close()
    client.shutdown()
    return keys


def get_map_list(host_list):
    """
    获取hazelcast所有的对象
    :param host_list:
    :return:
    """
    client = connect(host_list)
    maps = client.get_distributed_objects()
    print(maps)
    return maps


def remove_map(host_list, map_name):
    """
    删除某个map
    :param host_list:
    :param map_name:
    :return:
    """
    client = connect(host_list)
    map_remove = client.get_map(map_name)
    map_remove.destroy()
    print(map_name + "被删除")


def read_map_key_value(host_list, map_name):
    """
    获取所有的key-value以{}->{}方式打印
    :param host_list:
    :param map_name:
    :return:
    """
    client = connect(host_list)
    map_read = client.get_map(map_name).blocking()
    keys = map_read.entry_set()
    for key, value in keys:
        print("{} -> {}".format(key, value))
    client.shutdown()
    return keys


def read_map_value(host_list, map_name):
    """
    获取所有的value并写入本地文件
    :param host_list:
    :param map_name:
    :return:
    """
    client = connect(host_list)
    map_read = client.get_map(map_name)
    values = map_read.values().result()
    print(values)
    # file = open("test_value.txt", "w+")
    for value in values:
        # file.writelines(value + '\n')
        print(value)
    # file.close()
    client.shutdown()
    return values


def read_key_value(host_list, map_name, key_name):
    """
    获取某个key的value
    :param host_list:
    :param map_name:
    :param key_name:
    :return:
    """
    client = connect(host_list)
    map_read = client.get_map(map_name)
    value = map_read.get(key_name).result()
    print(value)
    return value


def put_map(host_list, map_name, key,value):
    client = connect(host_list)
    map_put = client.get_map(map_name)
    map_put.put(key, value)




