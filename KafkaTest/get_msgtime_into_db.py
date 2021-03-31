# author:丑牛
# datetime:2020/5/20 17:30
import json

import demjson
import kafka

from PostgresqlTest import postgres


def kafka_get_time(host, topic):
    """
    读取kafka中消费者的消息
    :param host:
    :param topic:
    :return:
    """
    consumer = kafka.KafkaConsumer(topic, bootstrap_servers=host)
    # 连接postgresql数据库
    host = '127.0.0.1'
    db_password = 'wzx670905'
    connet = postgres.connect(host, db_password)
    # 写入本地文件
    # f = open("test_time.csv", "w")
    # n = 0
    for msg in consumer:
        # print(msg.value)
        # f.write(msg.value)
        # 解决json loads报错'utf-32-be'
        # print(msg.value)
        str_1 = bytes.decode(msg.value)
        # 解决json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
        msg_str = json.loads(str_1)
        print(msg_str)
        # print(msg_str, print(type(msg_str)))
        # 转换处理时间
        time_end = float(msg_str["it"])
        # 事件发生时间
        time_start = float(msg_str["t"])
        time_use = time_end - time_start
        insert_sql = "INSERT INTO time(time_end, time_start, time_use) VALUES " \
                     "(" + str(time_end) + "," + str(time_start) + "," + str(time_use) + ")"
        # insert_sql = "INSERT INTO time_kafka(time_end) VALUES " \
        #              "(" + str(time_end) + ")"
        postgres.exec_table(connet, insert_sql)
        connet.commit()
        # f.write(str(time_end) + '\t' + str(time_use) + '\n')


if __name__ == "__main__":
    hosts = "192.168.175.234:9092,192.168.175.235:9092,192.168.175.236:9092"
    # hosts = "192.168.175.196:9092, 192.168.175.196:9093, 192.168.175.196:9094"
    # topic_name = "Inner_Ts_Cloud"
    topic_name = "whl_test1"
    # topic_name = "testinner"
    kafka_get_time(hosts, topic_name)
