#anonymousfunex2.py
rectarea=lambda l,b:l*b

#main program
l=int(input("Enter Length: "))
b=int(input("Enter Breadth: "))
area=rectarea(l,b)
print("Area of Rectangle : {}*{}={}".format(l,b,area))