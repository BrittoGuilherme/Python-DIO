print("\n"+" MENU ".center(50, "="))

def menu():
    menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato

        [q] Sair

    Digite a opção desejada: => """
    return input(menu)

def deposito (valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f" Deposito: R$ {valor:.2f}\n"
        print(f"\nDeposito de R$ {valor:.2f} foi efetuado com sucesso!")
        print(f"\nSeu saldo atual é de R$ {saldo:.2f}\n")
    else:
        print ("\nO valor informado é inválido, tente novamente.")
    return saldo, extrato

def saque (*, valor, saldo, extrato, limite, numero_saques, limite_saques):
    
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

        if not excedeu_saldo:
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


def main ():
    while True:
        saldo = 0
        limite = 500
        extrato = ""
        numero_saques = 0
        LIMITE_SAQUES = 3
        
        opcao = menu()
            
        if opcao == "d":
            print("\n"+" DEPÓSITOS ".center(50, "="))
            
            valor = float(input("\nDigite o valor que deseja DEPOSITAR: => "))
            saldo, extrato = deposito(valor, saldo, extrato)
            
        elif opcao == "s":
            print("\n"+" SAQUE ".center(50, "="))
            
            valor = float(input("\nDigite o valor que deseja SACAR: => "))
            saldo, extrato = saque (
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
                        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "q":
            print("\nObrigado por utilizar nossos serviços, até breve!\n")
            break
        
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

main()