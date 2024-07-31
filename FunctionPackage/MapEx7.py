#Program to demonstrate map() function
#MapEx7.py

#main program
line=input("Enter line of words seperated by space:")
words=line.split()
print("Given words=",words)
rwords=list(map(lambda word:word[::-1],words))
print("Reversed words=",rwords)