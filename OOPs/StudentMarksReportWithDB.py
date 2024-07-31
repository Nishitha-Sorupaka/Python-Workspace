#StudentMarksReportWithDB.py
import mysql.connector
class StudentMarksReport:
    def __init__(self):
            #Validation of Student Number
            while(True):
                self.sno=int(input("Enter Student Number: "))
                if(self.sno>0):
                    break
                print("\t{} is Invalid Student Number".format(self.sno))
            #Accepting Student Name
            self.sname=input("Enter Student Name: ")
            #Validating of C lang Marks(0-100)
            while(True):
                self.cm=int(input("Enter Marks in C: "))
                if(self.cm>=0 and self.cm<=100):
                    break
                print("\t{} is invalid Marks in C".format(self.cm))
            #Validating of CPP lang Marks(0-100)
            while(True):
                self.cppm=int(input("Enter Marks in CPP: "))
                if(self.cppm>=0 and self.cppm<=100):
                    break
                print("\t{} is invalid Marks in CPP".format(self.cppm))
            #Validating of PYTHON lang Marks(0-100)
            while(True):
                self.pym=int(input("Enter Marks in PYTHON: "))
                if(self.pym>=0 and self.pym<=100):
                    break
                print("\t{} is invalid Marks in C".format(self.pym))
    def compute(self):
        self.totMarks=self.cm+self.cppm+self.pym
        self.per=(self.totMarks/300)*100
        #Deciding the Grade
        if(self.cm<40 or self.cppm<40 or self.pym<40):
            self.result="FAIL"
        else:
            if(self.totMarks>=250 and self.totMarks<=300):
                self.result="DISTINCTION"
            elif(self.totMarks>=200 and self.totMarks<=249):
                self.result ="FIRST"
            elif (self.totMarks >= 150 and self.totMarks <=199):
                self.result = "SECOND"
            elif (self.totMarks >= 120 and self.totMarks <=149):
                self.result = "THIRD"
    def disMarksReport(self):
        #printing the result
        print("-"*50)
        print("STUDENT MARKS REPORT")
        print("-" * 50)
        print("\tStudent Number: {}".format(self.sno))
        print("\tStudent Name: {}".format(self.sname))
        print("\tStudent Marks in C language: {}".format(self.cm))
        print("\tStudent Marks in CPP language: {}".format(self.cppm))
        print("\tStudent Marks in PYTHON language: {}".format(self.pym))
        print("-" * 50)
        print("\tTOTAL MARKS = {}".format(self.totMarks))
        print("\tPERCENTAGE = {}".format(self.per))
        print("\tGRADE = {}".format(self.result))
        print("-" * 50)
    def saveStudentData(self):
        try:
            con = mysql.connector.connect(host="127.0.0.1", user="root", passwd="root", database="batch6pm")
            cur = con.cursor()
            iq="insert into result values(%d,'%s',%d,%d,%d,%d,%f,'%s')"
            cur.execute(iq %(self.sno,self.sname,self.cm,self.cppm,self.pym,self.totMarks,round(self.per,2),self.result))
            con.commit()
            print("{} Student Record Inserted---verify".format(cur.rowcount))
        except mysql.connector.DatabaseError as db:
            print("Problem in db:",db)


#main program
s=StudentMarksReport()
s.compute()
s.disMarksReport()
s.saveStudentData()