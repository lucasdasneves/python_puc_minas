#lists inside a dictionary example 2 with for statements

pessoa = {
    'nome' : ' Lea',
    'curso': 'computação',
    'linguagens': ['python', 'c', 'java']
}

for linguagem in pessoa ['linguagens']:
    print(linguagem.title())