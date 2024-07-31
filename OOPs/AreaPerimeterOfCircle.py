#Program for calculating Area and Perimeter of Circle using Classes and Object
#AreaPerimeterOfCircle.py
class Circle:
    pi=3.14 #here pi is Class level Data Member

#main program
obj=Circle() #here obj is an object
print("Content of obj= ",obj.__dict__)
print("--------------------------------")
obj.r=int(input("Enter the Radius of the Circle: "))
print("Content of obj= ",obj.__dict__)
print("--------------------------------")
#Calculating Area of Circle --- pi*r**2
obj.area=Circle.pi*(obj.r**2)
#Calculating Perimeter of Circle --- 2*pi*r
obj.peri=2*Circle.pi*obj.r
print("--------------------------------")
print("pi Value = {}".format(Circle.pi))
print("pi Value = {}".format(obj.pi))
print("Radius of Circle= {}".format(obj.r))
print("--------------------------------")
print("Area of Circle= {}".format(obj.area))
print("Perimeter of Circle= {}".format(obj.peri))
print("--------------------------------")
