#dictionary with on more than one entity and for statement

pessoa = {
    'nome': 'Lea',
    'Idade': 21,
    'curso': 'computação',
    }

for chave, valor in pessoa.items(): #items show us a pairs of key-value
    print("Chave: " + str(chave))
    print("Valor: " + str(valor))        
    print()