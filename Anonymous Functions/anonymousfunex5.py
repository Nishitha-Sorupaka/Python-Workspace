#anonymousfunex5.py

findbig=lambda x,y,z: x if (x>y) and (x>z) else y if (y>z) and (y>x) else z
findsmall=lambda k,v,r: k if (k<v) and (k<r) else v if (v<r) and (v<k) else r

#main program
a=int(input("Enter First Value:"))
b=int(input("Enter Second Value:"))
c=int(input("Enter Third Value:"))
print("max({},{},{})={}".format(a,b,c,findbig(a,b,c)))
print("min({},{},{})={}".format(a,b,c,findsmall(a,b,c)))