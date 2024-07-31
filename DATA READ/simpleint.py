#Program for calculating simple interest and total amount to pay
#simpleint.py
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
#cal si and totamt
si=(p*t*r)/100
totamt=p+si
#display the values
print("==================================")
print("\tR E S U L T S")
print("==================================")
print("Principle Amount={}".format(p))
print("Time ={}".format(t))
print("Rate of Interest={}".format(r))
print("---------------------------------")
print("Simple Interest={}".format(si))
print("Total Amount to Pay={}".format(totamt))
print("==================================")