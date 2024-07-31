#OracleRecordInsertEx3.py
import cx_Oracle
def recordInsert():
    while(True):
        try:
            con=cx_Oracle.connect("system/manager@localhost/xe")
            cur=con.cursor()
            #accept the employee details from KBD
            print("-"*50)
            empno=int(input("Enter Employee Number: "))
            empname=input("Enter Employee Name: ")
            empsal=float(input("Enter EMployee Salary: "))
            empdsg=input("Enter Employee Designation: ")
            iq="insert into employee values(%d,'%s',%f,'%s')"
            cur.execute(iq %(empno,empname,empsal,empdsg))
            #or cur.execute("insert into employee values(%d,'%s',%f,'%s')" %(empno,empname,empsal,empdsg))
            con.commit()
            print("-" * 50)
            print("{} Employee record inserted in Employee table successfully".format(cur.rowcount))
            print("-" * 50)
            ch=input("Do you want to Insert another record(yes/no): ")
            if(ch.lower()=="no"):
                break
        except cx_Oracle.DatabaseError as db:
            print("Problem in Oracle DB",db)
        except ValueError:
            print("Don't enter alphanumerics,strs and symbols for empnos,sals")

#main program
recordInsert()