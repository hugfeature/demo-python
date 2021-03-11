# author:丑牛
# datetime:2021/3/10 9:10
import os


def tree(path):
    prefix = "| "
    if os.path.isfile(path):
        filePath, fileName = os.path.split(path)
        print("|__" + fileName)
    for home, dirs, files in os.walk(path):
        for f in files:
            num = home.count('\\')
            print(prefix * (num -1) + "|__"+f)
        for d in dirs:
            num = home.count('\\')
            print(prefix * (num - 1) + "|__" + d)


if __name__ == '__main__':
    path = 'D:\\test'
    tree(path)
