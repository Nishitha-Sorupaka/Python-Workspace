#Program for adding Record to  CSV File by Python Program with csv module
#CsvWriteEx3.py-----csv.writer()  gives an object of <class, _csv.Writer>
import csv #Step-1
with open("emp.csv","a") as fp:
    while(True):
        print("-"*50)
        #Accepting Employee values from Keyboard
        empno=int(input("Enter Employee Number: "))
        ename=input("Enter Employee Name: ")
        sal=float(input("Enter Employee Salary: "))
        dsg=input("Enter Employee Designation: ")
        #Create an Empty List
        lst=[]
        #Append Employee Data to List object
        lst.append(empno)
        lst.append(ename)
        lst.append(sal)
        lst.append(dsg)
        #Create an object of csv.Writer
        csvwr=csv.writer(fp)
        #Write record data to csv file--writerow()
        csvwr.writerow(lst)
        print("Record Saved in a File: ")
        print("-" * 50)
        ch=input("Do you want to insert another record(yes/no)?")
        if(ch.lower()=="no"):
            break

