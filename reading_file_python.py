#reading external files with python

file = open("pessoas.txt","r") #r means that the archive is set for reading
# for statements is used to run the rows from the file
#split command splits the rows, the space gives the reference
#close command is used to close the file
for row in file:
	list = row.split()
	print(list)

file.close()