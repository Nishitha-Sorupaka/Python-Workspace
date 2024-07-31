#PolyEx8.py
class Circle:
    def area(self,r): # Original method
        self.ac=3.14*r**2
        print("Area of Circle: {}".format(self.ac))

class Square():
    def area(self,s): # Original method
        self.sa=s**2
        print("Area of Square: {}".format(self.sa))
        print("-"*50)

class Rect(Circle,Square):
    def area(self,l,b): # Overridden Method
        self.ra=l*b
        print("Area of Rectangle: {}".format(self.ra))
        print("-" * 50)
        super().area(float(input("Enter Radius: ")))
        print("-" * 50)
        Square.area(self,float(input("Enter Side: ")))

#main program
r=Rect()
r.area(float(input("Enter Length: ")),float(input("Enter Breadth: ")))