#Assignments
#1)Program: Write a python program which will accept length & breadth from keyboard and calculate Area & Circumference of rectangle?
#Area of Rectangle=length*breadth
#Circumference of Rectangle=2*(length+breadth)
length=int(input("Enter the length of Rectangle:"))
breadth=int(input("Enter the Breadth of Rectangle:"))
#cal area and circum
area=length*breadth
circum=2*(length+breadth)
#display length, breadth, area and circum
print("=======================")
print("Length=" ,length)
print("breadth=" ,breadth)
print("Area of Rectangle=" ,area)
print("Circumference of Rectangle",circum)
print("=======================")