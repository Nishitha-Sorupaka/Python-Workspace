#OracleTableCreateEx1.py
import cx_Oracle #step-1
def tablecreate():
    try:
        con=cx_Oracle.connect("system/manager@localhost/xe") #step-2
        cur=con.cursor() #step-3
        #step-4
        ct="create table employee1(eno number(2) primary key,ename varchar2(10) not null,marks number(5,2) not null)"
        cur.execute(ct)
        #step-5
        print("Employee Table Created successfully in Oracle Database")
    except cx_Oracle.DatabaseError as db:
        print("Problem in Oracle DB",db)

#main program
tablecreate()