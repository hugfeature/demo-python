# author:丑牛
# datetime:2020/9/27 9:07
import time


class Funnel(object):

    def __init__(self, capacity, leaking_rate):
        self.capacity = capacity
        self.leaking_rate = leaking_rate
        self.left_quota = capacity
        self.leaking_ts = time.time()

    def make_space(self):
        now_ts = time.time()
        delta_ts = now_ts - self.leaking_ts
        delts_quota = delta_ts * self.leaking_rate
        if delts_quota < 1:
            return
        self.left_quota += delts_quota
        self.leaking_ts = now_ts
        if self.left_quota > self.capacity:
            self.left_quota = self.capacity

    def watering(self, quota):
        self.make_space()
        if self.left_quota >= quota:
            self.left_quota -= quota
            return True
        return False


funnels = {}


def is_action_allowed(use_id, action_key, capacity, leaking_rate):
    key = '%s:%s' % (use_id, action_key)
    funnel = funnels.get(key)
    if not funnel:
        funnel = Funnel(capacity, leaking_rate)
        funnels[key] = funnel
    return funnel.watering(1)


for i in range(20):
    print(is_action_allowed('laoqian', 'reply', 15, 0.5))
