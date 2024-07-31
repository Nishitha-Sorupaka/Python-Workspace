#GenEx4.py
def kvrrange(Begin,End,Step):
    while(Begin<=End):
        yield Begin
        Begin+=Step
        #Begin=Begin+Step

#main program
g=kvrrange(10,20,2)
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
g1=kvrrange(100,120,3)
print("="*50)
while(True):
    try:
        print(next(g1))
    except StopIteration:
        print("=" * 50)
        break