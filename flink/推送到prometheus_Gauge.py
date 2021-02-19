# author:丑牛
# datetime:2020/10/28 15:49
import random
import prometheus_client
import requests
from prometheus_client import Gauge
from flask import Response, Flask
from prometheus_client.registry import CollectorRegistry

HOST = "192.168.175.234"
PORT = "8081"
JOBID = 'e5f5dd1148b1827c206b07e379f9e98d'
TASKID = 'container_1601880205345_0303_01_000002'
VERTICESID = '5c4ca2fea30dcf09bf3ee40c495fe808'


def jobvertices_metrics():
    """
    :return: 返回jobvertices的指标信息
    """
    url_metrics = "http://" + HOST + ":" + PORT + '/jobs/' + JOBID + '/vertices/' + VERTICESID + '/metrics'
    reponse = requests.get(url_metrics)
    result = reponse.json()
    list_1 = []
    for metric in result:
        url_metric = "http://" + HOST + ":" + PORT + '/jobs/' + JOBID + '/vertices/' + VERTICESID + '/metrics?get=' + \
                     metric['id']
        reponse = requests.get(url_metric)
        result = reponse.json()
        print(metric['id'], "=>", result)
        list_1.append(result)
    return list_1[46][0]['value'], list_1[274][0]['value'], list_1[0][0]['value']


app = Flask(__name__)
registry = CollectorRegistry()
currentOffsets_0 = Gauge("topic0", "topic0currentOffsets", registry=registry)
currentOffsets_1 = Gauge("topic1", "topic1currentOffsets", registry=registry)
currentOffsets_2 = Gauge("topic2", "topic2currentOffsets", registry=registry)


@app.route("/metrics")
def r_value():
    offset_0, offset_1, offset_2 = jobvertices_metrics()
    currentOffsets_0.set(offset_0)
    currentOffsets_1.set(offset_1)
    currentOffsets_1.set(offset_2)
    return Response(prometheus_client.generate_latest(registry),
                    mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
