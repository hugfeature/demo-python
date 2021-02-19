# author:丑牛
# datetime:2021/2/2 10:31
while True:
    try:
        list1 = []
        arr = input()
        dic = {}
        for i in arr:
            if not (i.isalpha() or i.isdigit() or i.isspace()):
                continue
            else:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
        dic = sorted(dic.items(), key=lambda x: x[0])  # 先按字符ASC排
        dic = sorted(dic, key=lambda x: x[1], reverse=True)  # 再按统计数目排
        print(''.join(k for (k, v) in dic))
    except:
        break
