# author:丑牛
# datetime:2020/8/14 13:46
import json
import random
import datetime
import time

from dateutil.relativedelta import relativedelta
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers='192.168.175.196:9092, 192.168.175.196:9093, 192.168.175.196:9094')
topic = 'wzx'


def test():
    try:
        id_n = 1
        n = 0
        while True:
            msg_time = datetime.datetime.now() + relativedelta(years=1, months=1)
            value_list = [800, 150, 230]
            value = random.choice(value_list)
            # msg = {'Value': value, 'SysCode': "26000101", 'ChannelCode': "001001",
            #        'DeviceCode': "000100010001" + "%04d" % id_n, 'DataID': "010001",
            #        'UpdateCount': 1, 'State': 1, 'Timestamp': int(msg_time.timestamp() * 1000)}
            msg = {'Value': 299, 'SysCode': "26000101", 'ChannelCode': "001001",
                   'DeviceCode': "0000000000000000", 'DataID': "040005",
                   'UpdateCount': 10, 'State': 1, 'Timestamp': int(msg_time.timestamp() * 1000)}
            send_msg = "[" + json.dumps(msg) + "]"
            producer.send(topic, send_msg.encode())
            if id_n == 400:
                id_n = 1
            id_n = id_n + 1
            n = n + 1
            print(n)
            # if n == 10000:
            #     break
            time.sleep(0.0025)
    except KafkaError as e:
        print(e)
    finally:
        producer.close()
        print('done')


if __name__ == '__main__':
    time_start = datetime.datetime.now().timestamp()
    print(time_start)
    test()
    time_end = datetime.datetime.now().timestamp()
    print(time_end)
    print('耗时：' + str(time_end - time_start) + '秒')
