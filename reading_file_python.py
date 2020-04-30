#reading files in python

file = open("pessoas.txt","r")
for linha in file:
	lista = linha.split()
	print(lista)

file.close()