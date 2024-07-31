#Program for creating a Database--batch6pm
#MySQLDatabaseCreateEx1.py
import mysql.connector
def databaseCreate():
    try:
        con=mysql.connector.connect(host="127.0.0.1",user="root",passwd="root")
        print("\nPython program obtains connection from MySQL")
        print("Type of con= ",type(con))
        cur=con.cursor()
        print("\nPython program created a cursor object")
        print("Type of cur= ",type(cur))
        cur.execute("create database batch6pm")
        print("Database Created Successfully")
    except mysql.connector.DatabaseError as db:
        print("Problem in Database: ",db)

#main program
databaseCreate()
