"""
Pre-requisite:
$ pip3 install mysql-connector-python
"""
import mysql.connector

def data_enter():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456789',
        database='harrydbst'
    )
    mycursor = mydb.cursor()
    #query = 'create database harrydbst;'
    #query = 'create table data(name varchar(20), email varchar(50));'
    #query = 'insert into data values(\'{}\', \'{}\');'.format("Harshit Sharma","harshit.sharma@partners.rivigo.com")
    #query = 'delete from data where name = \'{}\';'.format("Harshit Sharma 2")
    #query = 'alter table data modify email varchar(50) not null unique'

    try:
        mycursor.execute(query)
        mydb.commit()
        print('Done')
    except Exception as e:
        print("Some error occured while entering data")
        print(e)

data_enter()
