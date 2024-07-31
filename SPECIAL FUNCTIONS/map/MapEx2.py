#Program to demonstrate map() function
#MapEx2.py
def hike(sal):
    return(sal+sal*(50/100))

#main program
oldsal=[10,15,5,20,30,16]
print("="*50)
newsal=list(map(hike,oldsal))
print("Old Salary List:",oldsal)
print("New Salary List:",newsal)
print("="*50)