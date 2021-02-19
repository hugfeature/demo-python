# author:丑牛
# datetime:2020/9/27 13:54
import redis
client = redis.StrictRedis()
for i in range(10000):
    client.set('key%d' % i, i)
