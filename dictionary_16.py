#dictionary example with two loops for

pessoas = {
    'leasilva': { 
    'nome': 'Lea',
    'sobrenome': 'Silva',
    'curso': 'computação',
},

'eddiesilva': {
    'nome': 'Eddie',
    'sobrenome': 'Silva',
    'curso': 'computação',
}
}

for username, userinfo in pessoas.items():
    print("Usuário: " + username)
    for chave, valor in userinfo.items():
        print(chave + ": " + valor)
    print()