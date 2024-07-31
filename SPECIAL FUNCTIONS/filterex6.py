#filterex6.py
print("Enter the elements dynamically from KBD seperated by space:")
lst=[int(x) for x in input().split()]
print("-"*50)
print("Original Elements of list:{}".format(lst))
print("-"*50)
even=list(filter(lambda n: n%2==0,lst))
print("Even numbers in the list={}".format(even))
odd=list(filter(lambda n: n%2!=0,lst))
print("Odd numbers in the list={}".format(odd))
