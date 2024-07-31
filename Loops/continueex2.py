#PRogram to display +ve numbers and -ve numbers seperately
#continueex2.py
lst=[10,-20,30,40,-50,-60,70,0]
for val in lst:
	if(val<=0):
		continue
	print("\t",val)
print("="*20)
for val in lst:
	if(val>=0):
		continue
	print("\t",val)
