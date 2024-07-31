#PolyEx5.py
class Circle:
    def area(self):
        self.r=float(input("Enter Radius: "))
        self.ac=3.14*self.r**2
        print("Area of Circle: {}".format(self.ac))

class Square(Circle):
    def area(self):
        self.s=float(input("Enter Side: "))
        self.sa=self.s**2
        print("Area of Square: {}".format(self.sa))
        print("-"*50)
        super().area()

class Rect(Square):
    def area(self):
        self.l=float(input("Enter Length: "))
        self.b = float(input("Enter Breadth: "))
        self.ra=self.l*self.b
        print("Area of Rectangle: {}".format(self.ra))
        print("-" * 50)
        super().area()

#main program
r=Rect()
r.area()