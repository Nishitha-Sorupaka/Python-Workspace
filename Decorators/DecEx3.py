#DecEx3.py

def squareroot(getval):
    def operation():
        n=getval()
        res=n**0.5
        return res
    return operation


@squareroot
def getval():
    return int(input("Enter a number: "))


#main program
res=getval()
print("Square root = {}".format(res))