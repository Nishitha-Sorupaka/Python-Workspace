#Program to demonstrate map() function
#MapEx3.py
def hike(sal):
    return(sal+sal*(50/100))

#main program
def execute():
    print("Enter List of salaries of employees:")
    oldsal=[int(val) for val in input().split()]
    print("="*50)
    newsal=list(map(hike,oldsal))
    print("Old Salary List:",oldsal)
    print("New Salary List:",newsal)
    print("="*50)