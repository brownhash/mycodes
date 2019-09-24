import mysql.connector
import time


def mysql_write(host, user, password, db, query):

    my_db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db
    )

    my_cursor = my_db.cursor()

    try:
        print("--------")
        print(time.strftime("%H:%M:%S"))
        print("--------")
        my_cursor.execute(query)
        my_db.commit()
        print("Executed: ", query)
    except Exception as error:
        print("--------")
        print(time.strftime("%H:%M:%S"))
        print("--------")
        print("Error: ", error)


def mysql_read(host, user, password, db, query):
    my_db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db
    )

    my_cursor = my_db.cursor()

    try:
        my_cursor.execute(query)

        my_result = my_cursor.fetchall()
        print("--------")
        print(time.strftime("%H:%M:%S"))
        print("--------")
        columns = my_cursor.description
        column_name = ()
        for column in columns:
            column_name += (column[0],)
        print(column_name)
        for x in my_result:
            print(x)
    except Exception as error:
        print("Error: ", error)
