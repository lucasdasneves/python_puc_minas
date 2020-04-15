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