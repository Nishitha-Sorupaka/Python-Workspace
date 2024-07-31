#GenEx5.py
def getcources():
    yield "PYTHON"
    yield "JAVA"
    yield "DSA"
    yield "DSC"

#main program
crs=getcources()
print(next(crs))
print(next(crs))
print(next(crs))
print(next(crs))
