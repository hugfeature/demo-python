# author:丑牛
# datetime:2021/4/30 8:59
import datetime
from threading import Thread

from KafkaTest import kafka_utils
import multiprocessing
if __name__ == "__main__":
    time_start = datetime.datetime.now().timestamp()
    print(time_start)
    # hosts = "192.168.175.228:9092,192.168.175.228:9093,192.168.175.228:9094"
    hosts = "192.168.175.234:9092,192.168.175.235:9092,192.168.175.236:9092"
    # topic_name = "whl_test"
    topic_name = "wzx_test"
    threads = []
    for i in range(8):
        t = Thread(target=kafka_utils.kafka_producer_circulate, args=(hosts, topic_name))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    # print("The number of CPU is %d:" % (multiprocessing.cpu_count()))     # 打印CPU核数
    # for p in multiprocessing.active_children():         # 循环打印子进程的名称和pid
    #     print("子进程名称：%s，子进程pid：%d" % (p.name, p.pid))
    print("ending....")
    time_end = datetime.datetime.now().timestamp()
    print('耗时：' + str(time_end - time_start) + '秒')
