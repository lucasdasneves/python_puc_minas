#while example of a program to fill a dictionary

linguagens = {}

flag = True
while flag:
    nome = input("informe o seu nome: ")
    linguagem = input("Informe a lingaugem de programação: ")

    #armazena a resposta no dicionário
    linguagens[nome] = linguagem
    
    resposta = input("Há mais alguém para responder (s/n): ")
    if resposta == 'n':
        flag = False

for nome, linguagem in linguagens.items():
    print(nome + " tem preferência peta linguagem " + linguagem + ".")