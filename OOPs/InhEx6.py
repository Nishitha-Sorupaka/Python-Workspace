#Program for demonstrating Inheritance
#InhEx6.py  Univ getunivdet(uname,uloc) dispunivdet College getcolldet(cname,cloc) dispcolldet
# Student getstuddet(sno,sname,crs) dispstuddet
class Univ:
    def getunivdet(self):
        self.uname=input("Enter University Name: ")
        self.uloc=input("Enter University Location: ")
    def dispunivdet(self):
        print("-"*50)
        print("University Name: {}".format(self.uname))
        print("University Location: {}".format(self.uloc))
        print("-" * 50)

class College(Univ):
    def getcolldet(self):
        self.cname=input("Enter College Name: ")
        self.cloc=input("Enter College Location: ")
    def dispcolldet(self):
        print("-"*50)
        print("College Name: {}".format(self.cname))
        print("College Location: {}".format(self.cloc))
        print("-" * 50)

class Student(College):
    def getstuddet(self):
        self.getunivdet()
        self.getcolldet()
        self.sno=int(input("Enter Student Number: "))
        self.sname=input("Enter Student Name: ")
        self.crs=input("Enter Student Course: ")
    def dispstuddet(self):
        self.dispunivdet()
        self.dispcolldet()
        print("-"*50)
        print("Student Number: {}".format(self.sno))
        print("Student Name: {}".format(self.sname))
        print("Student Course: {}".format(self.crs))
        print("-" * 50)

'''u=Univ()
u.getunivdet()
u.dispunivdet()
c=College()
c.getcolldet()
c.dispcolldet()'''
s=Student()
'''s.getunivdet()
s.dispunivdet()
s.getcolldet()
s.dispcolldet()'''
s.getstuddet()
s.dispstuddet()

