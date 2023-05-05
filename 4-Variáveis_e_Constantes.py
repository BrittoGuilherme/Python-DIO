        #Variáveis
    
    # Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa.

    # Sintaxe:
    
name = ("Guilherme")
age = (29)
print (f"Meu nome é {name}, e eu tenho {age} anos")

    # Variáveis também podem ser declaradas na mesma linha, desde que separadas por virgula, ex.:

name, age = ("Guilherme", 29)
print (f"Meu nome é {name}, e eu tenho {age} anos")

        # Alterando Valores:

# Perceba que não precisamos definir o tipo de dados da variável, o Python faz isso automaticamente para nós. Por isso não podemos simplesmente criar uma variável sem atribuir um valor. Para alterar o valor da variável basta fazer uma atribuição de um novo valor:

name = "Jéssica"
age = (31)
print (f"Meu nome é {name}, e eu tenho {age} anos")

    # Constantes
    
# Assim como as variáveis, constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável.
# Python não tem constantes
# Não existe uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagens por exemplo: Java e C utilizamos final e const, respectivamente para declarar uma constante.
# Em Python usamos a convenção que diz ao programador  que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letras maíusculas:

ABS_PATH = '/home/guilherme/Documents/python_course/'
DEBUG = True
STATES = [
    'SP',
    'RJ',
    'MG',
]
AMOUNT = 30.2
   
    # Boas Práticas:

        # O padrão de nomes deve ser snake case.
        # Escolher nomes sugestivos.
        # Nome de constantes todo em maiúsculo.





