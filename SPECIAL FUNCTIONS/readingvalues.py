#readingvalues.py
#program for reading list of values dynamically from KBD
print("Enter the elements dynamically from KBD seperated by space:")
lst=[int(x) for x in input().split()] #List comprehension
print("Content of list=",lst)

print("Enter the elements dynamically from KBD seperated by comma:")
lst1=[float(x) for x in input().split(",")] #List comprehension
print("Content of list=",lst1)

print("Enter the elements dynamically from KBD seperated by #:")
lst2=[str(x) for x in input().split("#")] #List comprehension
print("Content of list=",lst2)