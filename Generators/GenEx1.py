#GenEx1.py
def kvrrange(Val):
    i=0
    while(i<Val):
        yield i
        i+=1

#main program
g=kvrrange(5)
print(type(g))
print("Content of g=",g)
print("="*50)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g)) This statement generates Stopiteration because generates yielded all the demanded values