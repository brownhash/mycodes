import csv
import time
import mysql.connector


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

        column_name = []
        columns = my_cursor.description
        for column in columns:
            column_name.append(column[0])

        my_result = my_cursor.fetchall()
        print("--------")
        print(time.strftime("%H:%M:%S"))
        print("--------")

        csv_data = [column_name]
        for x in my_result:
            print(x)
            temp = []
            for object in x:
                temp.append(object)
            csv_data.append(temp)

        with open('my_data.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(csv_data)
        csvFile.close()
    except Exception as error:
        print("Error: ", error)


"""
OUTPUT IN CSV -

name,email                                             <--column names
harrypotter,harry.potter@gmail.com                        <--data
Harshit Sharma,harshit.sharma@gmail.com      <--data
"""
