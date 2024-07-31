#Program to Generate a bill where take inputs 1.QTY of items 2.price per item provided discount 10% and tax 14%
#billex1.py
#accept product name, price per item, qty of items required
pname=input("Enter Product Name: ")


#Validation of price
while(True):
	price=float(input("Enter price per Item: "))
	if(price>0):
		break
#Validation of Quantity
while(True):
	qty=int(input("Enter Quantity of Items required: "))
	if(qty>0):
		break
#validation of Discount
while(True):
	discount=int(input("Enter Discount of Items(%): "))
	if(discount>0):
		break
#validation of Tax
while(True):
	tax=int(input("Enter Tax of Items(%): "))
	if(tax>0):
		break
#Calculate discount and tax
discountTotal=(price*qty)*(discount/100)
taxTotal=(price*qty)*(tax/100)
total=qty*price
print(discountTotal)
print(taxTotal)

print("-"*50)
print("B I L L")
print("-"*50)
print("Quantity Sold: {} ".format(qty))
print("Price per Item: {}".format(price))
print("-"*50)
print("Total Amount: {}".format(total))
print("Discount: -{}".format(discountTotal))
print("-"*50)
print("Discounted Total: {}".format(total-discountTotal))
print("Tax: +{}".format(taxTotal))
print("-"*50)
print("Total Amount to be paid: {}".format(total-discountTotal+taxTotal))
print("-"*50)




