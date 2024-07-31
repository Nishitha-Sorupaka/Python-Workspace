#MySQLRecordInsertEx.py
import mysql.connector
def recordinsert():
    try:
       con = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          passwd="root",
                                          database="batch6pm")
       while(True):
           try:
               cur=con.cursor()
               print("-"*50)
               #accept the emp details from KBD
               empno=int(input("Enter Employee Number:"))
               empname=input("Enter Employee Name:")
               empsal=float(input("Enter Employee Salary:"))
               empdsg = input("Enter Employee Designation:")
               #Prepare the Query with dynamic values
               iq="insert into employee values(%d,'%s',%f,'%s')"
               cur.execute(iq %(empno,empname,empsal,empdsg))
               #OR cur.execute("insert into employee values(%d,%s',%f,'%s')" %(empno,empname,empsal,empdsg))
               con.commit()
               print("-" * 50)
               print("{} Employee Record Inserted Sucessfully in Employee Table".format(cur.rowcount))
               print("-" * 50)
               ch=input("Do u want Insert  another record(yes/no):")
               if(ch.lower()=="no"):
                   break
           except ValueError:
               print("Don't enter alnums,strs and symbols for empnos,sals")
    except mysql.connector.DatabaseError as db:
            print("Problem in Oarcle DB",db)
#main program
recordinsert()