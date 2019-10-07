from flask import Flask
from system_metrics import get_metrics
import time

config = eval(open('config', 'r').read())
cpu_limit = config['cpu_limit']

app = Flask(__name__)
@app.route("/metrics")
def server():
    data = get_metrics()
    cpu = data['cpu']
    if cpu > cpu_limit:
        message = "{} - {} ({}%)".format(time.strftime("%d/%m/%y %H:%M:%S"), "ALERT: cpu load high!", cpu)
        sep = "-"*len(message)
        print("{}\n{}\n{}".format(sep, message, sep))
    return data

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
