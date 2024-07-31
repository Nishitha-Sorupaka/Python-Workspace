#Program for Converting Dict Type data inyto #Program for Converting JSON data ----json.dump()
#DictDataToJsonFile.py
import json
dictobj={"ENO":100,"ENAME":"Rossum","SAL":45.67,"CNAME":"PSF"}
print(dictobj,type(dictobj))
#Open the JSON file in WRITE mode
with open("emp.json","w") as fp:
	json.dump(dictobj,fp)
	print("Dict Object data Saved in JSON File--Verify")
