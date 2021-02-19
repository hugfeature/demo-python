# author:丑牛
# datetime:2020/9/24 14:16
import redis
import threading

locks = threading.local()
locks.redis = {}


def key_for(use_id):
    return "account_{}".format(use_id)


def _lock(client, key):
    return bool(client.set(key, True, nx=True, ex=5))


def _unlock(client, key):
    client.delete(key)


def lock(client, user_id):
    key = key_for(user_id)
    if key in locks.redis:
        locks.redis[key] += 1
        return True
    ok = _lock(client, key)
    if not ok:
        return False
    locks.redis[key] = 1
    return True


def unlock(client, user_id):
    key = key_for(user_id)
    if key in locks.redis:
        locks.redis[key] -= 1
        if locks.redis[key] <= 0:
            del locks.redis[key]
        return True
    return False


clinet = redis.StrictRedis()
print("lock", lock(clinet, "codehole"))
print("lock", lock(clinet, "codehole"))
print("unlock", unlock(clinet, "codehole"))
print("unlock", unlock(clinet, "codehole"))