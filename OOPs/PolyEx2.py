#Program for demonstrating Polymorphism
#PolyEx2.py
class C1:
    def disp(self): # Original Method
        print("C1---disp()")
class C2(C1):
    def disp(self): # Overridden Method
        print("C2---disp()")
class C3(C2):
    def disp(self): # Overridden Method
        C1.disp(self)
        C2.disp(self)
        print("C3---disp()")

#main program---we created 2 objects
print("w.r.t C3 Class")
o3=C3()
o3.disp()