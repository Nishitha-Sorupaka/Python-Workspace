#MySQLRecordUpdateEx.py
import mysql.connector
def recordUpdate():
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
               empname = input("Enter Employee Name:")
               empsal = float(input("Enter Employee Salary:"))
               empdsg = input("Enter Employee Designation:")
               #Prepare the Query with dynamic values
               iq="update employee set ename='%s',sal=%f,dsg='%s' where eno=%d"
               cur.execute(iq %(empname,empsal,empdsg,empno))
               #OR cur.execute("insert into employee values(%d,%s',%f,'%s')" %(empno,empname,empsal,empdsg))
               con.commit()
               print("-" * 50)
               if(cur.rowcount>0):
                   print("{} Employee Record Updated Sucessfully in Employee Table".format(cur.rowcount))
               else:
                   print("Employee record does not exist")

               print("-" * 50)
               ch=input("Do u want Update another record(yes/no):")
               if(ch.lower()=="no"):
                   break
           except ValueError:
               print("Don't enter alnums,strs and symbols for empnos")
    except mysql.connector.DatabaseError as db:
            print("Problem in Oarcle DB",db)
#main program
recordUpdate()