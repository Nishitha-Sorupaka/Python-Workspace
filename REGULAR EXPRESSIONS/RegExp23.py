#Program for searching exactly one 'k'
#RegExp23.py
import re
mattab=re.finditer("k","kvkkvkkkvkv")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp23.py
--------------------------------------------------
Start Index: 0 End Index: 1 Value: k
Start Index: 2 End Index: 3 Value: k
Start Index: 3 End Index: 4 Value: k
Start Index: 5 End Index: 6 Value: k
Start Index: 6 End Index: 7 Value: k
Start Index: 7 End Index: 8 Value: k
Start Index: 9 End Index: 10 Value: k
--------------------------------------------------
'''