#GenEx2.py
def kvrrange(val):
    i=0
    while(i<=val):
        yield i
        i=i+1

#main program
g=kvrrange(10)
print(type(g))
print("Content of g=",g)
print("="*50)
while(True):
    try:
        print(next(g))
    except StopIteration:
        print("=" * 50)
        break