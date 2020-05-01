#writing in files using python

materiais = ['caneta', 'caderno', 'livro']

file = open('materiais.txt','w')
for material in materiais:
    file.write(material + '\n')
    # \n is used to wrap the row

file.close()