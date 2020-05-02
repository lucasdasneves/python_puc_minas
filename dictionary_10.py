#dictionary examples with for statement

linguagens = {
    'lea': 'python',
    'sara': 'c',
    'eddie': 'java',
    'phil': 'python',
}

for nome in linguagens.keys(): #keys is a method to shows us only the keys from a dictionary
    print(nome.title())