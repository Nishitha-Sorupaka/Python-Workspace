#Program for Generating Pay Slip of a Employee
#a) Accept empno, empname and basicsal. 
#	if basicsal>=10000 then give
#		da=20%basicsal
#		ta=15%basicsal
#		hra=10%basicsal
#		ma=5%basicsal
#		gpf=2%basicsal
#		lic=3%basicsal
#	otherwise give (basicsal<10000)
#		da=25%basicsal
#		ta=20%basicsal
#		hra=15%basicsal
#		ma=6%basicsal
#		gpf=2%basicsal
#		lic=3%basicsal
#	calculate the netsal (netsal=[basicsal+da+ta+hra+ma]-[gpf+lic])
#	display Employee details and salary information
empno=int(input("Enter Employee Number:"))
empname=input("Enter Employee Name:")
basicsal=float(input("Enter Basic Salary"))
if(basicsal<=0):
	print("Invalid Basic Salary")
else:
	if(basicsal>=10000):
		da=basicsal*(20/100)
		ta=(15/100)*basicsal
		hra=(10/100)*basicsal
		ma=(5/100)*basicsal
		gpf=(2/100)*basicsal
		lic=(3/100)*basicsal
	else:
		da=(25/100)*basicsal
		ta=(20/100)*basicsal
		hra=(15/100)*basicsal
		ma=(6/100)*basicsal
		gpf=(2/100)*basicsal
		lic=(3/100)*basicsal
netsal=(basicsal+da+ta+hra+ma)-(gpf+lic)
print("=================================")
print("Employee Pay Slip Information")
print("=================================")
print("\tEmployee Number: {}".format(empno))
print("\tEmployee Name: {}".format(empname))
print("\tBasic Salary: {}".format(basicsal))
print("\tEmployee DA: {}".format(da))
print("\tEmployee TA: {}".format(ta))
print("\tEmployee HRA: {}".format(hra))
print("\tEmployee MA: {}".format(ma))
print("\tEmployee GPF: {}".format(gpf))
print("\tEmployee LIC: {}".format(lic))
print('------------------------------')
print("Net Salary of Employee: {}".format(netsal))
        

