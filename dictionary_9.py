#dictionary example with for statements

linguagens = {
    'lea': 'python',
    'sara': 'c',
    'eddie': 'java',
    'phil': 'python',
}

for nome, linguagem in linguagens.items():
    print(nome.title()+ " programa em " + linguagem.title())