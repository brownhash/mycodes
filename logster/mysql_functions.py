import mysql.connector


def mysql_read(host, user, password, database, read_query):
    my_db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    my_cursor = my_db.cursor()

    if "SELECT" not in read_query and "select" not in read_query:
        print("Query is not reading data.")
    else:
        query = read_query

    my_cursor.execute(query)
    my_result = my_cursor.fetchall()
    my_cursor.close()

    return my_result


def mysql_write(host, user, password, database, write_query):
    my_db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    my_cursor = my_db.cursor()

    if "INSERT" not in write_query and "insert" not in write_query and "update" not in write_query and "UPDATE" not in write_query:
        print("Query is not inserting data.")
        return "Error"
    else:
        my_cursor.execute(write_query)
        my_db.commit()
        my_cursor.close()

        return "Data inserted"


def mysql_remover(host, user, password, database, remove_query):
    my_db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    my_cursor = my_db.cursor()

    if "DELETE" not in remove_query and "delete" not in remove_query:
        print("Query is not deleting data.")
        return "Error"
    else:
        my_cursor.execute(remove_query)
        my_db.commit()
        my_cursor.close()

        return "Data deleted"


def create_tables(host, user, password, database, create_query):
    my_db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    my_cursor = my_db.cursor()
    if "CREATE" not in create_query and "create" not in create_query:
        print("Query is not creating table.")
        return "Error"
    else:
        my_cursor.execute(create_query)
        my_db.commit()
        my_cursor.close()

        return "table created"
