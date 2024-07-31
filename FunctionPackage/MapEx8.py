#Program to demonstrate map() function
#MapEx8.py
def listsum(a,b):
    return a+b
#main program
print("Enter list of values for First List: ")
lst1=[int(val) for val in input().split()]
print("Enter list of values for Second List: ")
lst2=[int(val) for val in input().split()]
lst3=list(map(listsum,lst1,lst2))
print("{}+{}={}".format(lst1,lst2,lst3))