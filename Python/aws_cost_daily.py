import argparse
import boto3
import datetime

def cost_allert():
    parser = argparse.ArgumentParser()
    parser.add_argument('--days', type=int, default=1)
    args = parser.parse_args()

    now = datetime.datetime.utcnow()
    start = (now - datetime.timedelta(days=args.days)).strftime('%Y-%m-%d')
    end = now.strftime('%Y-%m-%d')

    cd = boto3.client('ce', 'ap-south-1')

    results = []
    logs = []
    token = None
    while True:
        if token:
            kwargs = {'NextPageToken': token}
        else:
            kwargs = {}
        data = cd.get_cost_and_usage(TimePeriod={'Start': start, 'End': end}, Granularity='DAILY',
                                     Metrics=['UnblendedCost'], GroupBy=[{'Type': 'DIMENSION', 'Key': 'LINKED_ACCOUNT'},
                                                                         {'Type': 'DIMENSION', 'Key': 'SERVICE'}],
                                     **kwargs)
        results += data['ResultsByTime']
        token = data.get('NextPageToken')
        if not token:
            break
    sum = 0
    for result_by_time in results:
        for group in result_by_time['Groups']:
            amount = group['Metrics']['UnblendedCost']['Amount']
            unit = group['Metrics']['UnblendedCost']['Unit']
            sum += float(amount)
            s = (result_by_time['TimePeriod']['Start'], '\t', '\t'.join(group['Keys']), '\t', amount, '\t', unit, '\t',
                 result_by_time['Estimated'])
            logs.append(s)

    report = [{'date': start, 'service': "Total Cost", 'cost': sum}]

    for i in logs:
        date = i[0]
        service = i[2].split("\t")[1]
        cost = float(i[4])
        log = {'date': date, 'service': service, 'cost': cost}
        report.append(log)

    return(report)

data = cost_allert()
flag = 0
try:
    reader = open("log.txt","r")
    previous_logs = reader.readlines()
    reader.close()
    flag = 1
except:
    print("except occured")
    writer = open("log.txt","w")
    for i in data:
        writer.write(i+"\n")
    writer.close()

