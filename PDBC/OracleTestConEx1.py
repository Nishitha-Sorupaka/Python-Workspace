#program for demonstrating Python connection with Oracle DB
import cx_Oracle
kvr=cx_Oracle.connect("system/manager@localhost/xe")
print("\n Type of kvr=",type(kvr))
print("Python program obtains connection from Oracle DB")