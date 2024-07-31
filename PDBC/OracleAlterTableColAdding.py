#OracleAlterTableColAdding.py
import cx_Oracle #step-1
def tableColAdd():
    try:
        con=cx_Oracle.connect("system/manager@localhost/xe") #step-2
        cur=con.cursor() #step-3
        #step-4
        ct="alter table employee add(cname varchar2(10) not null)"
        cur.execute(ct)
        #step-5
        print("Employee Table altered successfully in Oracle DB--verify")
    except cx_Oracle.DatabaseError as db:
        print("Problem in Oracle DB",db)

#main program
tableColAdd()