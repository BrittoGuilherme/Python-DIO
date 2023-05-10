print("\n"+" MENU ".center(50, "="))

menu = (f"""
    [d] Depositar
    [s] Sacar
    [e] Extrato

    [q] Sair

 Digite a opção desejada: => """)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
        
    if opcao == "d":
        
        valor_deposito = float(input("\nDigite o valor que deseja DEPOSITAR: => "))
        print("\n"+" DEPÓSITOS ".center(50, "="))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += (f" Deposito: R$ {valor_deposito:.2f}\n")
            print(f"\nDeposito de R$ {valor_deposito:.2f} foi efetuado com sucesso!")
            print(f"\nSeu saldo atual é de R$ {saldo:.2f}\n")
        else:
            print ("\nO valor informado é inválido, tente novamente.")    
    
    elif opcao == "s":
        
        valor_de_saque = float(input("\nDigite o valor que deseja SACAR: => "))
        print("\n"+" SAQUE ".center(50, "="))
        
        excedeu_saldo = valor_de_saque > saldo
        
        excedeu_limite = valor_de_saque > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
                  
        if excedeu_saldo:
            print ("\nSaque não autorizado, valor de saque excede seu saldo atual!")
            print (f"\nSeu saldo atual é de: R$ {saldo:.2f}")
            
        elif excedeu_limite:
            print (f"\nSaque não autorizado, seu limite por saque é de R$ {limite:.2f}")
            print (f"\nSeu saldo atual é de: R$ {saldo:.2f}")
            
        elif excedeu_saques:
            print ("\nLimite de saque diário excedido!")
        
        elif valor_de_saque > 0:
        
            saldo -= valor_de_saque
            extrato += (f" Saque: R$ {valor_de_saque:.2f}\n")
            numero_saques += 1

            if not excedeu_saldo:
                print(f"\nSeu saque no valor de: R${valor_de_saque:.2f}, foi efetuado com sucesso!")
                print(f"\nSeu saldo atual é de: R${saldo:.2f}")
        else:
            print ("\nO valor informado é inválido, tente novamente.")    
            
    elif opcao == "e":
        print("\n"+" extrato ".upper().center(50,"="))
        print(" Não foram realizadas movimentações." if not extrato else extrato)
        print (f"\n Saldo: R$ {saldo:.2f}")
        print("=" * 50)      
        
    elif opcao == "q":
        print("\nObrigado por utilizar nossos serviços, até breve!\n")
        break
    
    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")