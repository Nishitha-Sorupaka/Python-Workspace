#OracleRecordInsertEx2.py
import cx_Oracle
def recordInsert():
    try:
        con=cx_Oracle.connect("system/manager@localhost/xe")
        cur=con.cursor()
        #accept the employee details from KBD
        empno=int(input("Enter Employee Number: "))
        empname=input("Enter Employee Name: ")
        empsal=float(input("Enter Employee Salary: "))
        empdsg=input("Enter Employee Designation: ")
        iq="insert into employee values(%d,'%s',%f,'%s')"
        cur.execute(iq %(empno,empname,empsal,empdsg))
        #or cur.execute("insert into employee values(%d,'%s',%f,'%s')" %(empno,empname,empsal,empdsg))
        con.commit()
        print("Employee record inserted in Employee table successfully")
    except cx_Oracle.DatabaseError as db:
        print("Problem in Oracle DB",db)

#main program
recordInsert()