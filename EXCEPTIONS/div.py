#div.py-----file name acts as a module name
from kvr import KvrDivisionError
def division(a,b):
	if(b==0):
		raise KvrDivisionError
	else:
		return(a/b)


#here division(-,-) is a common function