#OracleRecordInsertEx1.py
import cx_Oracle #step-1
def recordInsert():
    try:
        con=cx_Oracle.connect("system/manager@localhost/xe") #step-2
        cur=con.cursor() #step-3
        #step-4
        iq="insert into employee values(400,'Sagarika',2.4,'SE')"
        cur.execute(iq)
        con.commit()
        print("Employee record inserted in Employee table successfully")
    except cx_Oracle.DatabaseError as db:
        print("Problem in Oracle DB",db)

#main program
recordInsert()