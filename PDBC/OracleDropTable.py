#OracleDropTable.py
#OracleAlterTableColAdding.py
import cx_Oracle #step-1
def tableDrop():
    try:
        con=cx_Oracle.connect("system/manager@localhost/xe") #step-2
        cur=con.cursor() #step-3
        #step-4
        ct="drop table employee1"
        cur.execute(ct)
        #step-5
        print("Employee Table deleted successfully from Oracle DB--verify")
    except cx_Oracle.DatabaseError as db:
        print("Problem in Oracle DB",db)

#main program
tableDrop()