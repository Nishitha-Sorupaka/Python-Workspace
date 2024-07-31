#program for creating an object of cursor
#OracleCursorEx1.py
import cx_Oracle # step-1
try:
    con=cx_Oracle.connect("system/manager@localhost/xe") #step-2
    print("\nType of con=",type(con))
    print("Python program obtained connection from Oracle DB")
    cur=con.cursor() #step-3 
    print("\nType of cur=",type(cur))
    print("Python program creates cursor object")
except cx_Oracle.DatabaseError as db:
    print("Problem in Oracle DB: ", db)
