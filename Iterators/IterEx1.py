#IterEx1.py
lst=[10,20,30,40,50,60,70,80,90]
myiter=iter(lst)
print(type(lst))
print(type(myiter))
print("Content of iter=",myiter)
'''print(next(myiter))
print(next(myiter))
print(next(myiter))'''
while(True):
    try:
        print(next(myiter))
    except StopIteration:
        break