    # São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.

# Receba um número do teclado e exiba os 2 números seguintes
a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)

# Receba um número do teclado e exiba os 2 números seguintes:

# a = int(input("Informe um número inteiro: "))
# print(a)

# repita 2 vezes:
# a += 1
# print(a)


    # Comando For:
# O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

texto = (input("Informe um Texto: "))
VOGAIS = "AEIOU"

for letra in texto:  
    if letra.upper() in VOGAIS:
        print (letra, end=" ") # o argumento (end=" ") serve para em vez de mostrar cada repetição em um linha, seja mostrado tudo na msm linha separado por um espaço entre eles.
else:       # Embora não seja muito utilizado, e desnecessário neste caso tbm podemos utilizar o else junto com o for (for/else), para manter o código depois do for no msm bloco.
    print ()
# no exemplo acima "letra" é como se fosse uma variável que da nome ao for, e deve ser usada dentro do for para se referir a ele, "in" é onde vc vai apontar para o for acontecer, no caso acima na variável texto (que vai receber input do usuário), o for vai transformar as letras que vem da variável texto em maiúsculas, com o argumento (.upper), para comparar com a constante VOGAIS que tem seu conteúdo em maiúsculo, e por fim vai dar print apenas nas letras que coincidem nas duas variáveis.

    #Função Range:
# Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido: i, i+1, i+2, i+3, ..., j-1.
# Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step opcional.

list(range(6)) #sem o list na frente, o resultado seria (0,6), porém desta forma fica [0,1,2,3...]

for numero in range (0,11): # Não é necessário o uso do (0,11) pois já inicia em "0".
    print(numero, end=" ")

# Tabuada do "5":
for numero in range (0, 51, 5): # "0" Start "51" Stop e "5" Step (de quanto em quanto vai contar).
    print (numero, end=" ")

    # Comando While:
# O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print ("Obrigado por usar nosso sistema bancário, até logo!")
    
    #break e continue:
#break para o código se uma determinada condição for atendida
#já o continue pula o código que vem depois dele e continua a repetição quando uma condição é atendida.

#Exibindo apenas números pares ou ímpares dentro de uma sequencia:

numero = 1

while True: # Repetição infinita.
    
    if numero < 51:
        numero += 1
    if numero > 50:
        break
    elif numero % 2 == 0: # trocar o sinal de igual (==) por dirente (!=) para exibir números ímpares.
        continue
    print (numero, end=" ")
      
# Outra maneira mais simples:

numero = 1

while numero < 51: 
    
    numero += 1
    
    if numero > 50:
        break
    elif numero % 2 != 0:
      print (numero, end=" ")