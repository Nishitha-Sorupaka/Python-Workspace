#FilterEx5.py
posvalue=lambda n:n>0 #Anonymous function
#main program
print("Enter the values seperated by space: ")
lst=[int(val) for val in input().split()]
pslist=list(filter(lambda n:n>0,lst))
nglist=list(filter(lambda n:n<0,lst))
print("Given List=",lst)
print("Positive Elements List",pslist)
print("Negative Elements List",nglist)