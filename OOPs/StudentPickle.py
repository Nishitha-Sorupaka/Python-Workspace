#Program for saving the details of Student in studentpick file
#StudentPickle.py
import pickle
from Student import Student
class StudentPickle:
    def saveStudData(self):
        with open("studpick.data","ab") as fp:
            #accept the student data from keyboard
            print("-"*50)
            sno=int(input("Enter Student Number: "))
            sname = input("Enter Student Name: ")
            marks = float(input("Enter Student Marks: "))
            s=Student(sno,sname,marks) #object creation PVM calls Parameterized Constructor
            print("-" * 50)
            pickle.dump(s,fp)
            print("Student Record Saved Successfully")
            print("-" * 50)
