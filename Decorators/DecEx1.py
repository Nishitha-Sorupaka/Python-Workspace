#DecEx1.py
def getval():
    return int(input("Enter any value:"))

def square(getval):
    def operation():
        n=getval()
        res=n**2
        return res
    return operation


operation=square(getval)
res=operation()
print("Square={}".format(res))