#Program for Reading the data from CSV File by using CSV Module
#CsvReaderEx2.py----csv.reader()---Gives an object csv.reader class object
import csv
try:
    with open("emp.csv","r") as fp:
        csvr=csv.reader(fp) #Here csvr is an object of <class, _csv.reader>
        for record in csvr:
            for val in record:
                print("{}".format(val),end="\t")
            print()
        print("-"*50)
except FileNotFoundError:
    print("File Does not Exist")

