#MySQLDropTableEx.py
import mysql.connector
def tableDrop():
    try:
        con=mysql.connector.connect(host="127.0.0.1",user="root",passwd="root",database="batch6pm")
        cur=con.cursor()
        tb="drop table student1"
        cur.execute(tb)
        print("Student Table Dropped Successfully--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in Database: ",db)

#main program
tableDrop()