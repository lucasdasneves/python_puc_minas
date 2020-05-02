#dictionary inisde an other dictionary

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

for username , userinfo in pessoas.items():
    print("Usuário: " + username)
    print("Curso: " + userinfo['curso'])