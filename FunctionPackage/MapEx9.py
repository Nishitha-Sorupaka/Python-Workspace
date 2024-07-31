#Program to demonstrate map() function
#MapEx9.py
def listsum(a,b):
    return a+b
#main program
print("Enter list of values for First List: ")
lst1=[int(val) for val in input().split()]
print("Enter list of values for Second List: ")
lst2=[int(val) for val in input().split()]
lst3=list(map(listsum,lst1,lst2))
print("="*50)
print("\tlst1  +  lst2  = lst3")
for v1,v2,v3 in zip(lst1,lst2,lst3):
    print("\t{} {}  {}".format(lst1,lst2,lst3))
print("="*50)

print("="*50)
print("{}+{}={}".format(lst1,lst2,lst3))