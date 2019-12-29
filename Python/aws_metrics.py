import boto3
from datetime import datetime, timedelta

from flask import Flask
app = Flask(__name__)

@app.route("/metrics-mumbai")
def metrics_mumbai():
    return metrics("ap-south-1", 'i-005e8a7e3c38bab73')

@app.route("/metrics-singapore")
def metrics_sg():
    return metrics("ap-southeast-1", 'i-03be561ef6bc83400')


def metrics(region, i_id):
    t_day = datetime.today().day
    t_month = datetime.today().month
    t_year = datetime.today().year

    client = boto3.client('cloudwatch', region_name=region)
    response = client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': i_id
            },
        ],
        StartTime=datetime(2019, 9, 1) - timedelta(seconds=300),
        EndTime=datetime(t_year, t_month, t_day),
        Period=86400,
        Statistics=[
            'Maximum',
            'Minimum',
            'Average'
        ],
        Unit='Percent'
    )
    metric = ""
    for cpu in response['Datapoints']:
        date = str(cpu.get('Timestamp')).split(" ")[0]
        date = date.split("-")
        date = date[2]+"-"+date[1]+"-"+date[0]
        data = "{} {} {} {}$$".format(date, int(cpu.get('Minimum')),
                                      int(cpu.get('Maximum')), int(cpu.get('Average')))
        metric += data

    return metric

if __name__ == "__main__":
    app.run(debug=True)