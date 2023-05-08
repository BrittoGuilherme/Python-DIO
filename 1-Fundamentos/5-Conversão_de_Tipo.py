# Em alguns momentos é necessário será necessário converter o tipo de uma variável para manipular de forma diferente. Por exemplo:
# Variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

preco = (10.3)
print (preco)

preco = int (preco) # converte em inteiro.
print (preco)

preco = float (preco) # converte em float.
print (preco)

# conversão por divisão:

preco = (preco / 2) # dividi e converte o resultado em float.
print (preco)

preco = (preco // 2) # dividi porém retorna somente o nome inteiro, desprezando oq vem depois do ponto.
print (preco)

# convertendo para outros tipos:

preco = (50)
print (type(preco)) 

idade = str(26) # converte uma variável em string.

texto = (f"Idade {idade}, Preço {preco}")

print (texto)

# pode-se diretamente no print

idade = (30)
idade_str = str (idade)

print (type(idade))
print (type (idade_str))