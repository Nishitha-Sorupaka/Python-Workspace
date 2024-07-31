#Program for demonstating connection from MySql
#MySqlConnTestEx1.py
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="root")
print("\nPython program obtains connection from MySQL")
print("Type of con= ",type(con))