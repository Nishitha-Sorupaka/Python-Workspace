#RegExp4.py
import re
gd="Python is an oop Lang.Python is also Fun Prog Lang"
sd="Python"
matchTable=re.finditer(sd,gd) # here matchTable is an object of <class, 'callable_iterator'> 
print(matchTable,type(matchTable))
for match in matchTable:
	print("Start Index: {} \nEnd Index: {} \nValue: {}".format(match.start(),match.end(),match.group()))
	print("-"*50)

