#Program for demonstrating creating cursor in MySQL
#MySQLCursorTestEx1.py
import mysql.connector
con=mysql.connector.connect(host="127.0.0.1",user="root",passwd="root")
print("\nPython program obtains connection from MySQL")
print("Type of con= ",type(con))
cur=con.cursor()
print("\nPython program created a cursor object")
print("Type of cur= ",type(cur))