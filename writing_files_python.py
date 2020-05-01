#writing in files using python

materiais = ['caneta', 'caderno', 'livro']

file = open('materiais.txt','w')
for material in materiais:
    file.write(material + '\n')
    # \n is used to wrap the row
    #can I write my code in a Excel or SpreadSheets file?
    #https://stackoverflow.com/questions/9690138/how-do-i-access-read-write-google-sheets-spreadsheets-with-python

file.close()