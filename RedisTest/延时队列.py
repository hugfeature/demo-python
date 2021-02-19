# author:丑牛
# datetime:2020/9/25 9:10
import json
import time
import uuid

import redis


def delay(msg):
    msg.id = str(uuid.uuid4())  # b保证value的唯一性
    value = json.dumps(msg)
    retry_ts = time.time() + 5
    redis.zadd("delay-queue", retry_ts, value)


def loop():
    values = redis.zrangebyscore("delay-queue", 0, time.time(), start=0, num=1)
    if not values:
        time.sleep(1)
        # continue
    value = values[0]
    success = redis.zrem("delay-queue", value)
    if success:
        msg = json.loads(value)
        handle_msg(msg)