#OracleRecordDeleteEx2.py
import cx_Oracle
def deleteRecord():
    while(True):
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
            print("-"*50)
            ch=input("Do you want to delete another record(yes/no):")
            if(ch.lower()=="no"):
                break
        except cx_Oracle.DatabaseError as db:
            print("Problem in Oracle DB", db)
        except ValueError:
            print("Don't enter alphanumerics,strs and symbols for empnos")


#main program
deleteRecord()