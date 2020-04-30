#reading external files with python

file = open("pessoas.txt","r")
for row in file:
	list = row.split()
	print(list)

file.close()