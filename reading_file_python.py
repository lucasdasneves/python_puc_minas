#reading files in python

file = open('pessoas.txt','r')
for linba in file:
    lista = linha.split()
    print(lista)

file.close()