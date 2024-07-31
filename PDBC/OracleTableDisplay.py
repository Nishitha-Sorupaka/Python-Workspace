#Program for accepting any table name and display records along with column names
#OracleTableDisplay.py
import cx_Oracle
def getRecords():
    try:
        con=cx_Oracle.connect("system/manager@127.0.0.1/xe")
        cur=con.cursor()
        #accept table name from keyboard
        table=input("Enter any Table name: ")
        cur.execute("select * from %s" %table)
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
        print("'%s' table does not exist" %table)



#main program
getRecords()