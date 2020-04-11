#Calculadora

operacao = input("Qual a conta? Insira: + ou - ou * ou / ")
num1 = float(input("Digite o número 1: " ))
num2 = float(input("Digite o número 2: " ))

if operacao == '+':
    print(num1 + num2)

elif operacao == "-":
    print(num1 - num2)

elif operacao == "*":
        print(num1 * num2)

elif operacao == "/":
    print(num1 / num2)

else: print("Digite algum valor válido")
#falta ainda acrescentar a raiz quadrada