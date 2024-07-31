def square(getval):
    def operation():
        n=getval()
        res=n**2
        return res
    return operation
@square
def getval():
    return int(input("Enter any value:"))


#main program
res=getval()
print("Square={}".format(res))