#while statement and the break command

while True:
    mensagem = input("Escreva algo ('sair' para temrinar): ")
    if mensagem == 'sair':
        break
    else:
        print(mensagem)