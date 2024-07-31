#Program for demonstating connection from MySql
#MySqlConnTestEx2.py
import mysql.connector
con=mysql.connector.connect(host="127.0.0.1",user="root",passwd="root")
print("\nPython program obtains connection from MySQL")
print("Type of con= ",type(con))