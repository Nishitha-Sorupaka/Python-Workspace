#Program for accepting list of names and sort them in both ascending and descending order 
#sortnames.py--file name and acts as Module Name
#(sortnames.cpython-310.pyc)

def readnames():
	print("Enter List of Names seperated by Space:")
	lst=[str(names) for names in input().split()]
	return lst


def dispnames(names):
	print("-"*50)
	for name in names:
		print("\t{}".format(name))
	else:
		print("-"*50)

def sortnames():
	names=readnames()
	print("-"*50)
	print("Original Names: {}".format(names))
	print("-"*50)
	names.sort()
	print("Ascending Order: ")
	dispnames(names)
	print("-"*50)
	names.sort(reverse=True)
	print("Descending Order: ")
	dispnames(names)
	print("-"*50)


#sortnames()
