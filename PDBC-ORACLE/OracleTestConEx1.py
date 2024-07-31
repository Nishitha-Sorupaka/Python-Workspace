#program for demonstrating how to get the connection Oracle Database
#OracleTestConEx1.py
import cx_Oracle # Step-1
kvr=cx_Oracle.connect("system/manager@localhost/xe")
print("\n Type of kvr=",type(kvr))
print("Python program obtains connection from Oracle DB")