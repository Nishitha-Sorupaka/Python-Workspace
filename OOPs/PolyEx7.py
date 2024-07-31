#PolyEx7.py
class Circle:
    def __init__(self): # Original Constructor
        self.r=float(input("Enter Radius: "))
        self.ac=3.14*self.r**2
        print("Area of Circle: {}".format(self.ac))

class Square():
    def __init__(self): # Original Constructor
        self.s=float(input("Enter Side: "))
        self.sa=self.s**2
        print("Area of Square: {}".format(self.sa))
        print("-"*50)

class Rect(Circle,Square):
    def __init__(self): # Overriden Constructor
        self.l=float(input("Enter Length: "))
        self.b = float(input("Enter Breadth: "))
        self.ra=self.l*self.b
        print("Area of Rectangle: {}".format(self.ra))
        print("-" * 50)
        super().__init__()
        print("-" * 50)
        Square.__init__(self)

#main program
r=Rect()