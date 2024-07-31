#filterex5.py

print("Enter the Elements:")
lst=[int(x) for x in input().split()] #list comprehension
print("Content of List=",lst)
print("-"*50)
print("Original Elements of list:{}".format(lst))
print("-"*50)
pslist=list(filter(lambda n:n>0,lst))
nslist=set(filter(lambda k:k<0,lst))
zerolist=tuple(filter(lambda k:k==0,lst))
print("Positive ELements={}".format(pslist))
print("Negative ELements={}".format(nslist))
print("Zero ELements={}".format(zerolist))