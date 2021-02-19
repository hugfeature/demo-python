# author:丑牛
# datetime:2020/7/3 8:34
import paramiko
import psutil

linux = ['192.168.175.196']


# 连接linux服务器
def connectHost(ip, uname='root', passwd='123456'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(ip, username=uname, password=passwd)
    return ssh


def MainCheck():
    for a in range(len(linux)):
        ssh = connectHost(linux[a])
        # 获取当前系统时间
        chk = "date \"+%F %T\""
        stdin, stdout, stderr = ssh.exec_command(chk)
        check_time = stdout.readlines()
        check_time = check_time[0]
        # 查看CPU的使用情况
        p = psutil.Process()
        cpu_per = psutil.cpu_percent(0.5)
        cpu = "vmstat |sed  '1d'|sed  '1d'|awk '{print $15}'"
        stdin, stdout, stderr = ssh.exec_command(cpu)
        cpu_usage = stdout.readlines()
        cpu_usage = 100-(int(cpu_usage[0])+int(cpu_usage[1])+int(cpu_usage[2]))/3
        # cpu_usage = str(round((100-(int(cpu_usage[0])+int(cpu_usage[1])+int(cpu_usage[2]))/3), 2)) + '%'
        print(cpu_per, cpu_usage, check_time)
        # sql = "insert into cpu_usage values('%s', '%s', '%s', sysdate)" %(linux[a], cpu_usage, check_time)
        # db = connectDB()
        # sqlDML(sql,db)

        # 查看内存使用
        mem_use = psutil.virtual_memory()
        mem = "cat /proc/meminfo|sed -n '1,4p'|awk '{print $2}'"
        stdin, stdout, stderr = ssh.exec_command(mem)
        mem = stdout.readlines()
        mem_total = round(int(mem[0]) / 1024)
        mem_total_free = round(int(mem[1]) / 1024) + round(int(mem[2]) / 1024) + round(int(mem[3]) / 1024)
        mem_usage = (mem_total - mem_total_free)/1024
        # mem_usage = str(round(((mem_total - mem_total_free) / mem_total) * 100, 2)) + "%"
        print(mem, mem_usage, check_time)
        # sql = "insert into mem_usage values('%s','%s','%s','%s','%s','%s','%s',sysdate)" % (
        #        linux[a], str(round(int(mem[0]) / 1024)) + "M", str(round(int(mem[1]) / 1024)) + "M",
        #        str(round(int(mem[2]) / 1024)) + "M", str(round(int(mem[3]) / 1024)) + "M", mem_usage, check_time)
        # db = connectDB()
        # sqlDML(sql, db)


if __name__ == '__main__':
    MainCheck()
