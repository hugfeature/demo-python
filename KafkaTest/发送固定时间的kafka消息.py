'''
Author: 丑牛
Date: 2021-02-19 11:56:39
LastEditors: 丑牛
LastEditTime: 2021-12-09 16:59:06
Description: file content
'''
# author:丑牛
# datetime:2020/6/15 14:14
import json
import random
import datetime
import time
from dateutil.relativedelta import relativedelta
from kafka import KafkaProducer
from kafka.errors import KafkaError

# producer = KafkaProducer(bootstrap_servers='192.168.175.234:9092,192.168.175.235:9092,192.168.175.236:9092')
producer = KafkaProducer(bootstrap_servers='192.168.175.228:9092,192.168.175.228:9093,192.168.175.228:9094')
# topic = 'wzx'
# topic = 'Inner_Ts_Cloud'
# topic = 'wzxtest'
topic = 'wzx_test1'


def test():
    try:
        id_n = 1
        time_m = 0
        num = 0
        day_date = 10
        while True:
            # msg_time = (datetime.datetime.now() + relativedelta(years=1, month=8, day=day_date)).timestamp() * 1000
            value = random.randint(0, 9999)
            value_type = ["L", "B", "S", "F"]
            # random.choice(value_type)
            # msg_time = 1609517301000 + time_m * 150 * 1000  # 2021年1月
            msg_time = 1638345963000 + num # 2021年8月
            msg_time = random.randint(1638345963000, 1638345964000)
            # 'id': "1500001000010001" + "%08d" % n + "010001"
            msg = {'Value': 1, 'SysCode': "26000101", 'ChannelCode': "001001",
                   'DeviceCode': "000100010001"+ "%04d" % id_n, 'DataID': "010001",
                   'UpdateCount': 10, 'State': 1, 'Timestamp': msg_time}
            # msg = {'ns': "zmjtest", 'id': "19000010000100010001" + "%06d" % id_n + "0001",
            #        't': int(msg_time), 'v': str(num), 'vt': "L",
            #        'c': "001001", 'u': num, 's': 1, 'it': int(time.time() * 1000)}
            print(num)
            id_n = id_n + 1
            num = num + 1
            send_msg = "[" + json.dumps(msg) + "]"
            print(send_msg)
            # send_msg = json.dumps(msg) 
            producer.send(topic, send_msg.encode())
            # if id_n == 201:
            #     id_n = 1
            #     time_m = time_m + 1
            # if day_date == 28:
            #     break
            if num == 10000:
                break
            # time.sleep(0.001)
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
