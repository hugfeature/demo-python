# author:丑牛
# datetime:2020/5/17 14:41
import json
import random
import time
import kafka
import datetime
from dateutil.relativedelta import relativedelta
from kafka.errors import KafkaError


def kafka_topic_list(hosts):
    """
    获取kafka中所有的topic
    :param hosts:
    :return:
    """
    clien = kafka.KafkaConsumer(bootstrap_servers=hosts)
    topic_list = clien.topics()
    print(topic_list)
    clien.close()


def kafka_producer_circulate(hosts, topic_name):
    """
    向kafka循环发送
    :param hosts:
    :param topic_name:
    :return:
    """
    producer = kafka.KafkaProducer(bootstrap_servers=hosts)
    topic = topic_name
    try:
        id_n = 1
        time_m = 0
        num = 0
        while True:
            msg_time = datetime.datetime.now() + relativedelta(years=1, month=8, day=1)
            # msg_time = 1627747201000 + time_m * 1000 * 1000  # 2021年8月
            value = random.randint(0, 9999)
            value_type = ["L", "B", "S", "F"]
            # msg_time1 = 1609516801000 + time_m * 1000 * 1000
            # msg = {'Value': value, 'SysCode': "13000010", 'ChannelCode': "001001",
            #        'DeviceCode': "000100010001" + "%04d" % id_n, 'DataID': "010001", 'UpdateCount': id_n, 'State': 1,
            #        'Timestamp': int(msg_time.timestamp() * 1000)}
            # 'vt': random.choice(value_type)
            msg = {'ns': "111000", 'id': "16000010000100010001" + "%04d" % id_n + "010001",
                   't': int(msg_time.timestamp() * 1000), 'v': str(value), 'vt': "F",
                   'c': "001001", 'u': id_n, 's': 1, 'it': int(time.time() * 1000)}
            id_n = id_n + 1
            num = num + 1
            send_msg = "[" + json.dumps(msg) + "]"
            producer.send(topic, send_msg.encode())
            if id_n == 201:
                id_n = 1
                time_m = time_m + 1
            if num == 200000:
                break
            # time.sleep(0.0001)
    except KafkaError as e:
        print(e)
    finally:
        producer.close()
        print('done')


def kafka_producer(hosts, topic_name, msg):
    """
    向kafka中生产消息
    :param hosts:
    :param topic_name:
    :param msg:
    :return:
    """
    producer = kafka.KafkaProducer(bootstrap_servers=hosts)
    producer.send(topic_name, msg)
    producer.close()
    print("生产者发送消息完成")


def kafka_consumer(hosts, topic_name):
    """
    读取kafka中消费者的消息
    :param hosts:
    :param topic_name:
    :return:
    """
    consumer = kafka.KafkaConsumer(topic_name, bootstrap_servers=hosts)
    for msg in consumer:
        print(msg)
        print(msg.value)
        # print("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value))


def kafka_consumer_save(hosts, topic_name):
    """
    读取kafka消息并保存至本地文件
    :param hosts:
    :param topic_name:
    :return:
    """
    consumer = kafka.KafkaConsumer(topic_name, bootstrap_servers=hosts)
    file_name = topic_name + ".txt"
    file = open(file_name, "w+")
    for msg in consumer:
        # print(msg.value)
        file.write(str(msg.value) + '\n')
    file.close()
