#OracleRecordDeleteEx1.py
import cx_Oracle
def deleteRecord():
    try:
        con=cx_Oracle.connect("system/manager@localhost/xe")
        cur=con.cursor()
        eno=int(input("Enter Employee Number for deleting a Record: "))
        cur.execute("delete from employee where eno=%d" %eno)
        con.commit()
        if(cur.rowcount>0):
            print("{} record successfully deleted from Employee table".format(cur.rowcount))
        else:
            print("{} Employee Number does not exist!".format(eno))
    except cx_Oracle.DatabaseError as db:
        print("Problem in Oracle DB", db)


#main program
deleteRecord()