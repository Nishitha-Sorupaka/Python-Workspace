#Program for creating CSV file by Python Program with csv module
#CsvWriteEx1.py--------csv.writer()  gives an object of <class, _csv.Writer>
import csv #Step-1
hnames=["empno","ename","sal","dsg"]   #Step-2
records=[[10,"RS",3.4,"Author"],[20,"TR",4.4,"Scientist"],
				   [30,"DR",1.4,"SE"],
				   [40,"ST",2.4,"TL"],
				   [50,"GS",1.4,"HR"]] #Step-3
with open("emp.csv","a") as fp: #Step-4
    csvwr=csv.writer(fp) #Step-5--here csvwr is an object of <class, _csv.Writer>
    #Here write Header names to the csv file---writerow() present in the object of <class, _csv.Writer>
    csvwr.writerow(hnames) #Step-6
    #Write the records which are in the form of nested list--writerows()
    csvwr.writerows(records) #Step-7
    print("CSV file Created. Verify..!")





