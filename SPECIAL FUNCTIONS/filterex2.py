#filterex2.py
decide=lambda n: n>0
#decide=lambda n: True if n>0 else False 

#main program
lst=[10,20,30,-50,-11,-21,0,44,22,-9,12]
a=filter(decide,lst)
print("Type of a=",type(a)) # <class,'filter'>
print("content of a=",a)
#convert filter object into list type
pslist=list(a)
print("Positive Elements=",pslist)