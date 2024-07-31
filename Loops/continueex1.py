#program printing those characters except H and Y letters
#continueex1.py
s="PYTHON"
for x in s:
	if(x=='H') or (x=='Y'):
		continue
	print("\t",x)
else:
	print("I am in else... for loop")