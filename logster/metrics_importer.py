from mysql_functions import *
import time
import requests
import json


def get_servers():
    try:
        reader = open("config_main", "r")
        config = eval(reader.read())
        reader.close()
        mysql_config = config['mysql_config']
        mysql_host = mysql_config['host']
        mysql_username = mysql_config['username']
        mysql_password = mysql_config['password']
        mysql_database = mysql_config['database']
    except Exception as error:
        print("{} : Error in reading config. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))

    host_data = []

    try:
        host_query = "select host from happyserver.server_data;"
        hosts = mysql_read(mysql_host, mysql_username, mysql_password, mysql_database, host_query)

        for target in hosts:
            host_data.append(target[0])
    except Exception as error:
        print("{} : Error in reading hosts. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))

    return host_data


def get_metrics(target):
    url = "http://{}:8081/metrics".format(str(target))
    data = requests.get(url).text
    return data


def push_metrics(host, data):
    try:
        reader = open("config_main", "r")
        config = eval(reader.read())
        reader.close()
        mysql_config = config['mysql_config']
        mysql_host = mysql_config['host']
        mysql_username = mysql_config['username']
        mysql_password = mysql_config['password']
        mysql_database = mysql_config['database']
    except Exception as error:
        print("{} : Error in reading config. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))

    try:
        metrics_query = "select metrics from happyserver.metrics_data where `host`=\"{}\"".format(host)
        metrics_data = mysql_read(mysql_host, mysql_username, mysql_password, mysql_database, metrics_query)

        for metric in metrics_data[0]:
            if metric == "0":

                try:
                    reader = open("config_main", "r")
                    config = eval(reader.read())
                    reader.close()
                    mysql_config = config['mysql_config']
                    mysql_host = mysql_config['host']
                    mysql_username = mysql_config['username']
                    mysql_password = mysql_config['password']
                    mysql_database = mysql_config['database']
                except Exception as error:
                    print("{} : Error in reading config. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))

                try:
                    push_query = "update happyserver.metrics_data set metrics={} where `host`=\"{}\"".format(json.dumps(data), host)
                    mysql_write(mysql_host, mysql_username, mysql_password, mysql_database, push_query)
                except Exception as error:
                    print("{} : Error in pushing metrics data. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))

            else:
                try:
                    reader = open("config_main", "r")
                    config = eval(reader.read())
                    reader.close()
                    mysql_config = config['mysql_config']
                    mysql_host = mysql_config['host']
                    mysql_username = mysql_config['username']
                    mysql_password = mysql_config['password']
                    mysql_database = mysql_config['database']
                except Exception as error:
                    print("{} : Error in reading config. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))

                print()

    except Exception as error:
        print("{} : Error in reading metrics. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))


def metrics_importer():
    servers = get_servers()
    result = {}
    for server in servers:
        metric_data = get_metrics(server)
        result[server] = metric_data
        push_metrics(server, metric_data)


metrics_importer()
