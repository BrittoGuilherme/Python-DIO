    # Função input:
# A função builtin input é utilizada quando queremos ler dados da entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.

nome_user = input ('Informe seu nome aqui: ')
print (nome_user)

# A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.

nome, sobrenome = ('Guilherme' , 'Britto')

print (nome, sobrenome)
print (nome, sobrenome, end='...\n')
print (nome, sobrenome, sep='#')