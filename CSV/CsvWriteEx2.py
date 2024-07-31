#Program for adding Record to CSV file by Python Program with csv module
#CsvWriteEx2.py----csv.writer() gives an object of <class, _csv.Writer>
import csv #Step-1
record=[60,"KVR",0.0,"Trainer"]
with open("emp.csv","a") as fp:
    csvwr=csv.writer(fp)
    csvwr.writerow(record)
    print("Record saved in a file")