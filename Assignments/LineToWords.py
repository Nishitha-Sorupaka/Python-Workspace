#LineToWords.py
line=input("Enter a Line of Code you want to split into words: ")
words=line.split()
print("-"*50)
print(line)
print("-"*50)
for word in words:
	print("\t{}".format(word))
	for letter in word:
		print("\t\t{}".format(letter))
print("-"*50)