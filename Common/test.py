# author:丑牛
# datetime:2020/12/29 17:03
from icecream import ic


def is_exist(ele_list):
    for text in ele_list[0:2]:
        ic(text)
        if '必须' not in text:
            ic(text)
            return False
    text = ele_list[2]
    ic(text)
    return True


if __name__ == "__main__":
    # text_list = ['必须1', '必须的', 'json']
    # result = is_exist(text_list)
    # ic(result)
    text = ''
    ic(len(text)==0)