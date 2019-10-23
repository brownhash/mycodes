from mysql_functions import *
import time
import requests


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


def metrics_importer():
    servers = get_servers()
    for server in servers:
        metric_data = get_metrics(server)
        print(metric_data)


metrics_importer()
