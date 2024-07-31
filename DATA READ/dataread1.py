#Write a python program which can accept any two numerical values and multiply them? 
print("Enter two values: ")
a=input()
b=input()
x1=float(a)
x2=float(b)
x3=x1*x2
print("Value of a={} and is type={}".format(a,type(a)))

print("Value of b={} and is type={}".format(b,type(b)))
print("mul({},{}) = {}".format(x1,x2,x3))
print("mul(%0.2f,%0.2f)=%0.2f" %(x1,x2,x3))