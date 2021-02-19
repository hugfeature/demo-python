# author:丑牛
# datetime:2020/12/29 16:53
import datetime
import multiprocessing

import KAFKA消息发送
import MQTT消息发送

num = 100


def sendKafkaMsg():
    pool = multiprocessing.Pool(num)
    kafka_hosts = "192.168.175.234:9092,192.168.175.235:9092,192.168.175.236:9092"
    for i in range(num):
        topic = "wzx_test" + str(i)
        pool.apply_async(func=KAFKA消息发送.kafka_producer, args=(kafka_hosts, topic))
    pool.close()
    pool.join()


def sendMqttMsg():
    pool = multiprocessing.Pool(num)
    mqtt_hosts = '192.168.175.228'
    for i in range(num):
        client = "wzxtest" + str(i)
        topic = "/zmj/test" + str(i)
        pool.apply_async(func=MQTT消息发送.send, args=(client, mqtt_hosts, topic))
    pool.close()
    pool.join()


if __name__ == "__main__":
    time_start = datetime.datetime.now().timestamp()
    print(time_start)
    multiprocessing.Process(target=sendMqttMsg).start()
    multiprocessing.Process(target=sendKafkaMsg).start()
    # kafka_hosts = "192.168.175.234:9092,192.168.175.235:9092,192.168.175.236:9092"
    # kafka_topic = ["wzx_test0", "wzx_test1", "wzx_test2", "wzx_test3", "wzx_test4",
    #                "wzx_test5", "wzx_test6", "wzx_test7", "wzx_test8", "wzx_test9"]
    # mqtt_hosts = '192.168.175.228'
    # mqtt_topic = ["/zmj/test0", "/zmj/test1", "/zmj/test2", "/zmj/test3", "/zmj/test4",
    #               "/zmj/test5", "/zmj/test6", "/zmj/test7", "/zmj/test8", "/zmj/test9"]
    # p0 = multiprocessing.Process(target=KAFKA消息发送.kafka_producer, args=(kafka_hosts, kafka_topic[0]))
    # p1 = multiprocessing.Process(target=MQTT消息发送.send, args=(mqtt_hosts, mqtt_topic[0]))
    # p0.start()
    # p1.start()
    for p in multiprocessing.active_children():  # 循环打印子进程的名称和pid
        print("子进程名称：%s，子进程pid：%d" % (p.name, p.pid))
    print("ending....")
    time_end = datetime.datetime.now().timestamp()
    print('耗时：' + str(time_end - time_start) + '秒')
