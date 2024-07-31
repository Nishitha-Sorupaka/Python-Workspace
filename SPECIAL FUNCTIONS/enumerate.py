'''s="PYTHON"
d={1:"Python",2:"SAP",3:"C++"}
for i,v in enumerate(s):
    print("Index: {}===> Value: {}".format(i,v))
for i,v in enumerate(d):
    print("Index: {}===> Value: {}".format(i,v))'''

x = 1
while True:
    if x % 5 == 0:
        break
    print(x)
    x+= 1

'''
try:
    s1=int(input("Enter a number:"))
    s2=int(input("Enter a number:"))
    sum=s1/s2
except ZeroDivisionError:
    print("Do not enter zero for denominator")
except ValueError:
    print("do not enter string,alnum or special symbols as input")
else:
    print("Sum({},{})={}".format(s1,s2,sum))
    print("else block")
finally:
    print("finally block")

'''

'''
i = 0
while i < 3:
    print(i)
    i+=1
else:
     print(0)
'''
'''
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)'''
'''
def fun1(*argu):
    for arg in argu: 
        print(arg)

fun1("Hello","to","Welcome","ABC")
''''''
def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])
'''