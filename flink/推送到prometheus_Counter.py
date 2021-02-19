# author:丑牛
# datetime:2020/10/27 16:44
import prometheus_client
from prometheus_client import Counter
from flask import Response, Flask

app = Flask(__name__)

requests_total = Counter("request_count", "Total request cout of the host")


@app.route("/metrics")
def requests_count():
    requests_total.inc()
    # requests_total.inc(2)
    return Response(prometheus_client.generate_latest(requests_total),
                    mimetype="text/plain")


@app.route('/')
def index():
    requests_total.inc()
    return "Hello World"


if __name__ == "__main__":
    app.run('127.0.0.1')
