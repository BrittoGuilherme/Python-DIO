import textwrap

print("\n"+" MENU ".center(50, "="))

def menu():
    menu = """
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    
    [q]\tSair
    
    Digite a opção desejada: => """
    return input(textwrap.dedent(menu))


def deposito (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f" Deposito: R$ {valor:.2f}\n"
        print(f"\nDeposito de R$ {valor:.2f} foi efetuado com sucesso!")
        print(f"\nSeu saldo atual é de R$ {saldo:.2f}\n")
    else:
        print ("\nO valor informado é inválido, tente novamente.")
    return saldo, extrato

def saque (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print ("\nSaque não autorizado, valor de saque excede seu saldo atual!")
        print (f"\nSeu saldo atual é de: R$ {saldo:.2f}")
            
    elif excedeu_limite:
        print (f"\nSaque não autorizado, seu limite por saque é de R$ {limite:.2f}")
        print (f"\nSeu saldo atual é de: R$ {saldo:.2f}")
        
    elif excedeu_saques:
        print ("\nLimite de saque diário excedido!")
        
    elif valor > 0:
        
        saldo -= valor
        extrato += f" Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSeu saque no valor de: R${valor:.2f}, foi efetuado com sucesso!")
        print(f"\nSeu saldo atual é de: R${saldo:.2f}")
    else:
        print ("\nO valor informado é inválido, tente novamente.") 

    return saldo, extrato

def exibir_extrato (saldo, /, *, extrato):
    print("\n"+" extrato ".upper().center(50,"="))
    print(" Não foram realizadas movimentações." if not extrato else extrato)
    print (f"\n Saldo: R$ {saldo:.2f}")
    print("=" * 50)   
    
def cadastro_clientes(clientes):
    cpf = input("\nInforme o CPF (somente número): => ")
    cliente = verifica_cadastro(cpf, clientes)
    
    if cliente:
        print("\n"+" CPF já cadastrado! ".center(50, "="))
        return
    nome = input ("\nInforme nome completo: => ")
    data_nascimento = input("\nInforme a data de nascimento (dd-mm-aaaa): =>  ")
    endereco = input("\nInforme o endereço (logradouro, nº - bairro - cidade/sigla estado): => ")

    clientes.append ({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("\n"+" Usuário criado com sucesso! ".center(50, "="))
    
def verifica_cadastro(cpf, clientes):
    clintes_verificados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clintes_verificados [0] if clintes_verificados else None

def cadastro_contas(agencia, numero_da_conta, clientes):
    cpf = input("\nInforme o CPF do cliente (somente número): => ")
    cliente = verifica_cadastro(cpf, clientes)
    
    if cliente:
        print ("\n"+" Conta criada com sucesso! ".center(50, "="))
        return {"agencia": agencia, "numero_da_conta": numero_da_conta, "cliente": cliente}
    
    print("\n"+" Usuário não encontrado! ".center(50, "="))
    
def listar_contas(contas):
    for conta in contas:
        mostra_conta = f"""
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_da_conta"]}
            Titular:\t{conta["cliente"]["nome"]}
        """
        print(textwrap.dedent(mostra_conta))
        print("=" * 50)
    
def main ():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    clientes = []
    contas = []
    AGENCIA = "0001"
        
    while True:

        
        opcao = menu()
            
        if opcao == "d":
            print("\n"+" DEPÓSITOS ".center(50, "="))
            
            valor = float(input("\nDigite o valor que deseja DEPOSITAR: => "))
            saldo, extrato = deposito(saldo, valor, extrato)
            
        elif opcao == "s":
            print("\n"+" SAQUE ".center(50, "="))
            
            valor = float(input("\nDigite o valor que deseja SACAR: => "))
            saldo, extrato = saque (
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )
                        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            cadastro_clientes(clientes)
            
        elif opcao == "nc":
            numero_da_conta = len(contas) + 1
            conta = cadastro_contas(AGENCIA, numero_da_conta, clientes)
            
            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            print("\n"+" CONTAS ".center(50, "="))
            listar_contas(contas)  
                     
        elif opcao == "q":
            print("\nObrigado por utilizar nossos serviços, até breve!\n")
            break
        
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

main()