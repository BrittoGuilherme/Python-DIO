    # If / if-else / elif:
# A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

    # If:
# Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada if. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.

saldo = 2000.0
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print ('Realizando saque...')

if saldo < saque:
    print ('Saldo insuficiente!')

    # If/else:
# Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário o bloco de código do else será executado.

saldo = 2000.0
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print ('Realizando saque...')
else:
            print ('Saldo insuficiente!')

    # If/elif/else:
#Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código. 

opcao = int(input('Informe uma opção: \n [1] Sacar\n [2] Extrato: '))

if opcao == 1:
    valor = float(input('Informe o valor de saque: '))

elif opcao == 2:
    print ('Exibindo Extrato...')

else:
    sys.exit('Opção Inválida')

    # If Aninhado:
# Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else.

tipo_de_conta = int(input(f'Informe o tipo de conta: \n [1] Conta Normal\n [2] Conta Universitária: '))
cheque_especial = 500
saldo = 1000
valor_saque = float(input('Informe o valor do saque: '))

if tipo_de_conta == 1:
    if saldo >= valor_saque:
        print ('Saque realizado com sucesso!')
    elif valor_saque <= (saldo + cheque_especial):
        print ('Saque realizado com uso do cheque especial')
    else:
        print ('Saldo insuficiente!')
elif tipo_de_conta == 2:
    if saldo >= valor_saque:
        print ('Saque realizado com sucesso')
    else:
        print ('Saldo insuficiente!')

    # If Ternário:
# O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.

saldo = 1000
valor_saque = float(input('Informe o valor do saque: '))

status = 'Sucesso' if saldo >= valor_saque else 'Falha'

print (f'{status} ao realizar o saque!')
