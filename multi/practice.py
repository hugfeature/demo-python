# author:丑牛
# datetime:2021/4/30 8:43
"""多线程多进程模拟执行效率"""
import math
import time
from multiprocessing import Pool
from threading import Thread


def simulation_IO(a):
    """模拟IO操作"""
    time.sleep(3)


def simulation_compute(a):
    """模拟计算密集型任务"""
    for i in range(int(1e7)):
        math.sin(40) + math.cos(40)
    return


def normal_func(func):
    """普通方法执行效率"""
    for i in range(6):
        func(i)
    return


def mp(func):
    """进程池中的map方法"""
    with Pool(processes=6) as p:
        res = p.map(func, list(range(6)))
    return


def asy(func):
    """进程池中的异步执行"""
    with Pool(processes=6) as p:
        result = []
        for j in range(6):
            a = p.apply_async(func, args=(j, ))
            result.append(a)
        res = [j.get() for j in result]


def thread(func):
    """多线程方法"""
    threads = []
    for j in range(6):
        t = Thread(target=func, args=(j, ))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def showtime(f, func, name):
    """
    计算并展示函数的运行时间
    :param f: 多进程和多线程的方法
    :param func: 多进程和多线程方法中需要传入的函数
    :param name: 方法的名字
    :return:
    """
    start_time = time.time()
    f(func)
    print(f"{name} time: {time.time() - start_time:.4f}s")


def main(func):
    """
    运行程序的主函数
    :param func: 传入需要计算时间的函数名
    """
    showtime(normal_func, func, "normal")
    print()
    print("------ 多进程 ------")
    showtime(mp, func, "map")
    showtime(asy, func, "async")
    print()
    print("----- 多线程 -----")
    showtime(thread, func, "thread")


if __name__ == "__main__":
    print("------------ 计算密集型 ------------")
    func = simulation_compute
    main(func)
    print()
    print()
    print()
    print("------------ IO 密集型 ------------")
    func = simulation_IO
    main(func)

