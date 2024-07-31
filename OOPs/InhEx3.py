#Program for demonstrating Inheritance
#InhEx3.py
class C1:
    def getA(self):
        self.a=10
class C2(C1):
    def getB(self):
        self.b=20
class C3(C2):
    def getC(self):
        self.c=30
    def operation(self):
        self.d=self.a+self.b+self.c
        print("Sum({},{},{})={}".format(self.a,self.b,self.c,self.d))

#main program
o3=C3()
print(o3.__dict__) #{}
o3.getA()
print(o3.__dict__) # {'a';10}
o3.getB()
print(o3.__dict__) # {'a';10,'b':20}
o3.getC()
print(o3.__dict__) #  {'a';10,'b':20,'c':30}
o3.operation()
print(o3.__dict__) #  {'a';10,'b':20,'c':30,'d':60}
