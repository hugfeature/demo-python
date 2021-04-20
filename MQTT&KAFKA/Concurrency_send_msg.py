# author:丑牛
# datetime:2020/12/29 16:53
import datetime
import multiprocessing

import kafka_msg
import mqtt_msg

num = 100


def sendKafkaMsg():
    pool = multiprocessing.Pool(1)
    # 云侧
    # kafka_hosts = "192.168.175.234:9092,192.168.175.235:9092,192.168.175.236:9092"
    # 边缘侧
    kafka_hosts = "192.168.175.228:9092,192.168.175.228:9093,192.168.175.228:9094"
    for i in range(num):
        # 云侧
        # topic = "whl_test"
        # 边缘侧
        topic = "wzx_test"
        pool.apply_async(func=kafka_msg.kafka_producer, args=(kafka_hosts, topic))
    pool.close()
    pool.join()


def sendMqttMsg():
    pool = multiprocessing.Pool(1)
    mqtt_hosts = '192.168.175.228'
    for i in range(num):
        # client = "wzxtest" + str(i)
        # topic = "/zmj/test" + str(i)
        client = "wzxtest"
        topic = "pingmeijituan/shoushanyikuang/zstest"
        pool.apply_async(func=mqtt_msg.send_edge, args=(client, mqtt_hosts, topic))
    pool.close()
    pool.join()


if __name__ == "__main__":
    time_start = datetime.datetime.now().timestamp()
    multiprocessing.Process(target=sendMqttMsg).start()
    # multiprocessing.Process(target=sendKafkaMsg).start()
    for p in multiprocessing.active_children():  # 循环打印子进程的名称和pid
        print("子进程名称：%s，子进程pid：%d" % (p.name, p.pid))
    print("ending....")
    time_end = datetime.datetime.now().timestamp()
    print('耗时：' + str(time_end - time_start) + '秒')
