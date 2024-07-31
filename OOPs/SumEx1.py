#Program for calculating addition of two numbers using Classes and Object
#SumEx1.py
class Sum:pass

#main program
s=Sum() #here s is called object
print("Content of s= ",s.__dict__)
print("--------------------------------")
s.k=int(input("Enter the value of k: "))
s.v=int(input("Enter the value of v: "))
print("Content of s= ",s.__dict__)
print("--------------------------------")
#add the values
s.r=s.k+s.v
print("First Value: {}".format(s.k))
print("Second Value: {}".format(s.v))
print("Sum= {}".format(s.r))
print("--------------------------------")
