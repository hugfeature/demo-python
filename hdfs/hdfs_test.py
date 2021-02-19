# author:丑牛
# datetime:2020/7/29 9:46

from hdfs.client import Client


def con(host):
    conn = Client(host)
    return conn


def ls(host, remote_path):
    conn = con(host)
    list_path = conn.list(remote_path)
    return list_path


def down(host, remote_path, local_path):
    conn = con(host)
    conn.download(remote_path, local_path)


if __name__ == "__main__":
    hdfs_host = "http://192.168.175.231:9870/"
    client = Client(hdfs_host)
    print(client.list("/test/parquet/ns=37082600014020001005/d=20200801"))
    print(len(client.list("/test/parquet/ns=37082600014020001005/d=20200801")))
    # client.download('/test/parquet/ns=37082600014020001005',
    #                 'D:\\PycharmWorkSpace\\demo\\hdfs')
    # local_file_path = "D:\\PycharmWorkSpace\\demo\\hdfs\\ns=37082600014020001005"
    # columns = ['id', 't', 'v', 'vt', 'c', 'u', 's', 'dqsj']
    # df = pa.read_parquet(local_file_path, engine='auto', columns=columns)
    # print(df['dqsj'])
