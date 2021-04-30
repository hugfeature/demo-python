# author:丑牛
# datetime:2020/6/18 13:51
import json
import multiprocessing
import random
import time
import kafka
import datetime
# from dateutil.relativedelta import relativedelta
from kafka.errors import KafkaError


def kafka_producer(host, topic):
    """
    向kafka循环发送消息
    :param host:
    :param topic:
    :return:
    """
    producer = kafka.KafkaProducer(bootstrap_servers=host)
    try:
        n = 1
        while True:
            # msg_time = datetime.datetime.now() + relativedelta(years=1, month=8, day=26)
            msg_time = datetime.datetime.now().timestamp() * 1000
            value = random.randint(0, 9999)
            # value_type = ["L", "B", "S", "F"]
            msg = {'ns': "test_KAFKA", 'id': "26000101000100010001000101" + "%04d" % n,
                   't': int(msg_time), 'v': str(value), 'vt': 'L',
                   'c': "001001", 'u': n, 's': 1, 'it': int(msg_time)}
            n = n + 1
            if n == 100:
                n = 1
            send_msg = json.dumps(msg)
            producer.send(topic, send_msg.encode())
            time.sleep(0.0004)
    except KafkaError as e:
        print(e)
    finally:
        producer.close()
        print('done')


if __name__ == "__main__":
    hosts = "192.168.175.234:9092,192.168.175.235:9092,192.168.175.236:9092"
    topic_name = "wzx_test"
    p0 = multiprocessing.Process(target=kafka_producer, args=(hosts, topic_name))
    # p1 = multiprocessing.Process(target=kafka_producer, args=(hosts, topic_name))
    p0.start()
    # p1.start()
    print("The number of CPU is %d:" % (multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("子进程名称：%s，子进程pid：%d" % (p.name, p.pid))
