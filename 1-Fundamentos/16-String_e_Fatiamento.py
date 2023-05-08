    # Conhecendo métodos úteis da classe string
# A classe String do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.
# Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em Python esse trabalho é muito simples.

curso = "pYtHon"

print (curso.upper()) # Maiúscula
print (curso.lower()) # Minúscula
print (curso.title()) # Título
print ()

curso = "     Python  "
print ("#",curso,"#")
print ("#",curso.strip(),"#") # Elimina os espaços em branco.
print ("#",curso.lstrip(),"#") # Elimina os espaços em branco do lado ESQUERDO.
print ("#",curso.rstrip(),"#") # Elimina os espaços em branco do lado DIREITO.
print ()

curso = "Python"
print (curso.center(16, "*")) # 
print ("*".join(curso)) # 

    # Interpolação de Variáveis:
# Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é utilizando o método format e a última é utilizando f strings.
# A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro, por esse motivo iremos focar nas 2 últimas.

# Old Style %

nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

    # Método Format:

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

b_dados = {"nome": "Guilherme", "idade": 29, "profissao": "Programador", "linguagem": "Python"}

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**b_dados))

    # Método f-string:

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# Formatando com f-string:

PI = 3.14159

print(f"Valor de PI: {PI:.2f}") # o primeiro parâmetro depois do PI: refere-se ao espaço entre a string e a variável, (neste caso em branco). Já o segundo refere-se ao numero de casas decimais que vc quer exibir, (neste caso 2), e o "f" pq é uma variável do tipo float.

print(f"Valor de PI: {PI:10.2f}")

    # Fatiamento de string:
    
nome = "Guilherme Matos de Britto Silva"

print (nome[:9])
print (nome[0])
print (nome[-1])
print (nome[-5:])
print (nome[10:])
print (nome[10:15])
print (nome[10:15:2])
print (nome[:])
print (nome[::-1])

    # String Múltiplas Linhas:
# Strings de múltiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição. Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final. 

# Strings Triplas/Múltiplas:

nome = "Guilherme"
curso = "Python"

mensagem_1 = f"""
Olá, meu nome é {nome}.
Estou aprendendo {curso}.
"""

mensagem_2 = f"""
    Olá, meu nome é {nome}.
Estou aprendendo {curso}.
            Essa mensagem tem diversos recuos.
"""

print (mensagem_1, mensagem_2)