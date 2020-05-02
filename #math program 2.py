#math program 2

var1 = float(input("Insert the first variable: "))
var2 = float(input("Insert the second variable: "))
op = input("Insert the operator code (1, 2, 3 or 4): ")

if op == '1': #warning !!: I need to put ==
    print("The result is: ", var1 + var2)
elif op == '2':
    print("The result is: ", var1 - var2)
elif op == '3':
    print("The result is: ", var1 * var2)
elif op == '4':
    print("The result is: ", var1 / var2)
else:
    print("Wrong operator selected")