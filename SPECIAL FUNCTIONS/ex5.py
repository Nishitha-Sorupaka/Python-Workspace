#ex5.py
#WAp wich will accept list of values and find the squares of positive and negative list of elements seperately
print("Enter the numbers from KBD seperated by space:")
lst=[int(x) for x in input().split()]
obj1=list(map(lambda n:n**2,filter(lambda n:n>0,lst)))
print(obj1)
obj2=list(map(lambda n:n**2,filter(lambda n:n<0,lst)))
print(obj2)
print("-"*50)
print("Original List:{}".format(lst))
print("-"*50)
print("Positive Squares of Given Numbers:{}".format(obj1))
print("Negative Squares of Given Numbers:{}".format(obj2))
print("-"*50)