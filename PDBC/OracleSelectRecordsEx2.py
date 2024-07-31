#Program for reading the records from employee table
#OracleSelectRecordsEx2.py
import cx_Oracle
def getRecords():
    try:
        con=cx_Oracle.connect("system/manager@127.0.0.1/xe")
        cur=con.cursor()
        cur.execute("select * from employee")
        print("-"*50)
        records = cur.fetchmany(5)
        for record in records:
            for val in record:
                print("{}".format(val),end="\t")
            print()
        print("-"*50)
    except cx_Oracle.DatabaseError as db:
        print("Problem in Database: ",db)



#main program
getRecords()