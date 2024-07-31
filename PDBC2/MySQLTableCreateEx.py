#MySQLTableCreateEx.py
import mysql.connector
def tableCreate():
    try:
        con=mysql.connector.connect(host="127.0.0.1",user="root",passwd="root",database="batch6pm")
        cur=con.cursor()
        tc="create table student1(sno int primary key,name varchar(10) not null,marks float not null)"
        cur.execute(tc)
        print("Student Table Created Successfully--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem in Database: ",db)

#main program
tableCreate()