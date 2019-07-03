"""
Pre-requisite:
$ pip3 install mysql-connector-python
"""
import mysql.connector

def data_enter(fname,sname,email,password,branch):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sample_db'
    )
    mycursor = mydb.cursor()
    query="insert into users(fname, sname, email, password, branch) values(\""+fname+"\", \""+sname+"\", \""+email+"\", PASSWORD(\""+password+"\"), \""+branch+"\");"
    try:
        mycursor.execute(query)
        mydb.commit()
    except:
        print("Some error occured while entering data")
