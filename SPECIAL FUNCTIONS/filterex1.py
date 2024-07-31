#Program for demonstrating filter() method
#filterex1.py
lst=[10,20,30,-50,-11,-21,0,44,22,-9,12]
def decide(n):
	if n>0:
		return True
	else:
		return False

#main program
a=filter(decide,lst)
print("Type of a=",type(a)) # <class,'filter'>
print("content of a=",a)
#convert filter object into list type
pslist=list(a)
print("Given List=",lst)
print("Positive Elements=",pslist)