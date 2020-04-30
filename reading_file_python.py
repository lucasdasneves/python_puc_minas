#reading files in python

file = open('C:\\Users\\Samsung\\Documents\\GitHub\\python_puc_minas\\pessoas.txt','r')
for linha in file:
    lista = linha.split()
    print(lista)

file.close()