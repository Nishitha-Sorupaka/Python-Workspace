#divdemo.py
from div import division
from kvr import KvrDivisionError
try:
	x=int(input("Enter First Value:"))
	y=int(input("Enter Second Value:"))
	res=division(x,y)
except KvrDivisionError:
	print("\nDo not enter Zero for Denominator")
except ValueError:
	print("\nDo not enter strs,symbols, alpha-numerics")
else:
	print("Result={}".format(res))
finally:
	print("\nI am from finally block")