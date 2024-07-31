#FilterEx6.py
print("Enter values seperated by space: ")
lst=[int(val) for val in input().split()]
evenlist=list(filter(lambda n:n%2==0,lst))
oddlist=set(filter(lambda n:n%2!=0,lst))
print("Given List=",lst)
print("Even Numbers List",evenlist)
print("Odd Numbers List",oddlist)