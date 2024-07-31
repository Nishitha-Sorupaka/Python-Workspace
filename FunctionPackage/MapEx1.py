#Program to demonstrate map() function
#MapEx1.py
def hike(sal):
    return(sal+sal*(50/100))

#main program
oldsal=[10,15,5,20,30,16]
obj=map(hike,oldsal)
print("Type of obj={}".format(type(obj)))
print("="*50)
newsal=list(obj)
print("Old Salary List:",oldsal)
print("New Salary List:",newsal)
print("="*50)