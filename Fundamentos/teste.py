numero = 1

while True: # Repetição infinita.
    
    if numero < 51:
        numero += 1
    if numero > 50:
        break
    elif numero % 2 == 0: # trocar o sinal de igual (==) por dirente (!=) para exibir números ímpares.
        continue
    print (numero, end=" ")