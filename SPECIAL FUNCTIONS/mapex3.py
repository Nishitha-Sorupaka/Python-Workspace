#mapex3.py
print("Enter Employee old salaries seperated by space:")
oldsallist=[float(x) for x in input().split()]
newsallist=list(map(lambda sal:sal*1.02,oldsallist))
print("\nOld Salary List={}".format(oldsallist))
print("New Salary List={}".format(newsallist))
print("\nOld Salary List:")
for oldsal in oldsallist:
	print("\t{}".format(oldsal))
print("New Salary List:")
for newsal in newsallist:
	print("\t{}".format(round(newsal,2)))

print("-"*50)
print("Old Salary\tNew Salary")
print("-"*50)
for old,new in zip(oldsallist,newsallist):
	print("\t{}\t{}".format(old,round(new,2)))
print("-"*50)