#Program to Generate a Electricity bill provided taking Service Number, Consumer Name, Number of units consumed as inputs provided:
	# Rates for units
	# 0 to 100---------per unit Rs. 5
	# 101 to 200---------per unit Rs. 7.5
	# 201 to 300---------per unit Rs. 10
	# above 300 ---------per unit Rs. 12
#billex2.py
#Validating Service Number
while(True):
	servicenumber=int(input("Enter Service Number: "))
	if(servicenumber>0):
		break

#Consumer name input
consumername=input("Enter Consumer Name: ")

#Validating No. of Units Consumed
while(True):
	units=int(input("Enter Number of Units Consumed: "))
	if(units>0):
		break
print("="*50)
print("ELECTRICITY BILL")
print("-"*50)
print("Service Number: {} ".format(servicenumber))
print("Consumer Name: {} ".format(consumername))
print("Number of Units Consumed: {}".format(units))
print("-"*50)
if(units<=100):
	print("Total Price: {}".format(units*5))
elif(units>=101 and units<=200):
	print("Total Price: {}".format((100*5)+((units-100)*7.5)))
elif(units>=201 and units<=300):
	print("Total Price: {}".format((100*5)+(100*7.5)+((units-200)*10)))
else:
	print("Total Price: {}".format((100*5)+(100*7.5)+(100*10)+(units-300)*12))

print("-"*50)

print("-"*50)




