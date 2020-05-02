#using flags and while

flag = True
while flag:
    mensagem =input("Escreva algo ('sair' para terminar): ")
    if mensagem == 'sair':
        flag = False
    else:
        print(mensagem)

        #com esse código, enquanto eu não digitar 'sair', o programa não para de se executar.