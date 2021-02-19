# author:丑牛
# datetime:2020/8/14 13:46
import json
import random
import datetime
import time

from dateutil.relativedelta import relativedelta
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers='192.168.175.234:9092,192.168.175.235:9092,192.168.175.236:9092')
topic = 'testinner'


def test():
    try:
        n = 0
        id_n = 0
        while True:
            # msg_time = datetime.datetime.now() + relativedelta(years=1, months=0)
            msg_time = 1631069452963 + n * 30 * 1000
            value_lsit = [100, 199, 299]
            label_list = ['260001010001000100010001010001', '260001010001000100010002010001',
                          '260001010001000100010003010001', '260001010001000100010006010001',
                          '260001010001000100010004010001', '260001010001000100010005010001',
                          '260001010001000100010007010001', '260001010001000100010008010001',
                          '260001010001000100010009010001', '260002010000000000000000040001',
                          '260001010000000000000000040001', '260001040019000100010001010004',
                          '260001040019000100010001010002', '260001010000000000000000020003',
                          '260001010000000000000000000000', '260001020002000100010001050009']
            label = random.choice(label_list)
            if label == '260001010000000000000000040001':
                value = 1
                value_type = "F"
            elif label == '260001010000000000000000020003':
                value = 'true'
                value_type = "B"
            elif label == '260001020002000100010001050009':
                value = '0801'
                value_type = "S"
            else:
                value = random.choice(value_lsit)
                value_type = "F"
            msg = {'ns': "37082600014020001002", 'id': label, 't': msg_time, 'v': str(value),
                   'vt': value_type, 'c': "001001", 'u': 1, 's': 1, 'it': msg_time}
            # msg = {'ns': "37082600014020001002", 'id': "26000101000100010001" + "%04d" % id_n + "010001", 't': msg_time, 'v': random.choice(value_lsit),
            #        'vt': "F", 'c': "001001", 'u': 1, 's': 1, 'it': msg_time}
            send_msg = "[" + json.dumps(msg) + "]"
            producer.send(topic, send_msg.encode())
            n = n + 1
            print(n)
            id_n = id_n + 1
            if id_n == 400:
                id_n = 1
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
