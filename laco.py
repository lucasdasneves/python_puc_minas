materiais = ['caneta', 'caderno', 'livro', 'lapis']
print(materiais)

#printing each element from the list

materiais = ['caneta', 'caderno', 'livro', 'e-book']
for material in materiais :
    print(material) #this is the for body
    print(material.title())
    print(len(materiais))

# "for" makes variable "material" write each element from the list per time

#numeric lists. In python we use Range to generate number in "for"

for valor in range(1,5):
    print(valor)

numeros = list(range(1,6))
print(numeros)

for numeros in range(1,7):
    print(numeros)

quadrados = []
for valor in range(1,11):
    quadrado = valor ** 2
    quadrados.append(quadrado)
print(quadrados)
#square os a list numbers

digitos = [1,2,3,4,5,6,7,8,9,0]
print(min(digitos))
print(max(digitos))
print(sum(digitos))
# stats basics

materiais = ['caneta','caderno','livro','e-book']
print(materiais[0:4])
# manipulating some list contents

materiais = ['caneta','caderno','livro','e-book','etc']
print(materiais[2:])
# manipulating some list contents

materiais = ['caneta','caderno','livro','e-book']
objetos = materiais[1:3]
print(materiais)
print(objetos)

materiais = [1,2,3,4]
objetos = materiais
objetos.append(5)
print(materiais)
print(objetos)

meteriais = [1,2,3,4]
objetos = materiais[:]
objetos.append(5)
print(materiais)
print(objetos)