#mapex4.py
print("Enter list of elements seperated by space:")
lst=[float(val) for val in input().split()]
sqlist=tuple(map(lambda val:val**2,lst))
clist=tuple(map(lambda val:val**3,lst))
sqrt=tuple(map(lambda val:val**0.5,lst))
print(lst,sqlist,clist,sqrt)
print("-"*50)
print("Given Value\tSquare\tCubes\tSquareRoot")
print("-"*50)
for n,sq,c,r in zip(lst,sqlist,clist,sqrt):
	print("\t{}\t{}\t{}\t{}".format(n,sq,c,round(r,2)))
print("-"*50)