#Program for demonstrating how to get the connection Oracle Database
#OracleTestConEx2.py
import cx_Oracle # Step-1
try:
    kvr=cx_Oracle.connect("system/manager@127.0.0.1/xe") # Step-2
    print("\nType of kvr=",type(kvr))
    print("Python Program program obtains Connection from Oracle DB")
except cx_Oracle.DatabaseError as db:
    print("Database error: ",db)