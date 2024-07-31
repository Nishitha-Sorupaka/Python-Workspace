#FilterEx2.py
def posvalue(n):
    if n>0:
        return True
    else:
        return False
#main program
lst=[10,23,-45,67,-78,12,-34,28]
pslist=list(filter(posvalue,lst))
print("Given List=",lst)
print("Positive Elements List=",pslist)