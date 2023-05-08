    # São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo: op_comparacao + op_logico + op_comparacao… N …

saldo = 1000
saque = 200
limite = 100

print (saldo >= saque)
print (saque <= limite)

# Operador E:

saldo = 1000
saque = 200
limite = 100

print (saldo >= saque and saque <= limite)

# Operador OU:

saldo = 1000
saque = 200
limite = 100

print (saldo >= saque or saque <= limite)

# Operador Negação:

contatos_de_emergencia = []

print ('')

print (not 1000 > 1500)

print (not contatos_de_emergencia)

print (not 'saque 1500:')

print (not '')

# Parênteses:

saldo = 1000
saque = 200
limite = 100
conta_especial = True

print ('')

print (saldo >= saque and saque <= limite or conta_especial and saldo >= saque) # Sintaxe Errada

print ((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)) # Sintaxe Correta

# Pode ser atribuído a uma variável:

autorizacao_de_saque = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print (autorizacao_de_saque)