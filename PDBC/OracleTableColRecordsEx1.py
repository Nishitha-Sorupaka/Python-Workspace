#Program for obtaining Column names along with records
#OracleTableColRecordsEx1.py
import cx_Oracle
def getRecords():
    try:
        con=cx_Oracle.connect("system/manager@127.0.0.1/xe")
        cur=con.cursor()
        cur.execute("select * from employee")
        print("-"*50)
        #code for obtaining Col Names
        for col in cur.description:
            print(col[0],end="\t")
        print()
        print("-" * 50)
        #code for obtaining records
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val),end="\t")
            print()
        print("-" * 50)
    except cx_Oracle.DatabaseError as db:
        print("Problem in Database: ",db)



#main program
getRecords()