#while statement and the continue command

contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0: #mod (%) the rest of the equation is zero
        continue
    print(contador)