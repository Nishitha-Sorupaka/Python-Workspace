#Program for creating CSV File by Python Program with csv module where the data is available in the form of dict
#CsvDictWriteEx1.py
import csv #Step-1
hname=["HTNO","NAME","BRANCH","CGPA"] # step-2
records=[ {"HTNO":100,"NAME":"VIVEK","BRANCH":"CSE","CGPA":8.0},
			  {"HTNO":200,"NAME":"NARESH","BRANCH":"ECE","CGPA":7.8},
			  {"HTNO":300,"NAME":"DINESH","BRANCH":"EEE","CGPA":8.1},
			  {"HTNO":400,"NAME":"AMOL","BRANCH":"IT","CGPA":7.7},
			  {"HTNO":500,"NAME":"SUJITH","BRANCH":"MECH","CGPA":8.3}] # Step-3
with open("univstud.csv","a") as fp: #Step-4
    csvdwr=csv.DictWriter(fp,fieldnames=hname) #Step-5
    csvdwr.writeheader() #Step-6
    csvdwr.writerows(records) #Step-7
    print("Dict Data Saved as records in CSV File:")