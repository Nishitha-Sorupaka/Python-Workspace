#MySQLRecordSelectEx.py
import mysql.connector
def recordSelect():
    try:
       con = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          passwd="root",
                                          database="batch6pm")
       cur=con.cursor()
       tname=input("Enter any table name: ")
       cur.execute("select * from %s" %tname)
       #getting column names
       print("-"*50)
       for col in cur.description:
           print(col[0],end="\t")
       print()
       print("-" * 50)
       #getting the records
       records=cur.fetchall()
       for record in records:
           for val in record:
               print("{}".format(val),end="\t")
           print()
       print("-" * 50)


    except mysql.connector.DatabaseError as db:
            print("Problem in Oarcle DB",db)
#main program
recordSelect()