#Program to demonstrate map() function
#MapEx6.py

#main program
print("Enter line of words seperated by space:")
words=[word for word in input().split()]
print("Given words=",words)
rwords=list(map(lambda word:word[::-1],words))
print("Reversed words=",rwords)