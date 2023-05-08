    # A Estética:
    
# Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

    # Bloco de Comando:
    
# As linguagens de programação costumam utilizar caracteres ou palavras reservadas para terminar o início e fim do bloco. Em Java e C por exemplo, utilizamos chaves:

def sacar(self, valor: float) -> None:  # início do bloco do método
        
    if self.saldo >= valor:  # início do bloco do if
    
        self.saldo -= valor  
        
    # fim do bloco do if
    
# fim do bloco do método

# Isso não funciona em Python:
def sacar(self, valor: float) -> None:  # início do bloco do método
if self.saldo >= valor:  # início do bloco do if    
self.saldo -= valor          
# fim do bloco do if    
# fim do bloco do método

