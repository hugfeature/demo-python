# author:丑牛
# datetime:2020/5/20 17:30
import json
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
    host = '127.0.0.1'
    db_password = 'wzx670905'
    connet = postgres.connect(host, db_password)
    # f = open("test_time.csv", "w")
    # n = 0
    for msg in consumer:
        # print(msg.value)
        # f.write(msg.value)
        msg_str = json.loads(msg.value)
        # 转换处理时间
        # time_end = float(msg_str[0]["t"])
        time_end = float(msg_str[0]["it"])
        # 事件发生时间
        # time_start = float(msg_str[0]["Timestamp"])
        # time_use = time_end - time_start
        # insert_sql = "INSERT INTO time(time_end, time_start, time_use) VALUES " \
        #              "(" + str(time_end) + "," + str(time_start) + "," + str(time_use) + ")"
        insert_sql = "INSERT INTO time_kafka(time_end) VALUES " \
                     "(" + str(time_end) + ")"
        postgres.exec_table(connet, insert_sql)
        connet.commit()
        # f.write(str(time_end) + '\t' + str(time_use) + '\n')


if __name__ == "__main__":
    hosts = "192.168.175.234:9092,192.168.175.235:9092,192.168.175.236:9092"
    # hosts = "192.168.175.196:9092, 192.168.175.196:9093, 192.168.175.196:9094"
    # topic_name = "Inner_Ts_Cloud"
    topic_name = "wzx_test"
    # topic_name = "testinner"
    kafka_get_time(hosts, topic_name)
