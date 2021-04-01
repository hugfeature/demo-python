# author:丑牛
# datetime:2020/12/29 16:32
import json
import random
import datetime
import time

import kafka
from dateutil.relativedelta import relativedelta
from kafka.errors import KafkaError


def kafka_producer(hosts, topic):
    """
    向kafka循环发送
    :param hosts:
    :param topic:
    :return:
    """
    producer = kafka.KafkaProducer(bootstrap_servers=hosts)
    try:
        id_n = 0
        while True:
            # 一个月之前的当天
            # msg_time = datetime.datetime.now() + relativedelta(years=0, months=-1, days=0)
            # 当前时间
            msg_time = datetime.datetime.now()
            value = random.randint(0, 9999)
            label_list = ['260001010001000100010001010001', '260001010001000100010002010001',
                          '260001010001000100010003010001', '260001010001000100010006010001',
                          '260001010001000100010004010001', '260001010001000100010005010001',
                          '260001010001000100010007010001', '260001010001000100010008010001',
                          '260001010001000100010009010001', '260002010000000000000000040001',
                          '260001010000000000000000040001', '260001040019000100010001010004',
                          '260001040019000100010001010002', '260001010000000000000000020003',
                          '260001010000000000000000040005', '260001020002000100010001050009']
            label = random.choice(label_list)
            msg = {'Value': value, 'SysCode': label[0:8], 'ChannelCode': "001001",
                   'DeviceCode': label[8:24], 'DataID': label[24:30], 'UpdateCount': id_n, 'State': 1,
                   'Timestamp': int(msg_time.timestamp() * 1000)}
            id_n = id_n + 1
            send_msg = "[" + json.dumps(msg) + "]"
            producer.send(topic, send_msg.encode())
            # time.sleep(0.0005)
            print(id_n)
            if id_n == 100000:
                break
    except KafkaError as e:
        print(e)
    finally:
        producer.close()
        print('done')
