#anonymousfunex8.py

findbig = lambda l1: max(l1)
findsmall = lambda k: min(k)


#main program
print("Enter List of values seperated by space:")
lst=[int(x) for x in input().split()]
print("max({})={}".format(lst,findbig(lst)))
print("min({})={}".format(lst,findsmall(lst)))