#MySQLTableAddColNameEx.py
import mysql.connector
def tableCreate():
    try:
        con=mysql.connector.connect(host="127.0.0.1",user="root",passwd="root",database="batch6pm")
        cur=con.cursor()
        aq="alter table student add(colname varchar(10))"
        cur.execute(aq)
        print("Student Table altered Successfully--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in Database: ",db)

#main program
tableCreate()