#Program for searching zero 'k' or one 'k'
#RegExp26.py
import re
mattab=re.finditer("k?","kvkkvkkkvkv")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp26.py
--------------------------------------------------
Start Index: 0 End Index: 1 Value: k
Start Index: 1 End Index: 1 Value:
Start Index: 2 End Index: 3 Value: k
Start Index: 3 End Index: 4 Value: k
Start Index: 4 End Index: 4 Value:
Start Index: 5 End Index: 6 Value: k
Start Index: 6 End Index: 7 Value: k
Start Index: 7 End Index: 8 Value: k
Start Index: 8 End Index: 8 Value:
Start Index: 9 End Index: 10 Value: k
Start Index: 10 End Index: 10 Value:
Start Index: 11 End Index: 11 Value:
--------------------------------------------------
'''