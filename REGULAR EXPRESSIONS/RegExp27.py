#Program for searching All Values in given data
#RegExp27.py
import re
mattab=re.finditer(".","kvkkvkkkvkv")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp27.py
--------------------------------------------------
Start Index: 0 End Index: 1 Value: k
Start Index: 1 End Index: 2 Value: v
Start Index: 2 End Index: 3 Value: k
Start Index: 3 End Index: 4 Value: k
Start Index: 4 End Index: 5 Value: v
Start Index: 5 End Index: 6 Value: k
Start Index: 6 End Index: 7 Value: k
Start Index: 7 End Index: 8 Value: k
Start Index: 8 End Index: 9 Value: v
Start Index: 9 End Index: 10 Value: k
Start Index: 10 End Index: 11 Value: v
--------------------------------------------------
'''