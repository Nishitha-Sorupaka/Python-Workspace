# Program for Reading the data from CSV File by using CSV Module in the form Dict
# CsvDictReaderEx2.py
import csv

with open("student.csv", "r") as fp:
    csvdr = csv.DictReader(fp)  # here csvdr is an object of type <class, csv.DictReader>
    for drdata in csvdr:
        for k, v in drdata.items():
            print("\t{}--->{}".format(k, v))
        print("------------------------------------------")

