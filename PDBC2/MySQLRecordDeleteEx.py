#MySQLRecordDeleteEx.py
import mysql.connector
def recordDelete():
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
               #Prepare the Query with dynamic values
               iq="delete from employee where eno=%d"
               cur.execute(iq %(empno))
               #OR cur.execute("insert into employee values(%d,%s',%f,'%s')" %(empno,empname,empsal,empdsg))
               con.commit()
               print("-" * 50)
               if(cur.rowcount>0):
                   print("{} Employee Record Deleted Sucessfully in Employee Table".format(cur.rowcount))
               else:
                   print("Employee record does not exist")

               print("-" * 50)
               ch=input("Do u want delete another record(yes/no):")
               if(ch.lower()=="no"):
                   break
           except ValueError:
               print("Don't enter alnums,strs and symbols for empnos")
    except mysql.connector.DatabaseError as db:
            print("Problem in Oarcle DB",db)
#main program
recordDelete()