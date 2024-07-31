#Non-IterEx.py
'''
s="Python"
itobj=iter(s)
while True:
    try:
        item=next(s)
        print(item)
    except StopIteration:
        break
        '''
mytuple=("apple","banana","cherry")
myiter=iter(mytuple)
print(type(myiter))
print("Content of iter=",myiter)
print(next(myiter))
print(next(myiter))
print(next(myiter))
#print(next(myiter))

