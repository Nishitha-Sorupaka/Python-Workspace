#Student.py -----File name acts as Module name
class Student:
    def __init__(self,sno,sname,marks):
        self.sno=sno
        self.sname=sname
        self.marks=marks
    def disStudData(self):
        print("{}\t{}\t{}".format(self.sno,self.sname,self.marks))