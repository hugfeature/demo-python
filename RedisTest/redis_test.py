# author:丑牛
# datetime:2020/7/24 10:34
import redis


def redis_con(cluster_ip):
    connect = redis.Redis(host=cluster_ip, port=6379)
    return connect


if __name__ == "__main__":
    host = "127.0.0.1"
    con = redis_con(host)
    a=con.keys()
    print(a)
