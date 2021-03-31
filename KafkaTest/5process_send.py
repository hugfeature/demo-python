# author:丑牛
# datetime:2020/5/18 10:23
import datetime

from KafkaTest import kafka_utils
import multiprocessing
if __name__ == "__main__":
    time_start = datetime.datetime.now().timestamp()
    print(time_start)
    # hosts = "192.168.175.198:9092,192.168.175.198:9093,192.168.175.198:9094"
    hosts = "192.168.175.234:9092,192.168.175.235:9092,192.168.175.236:9092"
    topic_name = "whl_test"
    # topic_name = "testinner"
    p0 = multiprocessing.Process(target=kafka_utils.kafka_producer_circulate, args=(hosts, topic_name))
    p1 = multiprocessing.Process(target=kafka_utils.kafka_producer_circulate, args=(hosts, topic_name))
    p2 = multiprocessing.Process(target=kafka_utils.kafka_producer_circulate, args=(hosts, topic_name))
    p3 = multiprocessing.Process(target=kafka_utils.kafka_producer_circulate, args=(hosts, topic_name))
    p4 = multiprocessing.Process(target=kafka_utils.kafka_producer_circulate, args=(hosts, topic_name))
    p0.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print("The number of CPU is %d:" % (multiprocessing.cpu_count()))     # 打印CPU核数
    for p in multiprocessing.active_children():         # 循环打印子进程的名称和pid
        print("子进程名称：%s，子进程pid：%d" % (p.name, p.pid))
    print("ending....")
    time_end = datetime.datetime.now().timestamp()
    print('耗时：' + str(time_end - time_start) + '秒')
