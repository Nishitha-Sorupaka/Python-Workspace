#Program to demonstrate the concept of logical operators
#Logical Operators
#lop.py
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float(input("Enter value of c:"))
print("({}<{})and({}<{})={}".format(a,b,a,c,(a<b)and(a<c)))
print("({}<{})and({}=={})={}".format(a,b,a,c,(a<b)and(a==c)))
print("({}>{})or({}<{})={}".format(a,b,a,c,(a<b)or(a<c)))
print("({}>{})or({}>{})={}".format(a,b,a,c,(a>b)or(a>c)))
print("not({}=={})and({}!={})={}".format(a,b,b,c,not(a==b)and(b!=c)))
print("not({}!={})and({}>{})={}".format(a,b,b,c,not(a!=b)or(b>c)))