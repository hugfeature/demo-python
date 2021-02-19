# author:丑牛
# datetime:2020/9/5 8:46
import wmi


def connect_server(ip, user, passwod):
    connect = wmi.WMI(computer=ip, user=user, password=passwod)
    return connect


if __name__ == '__main__':
    connet = connect_server('192.168.175.215', 'administrator', 'yydk@67891289')
    for sys in connet.Win32_OperatingSystem():
        print("Version:%s" % sys.Caption.encode("UTF8"), "Vernum:%s" % sys.BuildNumber)  # 系统信息
        print(sys.OSArchitecture.encode("UTF8"))  # 系统的位数
        print(sys.NumberOfProcesses)  # 系统的进程数
