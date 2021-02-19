# author:丑牛
# datetime:2020/9/29 8:24
import redis


def key_for(user_id):
    return "account_{}".format(user_id)


def double_account(client, user_id):
    key = key_for(user_id)
    while True:
        client.watch(key)
        value = int(client.get(key))
        value *= 2
        pipe = client.pipeline(transaction=True)
        pipe.multi()
        pipe.set(key, value)
        try:
            pipe.execute()
            break
        except redis.WatchError:
            continue
    return int(client.get(key))


client = redis.StrictRedis()
user_id = "abc"
client.setnx(key_for(user_id), 5)
print(double_account(client, user_id))