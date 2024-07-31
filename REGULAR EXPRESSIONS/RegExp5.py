#Program for searching 'a' or 'b' or 'c' only
#RegExp5.py
import re
mattab=re.finditer('[abc]',"cAK@2aLp4#Gq8HbQw")
print("-"*50)
for mat in mattab:
	print("Start Index: {} End Index: {} Value: {}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)

'''

D:\Python-Workspace\REGULAR EXPRESSIONS>py RegExp5.py
--------------------------------------------------
Start Index: 0 End Index: 1 Value: c
Start Index: 5 End Index: 6 Value: a
Start Index: 14 End Index: 15 Value: b
--------------------------------------------------
'''