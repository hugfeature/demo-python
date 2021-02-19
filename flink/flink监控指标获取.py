# author:丑牛
# datetime:2020/10/16 13:28
import requests

HOST = "192.168.175.234"
PORT = "8081"
JOBID = 'e5f5dd1148b1827c206b07e379f9e98d'
TASKID = 'container_1601880205345_0303_01_000002'
VERTICESID = '5c4ca2fea30dcf09bf3ee40c495fe808'


def jobs_overview():
    """
    :return: 返回jobs信息
    """
    url = "http://" + HOST + ":" + PORT + '/jobs/overview'
    reponse = requests.get(url)
    # reponse转为json格式
    result = reponse.json()
    # 获取applicatios列表
    print(result['jobs'])


def jobs_metrics():
    """
    :return: 返回jobs指标信息
    """
    url_metrics = "http://" + HOST + ":" + PORT + '/jobs/metrics'
    reponse = requests.get(url_metrics)
    result = reponse.json()
    for metric in result:
        url_metric = "http://" + HOST + ":" + PORT + '/jobs/metrics?get=' + metric['id']
        reponse = requests.get(url_metric)
        result = reponse.json()
        print(metric['id'], "=>", result)


def jobmanager_metrics():
    """
    :return: 返回job的消耗的系统信息
    """
    url_metrics = "http://" + HOST + ":" + PORT + '/jobmanager/metrics'
    reponse = requests.get(url_metrics)
    result = reponse.json()
    for metric in result:
        url_metric = "http://" + HOST + ":" + PORT + '/jobmanager/metrics?get=' + metric['id']
        reponse = requests.get(url_metric)
        result = reponse.json()
        print(metric['id'], "=>", result)


def jobs_checkpoints():
    """
    :return: 返回jobs的checkpoints信息
    """
    url = "http://" + HOST + ":" + PORT + '/jobs/' + JOBID + '/checkpoints'
    reponse = requests.get(url)
    # reponse转为json格式
    result = reponse.json()
    # 获取applicatios列表
    print(result)


def jobs_vertexid():
    """
    :return: 返回jobs的vertices信息
    """
    url = "http://" + HOST + ":" + PORT + '/jobs/' + JOBID
    reponse = requests.get(url)
    # reponse转为json格式
    result = reponse.json()
    # 获取applicatios列表
    print(result['vertices'])


def jobs_backPressure():
    """
    :return: 返回jobs的backpressure信息
    """
    url = "http://" + HOST + ":" + PORT + '/jobs/' + JOBID + '/vertices/' + VERTICESID + '/backpressure'
    reponse = requests.get(url)
    # reponse转为json格式
    result = reponse.json()
    # 获取applicatios列表
    print(result)


def jobvertices_metrics():
    """
    :return: 返回jobvertices的指标信息
    """
    url_metrics = "http://" + HOST + ":" + PORT + '/jobs/' + JOBID + '/vertices/' + VERTICESID + '/metrics'
    reponse = requests.get(url_metrics)
    result = reponse.json()
    # list_1 = []
    for metric in result:
        url_metric = "http://" + HOST + ":" + PORT + '/jobs/' + JOBID + '/vertices/' + VERTICESID + '/metrics?get=' + metric['id']
        reponse = requests.get(url_metric)
        result = reponse.json()
        print(metric['id'], "=>", result)
    #     list_1.append(result)
    # print(list_1[0][0]['value'])


def task_overview():
    """
    :return: 返回taskmanager
    """
    url = "http://" + HOST + ":" + PORT + '/taskmanagers'
    reponse = requests.get(url)
    # reponse转为json格式
    result = reponse.json()
    # 获取applicatios列表
    print(result)


def task_metrics():
    """
    :return: 返回task指标信息
    """
    url_metrics = "http://" + HOST + ":" + PORT + '/taskmanagers/metrics'
    reponse = requests.get(url_metrics)
    result = reponse.json()
    for metric in result:
        url_metric = "http://" + HOST + ":" + PORT + '/taskmanagers/metrics?get=' + metric['id']
        reponse = requests.get(url_metric)
        result = reponse.json()
        print(metric['id'], "=>", result)


if __name__ == "__main__":
    # jobs_overview()
    # jobs_metrics()
    # jobmanager_metrics()
    # jobs_checkpoints()
    jobvertices_metrics()
    # jobs_backPressure()
    # task_overview()
    # task_metrics()
