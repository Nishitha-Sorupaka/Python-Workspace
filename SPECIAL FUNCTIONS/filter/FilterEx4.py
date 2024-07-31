#FilterEx4.py
posvalue=lambda n:n>0 #Anonymous function
#main program
print("Enter the values seperated by space: ")
lst=[int(val) for val in input().split()]
pslist=list(filter(posvalue,lst))
print("Given List=",lst)
print("Positive Elements List",pslist)