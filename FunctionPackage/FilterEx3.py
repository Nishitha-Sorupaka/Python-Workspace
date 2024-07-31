#FilterEx3.py
def posvalue(n):
    if n>0:
        return True
    else:
        return False
#main program
print("Enter the values seperated by space: ")
lst=[int(val) for val in input().split()]
pslist=list(filter(posvalue,lst))
print("Given List=",lst)
print("Positive Elements List",pslist)