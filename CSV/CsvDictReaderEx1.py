#Program for Reading the data from CSV File by using CSV Module in the form Dict
#CsvDictReaderEx1.py
import csv
try:
    with open("emp.csv","r") as fp:
        csvdr=csv.DictReader(fp) #Here csvr is an object of <class, _csv.DictReader>
        for record in csvdr:
            for k,v in record.items():
                print("\t{}---->{}".format(k,v))
        print("-"*50)
except FileNotFoundError:
    print("File Does not Exist")