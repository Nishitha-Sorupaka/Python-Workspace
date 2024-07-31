#Program for reading the records from employee table
#OracleSelectRecordsEx1.py
import cx_Oracle
def getRecords():
    try:
        con=cx_Oracle.connect("system/manager@127.0.0.1/xe")
        cur=con.cursor()
        cur.execute("select * from employee")
        print("-"*50)
        while(True):
            record = cur.fetchone()
            if(record!=None):
                for val in record:
                    print("{}".format(val),end="\t")
                print()
            else:
                print("-" * 50)
                break
    except cx_Oracle.DatabaseError as db:
        print("Problem in Database: ",db)



#main program
getRecords()