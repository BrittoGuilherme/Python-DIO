# print("\n"+" MENU ".center(50, "="))

# def menu():
#     menu = """
#         [d] Depositar
#         [s] Sacar
#         [e] Extrato

#         [q] Sair

#     Digite a opção desejada: => """
#     return input(menu)

# def deposito (valor_deposito, saldo, extrato, /):
#     if valor_deposito > 0:
#         saldo += valor_deposito
#         extrato += valor_deposito
#         print(f"\nDeposito de R$ {valor_deposito:.2f} foi efetuado com sucesso!")
#         print(f"\nSeu saldo atual é de R$ {saldo:.2f}\n")
#     else:
#         print ("\nO valor informado é inválido, tente novamente.")
#     return saldo, valor_deposito,
# deposito(500, 200, 100)

def cadastro_cliente(clientes):
    cpf = input("Informe o CPF (somente numeros): => ")
    cliente = verifica_cadastro(cpf, clientes)
    
    if cliente:
        print("CPF já cadastrado!")
        return

    nome = input("Informe o nome completo: => ")
    data_de_nascimento = input ("Infomre data de nascimento (dd-mm-aaaa): => ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): => ")
    
    clientes.append ({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Cadastro efetuado com sucesso!")

def verifica_cadastro(cpf,clientes):
    clintes_verificados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clintes_verificados[0] if clintes_verificados else None

clientes = []
cadastro_cliente(clientes)
