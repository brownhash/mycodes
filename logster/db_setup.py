import time
from mysql_functions import *


def db_setup():
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
        create_query = "create table IF NOT EXISTS `server_data` (`time` VARCHAR(20) NOT NULL, `host` VARCHAR(20) NOT NULL UNIQUE, `host_name` VARCHAR(50) NOT NULL UNIQUE, `group_name` VARCHAR(50) NOT NULL);"
        create_tables(mysql_host, mysql_username, mysql_password, mysql_database, create_query)
    except Exception as error:
        print("{} : Error in creating table - server_data. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))

    try:
        create_query = "create table IF NOT EXISTS `alert` (`alert_name` varchar(50) NOT NULL, `alert_type` varchar(20) NOT NULL);"
        create_tables(mysql_host, mysql_username, mysql_password, mysql_database, create_query)
    except Exception as error:
        print("{} : Error in creating table - server_data. {}".format(time.strftime("%H:%M:%S %d/%m/%y"), error))
