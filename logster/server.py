from flask import Flask
from system_metrics import get_metrics
import time

app = Flask(__name__)
@app.route("/metrics")
def server():
    data = get_metrics()
    cpu = data['cpu']
    if cpu > 4:
        message = "{}\n{}\n{}\n{} - {}%".format("--------", time.strftime("%H:%M:%S"), "--------", "ALERT- cpu load high!", cpu)
        print(message)
    return data

if __name__ == "__main__":
    app.run(debug=False)
