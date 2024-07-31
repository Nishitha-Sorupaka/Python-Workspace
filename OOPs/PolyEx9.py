#PolyEx9.py
class Circle:
    def __init__(self,r): # Original Constructor
        self.ac=3.14*r**2
        print("Area of Circle: {}".format(self.ac))

class Square():
    def __init__(self,s): # Original Constructor
        self.sa=s**2
        print("Area of Square: {}".format(self.sa))
        print("-"*50)

class Rect(Circle,Square):
    def __init__(self,l,b): # Overridden Constructor
        self.ra=l*b
        print("Area of Rectangle: {}".format(self.ra))
        print("-" * 50)
        super().__init__(float(input("Enter Radius: ")))
        print("-" * 50)
        Square.__init__(self,float(input("Enter Side: ")))

#main program
r=Rect(float(input("Enter Length: ")),float(input("Enter Breadth: ")))