#OracleRecordUpdateEx1.py
import cx_Oracle
def updateRecord():
    try:
        con=cx_Oracle.connect("system/manager@localhost/xe")
        cur=con.cursor()
        eno=int(input("Enter Employee Number for updating a Record: "))
        empdsg=input("Enter new Designation of Employee: ")
        cur.execute("update employee set sal=sal+sal*(20/100),desg='%s' where eno=%d" %(empdsg,eno))
        con.commit()
        if(cur.rowcount>0):
            print("{} record successfully updated from Employee table".format(cur.rowcount))
        else:
            print("{} Employee Number does not exist!".format(eno))
    except cx_Oracle.DatabaseError as db:
        print("Problem in Oracle DB", db)


#main program
updateRecord()