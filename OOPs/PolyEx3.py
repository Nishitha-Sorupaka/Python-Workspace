#Program for demonstrating Polymorphism
#PolyEx3.py
class C1:
    def __init__(self): # Default Constructor
        print("C1---default Constructor")
class C2(C1):
    def __init__(self): # Overridden Constructor
        super().__init__()
        print("C2---Overridden Constructor")
class C3(C2):
    def __init__(self): # Overridden Constructor
        super().__init__()
        print("C3---Overridden Constructor")

#main program---we created 1 objects
print("w.r.t C3 Class")
o3=C3() # Object Creation---calls Constructor