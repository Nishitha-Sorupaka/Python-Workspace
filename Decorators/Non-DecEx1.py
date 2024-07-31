#Non-DecEx1.py
def getval():
    return int(input("Enter any value:"))

def square():
    n=getval()
    res=n**2
    return res

def squareroot():
    n=getval()
    res=n**0.5
    return res

def cube():
    n=getval()
    res=n**3
    return res

#main program
res=square()
print("Square ={}".format(res))
res=squareroot()
print("Squareroot ={}".format(res))
res=cube()
print("Cube ={}".format(res))