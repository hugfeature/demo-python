# author:丑牛
# datetime:2020/9/25 14:50
import redis


client = redis.StrictRedis()
client.delete('codehole')
for i in range(10000):
    client.execute_command('bf.add', 'codehoel', 'user%d' % i)
    ret = client.execute_command('bf.exits', 'codehole', 'user%d' % i)
    if ret == 0:
        print(i)
        break