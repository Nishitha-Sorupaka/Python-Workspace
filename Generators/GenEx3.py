#GenEx3.py
def kvrrange(Begin,End):
    while(Begin<=End):
        yield Begin
        Begin+=1

#main program
g=kvrrange(10,20)
print(type(g))
print("Content of g=",g)
print("="*50)
while(True):
    try:
        print(next(g))
    except StopIteration:
        print("=" * 50)
        break
print("=" * 50)
g1=kvrrange(100,120)
print("="*50)
while(True):
    try:
        print(next(g1))
    except StopIteration:
        print("=" * 50)
        break