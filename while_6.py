#while, lists and dictionaries

materiais = ['caneta', 'caderno', 'livro', 'lápis']
objetos = []

while materiais:
    objeto = materiais.pop()
    objetos.append(objeto)

for objeto in objetos:
    print(objeto.title())