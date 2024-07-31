#Program to demonstrate map() function
#MapEx5.py

#main program
print("Enter List of salaries of employees:")
oldsal=[int(val) for val in input().split()]
print("="*50)
newsal=list(map(lambda sal:sal+sal*(50/100),oldsal))
print("Old Salary List:",oldsal)
print("New Salary List:",newsal)
print("="*50)