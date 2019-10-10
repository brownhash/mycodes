from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from mysql_functions import *
import time


application = Flask(__name__)
@application.route("/happysystem")
def happy_system():
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
        host_query = "select host, host_name from happyserver.server_data;"
        hosts = mysql_read(mysql_host, mysql_username, mysql_password, mysql_database, host_query)

        for target in hosts:
            host_data.append([target[0], target[1]])
    except Exception as error:
        print("{} : Error in reading hosts. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))

    groups_data = []

    try:
        group_query = "select group_name from happyserver.server_data;"
        groups = mysql_read(mysql_host, mysql_username, mysql_password, mysql_database, group_query)

        for group in groups:
            group_data = group[0]
            if group_data not in groups_data:
                groups_data.append(group_data)
    except Exception as error:
        print("{} : Error in reading groups. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))

    alerts = []

    try:
        alert_query = "select * from happyserver.alert;"
        alert = mysql_read(mysql_host, mysql_username, mysql_password, mysql_database, alert_query)

        for alrt in alert:
            alert_data = "{}({})".format(alrt[0], alrt[1])
            alerts.append(alert_data)
    except Exception as error:
        print("{} : Error in reading alerts. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))

    return render_template("happy_system.html", result={'hosts':host_data, 'groups':groups_data, 'alerts': alerts})


@application.route("/managetargets")
def manage_targets():
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
        host_query = "select host, host_name, group_name from happyserver.server_data;"
        hosts = mysql_read(mysql_host, mysql_username, mysql_password, mysql_database, host_query)

        for target in hosts:
            target_data = [target[0], target[1], target[2]]
            host_data.append(target_data)
    except Exception as error:
        print("{} : Error in reading hosts. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))

    return render_template("manage_targets.html", result = {'total_hosts': len(host_data), 'hosts':host_data})


@application.route("/addtarget", methods=['POST'])
def add_target():

    if request.method == 'POST':

        result = request.form
        target_address = result.get("target_address")
        target_name = result.get("target_name")
        group = result.get("group")
        if not target_name or not target_address or not group:
            return "Fill all the fields"

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
            add_target_query = "insert into server_data values(\'{}\', \'{}\', \'{}\', \'{}\');".format(time.strftime("%H:%M:%S %d/%m/%y"), target_address, target_name, group)
            print(add_target_query)
            mysql_write(mysql_host, mysql_username, mysql_password, mysql_database, add_target_query)
            return redirect("http://localhost:5000/managetargets")
        except Exception as error:
            print("{} : Error in adding Target. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))
            return "error"


@application.route("/removetarget", methods=['POST'])
def remove_target():
    if request.method == 'POST':

        result = request.form
        target = result.get("targets")
        if not target:
            return "No target was selected"
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
            remove_target_query = "delete from server_data where `host`=\'{}\';".format(target)
            print(remove_target_query)
            mysql_remover(mysql_host, mysql_username, mysql_password, mysql_database, remove_target_query)
            return redirect("http://localhost:5000/managetargets")
        except Exception as error:
            print("{} : Error in adding Target. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))
            return "error"


if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0')
