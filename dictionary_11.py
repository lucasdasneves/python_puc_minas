#dictionary and for statements with values method

linguagens = {
    'lea': 'python',
    'sara': 'c',
    'eddie': 'java',
    'phil': 'python',
}

for linguagem in linguagens.values(): #values method shows us the values of a dictionary
    print(linguagem.title())