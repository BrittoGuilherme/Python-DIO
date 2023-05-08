print ()
print ("  MENU  ".center(40, "#"))
menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato

    [q] Sair

Digite a opção desejada => """

valor_deposito = 0
valor_de_saque = 0
saldo = 0
LIMITE = 500
extrato_deposito = []
extrato = []
numero_saques = 0
LIMITE_SAQUES = 4

while True:
    
    opcao = input(menu)
    
                            # Depositos
                            
    if opcao == "d":
        print ()
        print ("  DEPÓSITOS  ".center(40, "#"))
        print ()
        valor_deposito = float(input("Digite o valor que deseja DEPOSITAR: "))
        saldo += valor_deposito
        extrato.insert(0, ["Depósito", valor_deposito])
        print (f"""
    Deposito de R${valor_deposito:.2f} efetuado com sucesso!

    Seu saldo atual é de R${saldo:.2f}
    """)
        if valor_deposito < 0:
            print ("Numero inválido, favor digitar um número positivo.")
            
                            # Saques
                            
    elif opcao == "s":
        
        valor_de_saque = float(input("Digite o valor que deseja SACAR: "))
        
        if (valor_de_saque <= LIMITE) and (valor_de_saque <= saldo):
            
            LIMITE_SAQUES -= 1
            if LIMITE_SAQUES <= 0:
                print ("""
    Limite diário de 3 saques foi atingido!
    """)
                continue

            saldo -= valor_de_saque
            extrato.insert(0, ["Saque", valor_de_saque])
            print (f"""
    Seu saque no valor de: R${valor_de_saque:.2f}, foi efetuado com sucesso!
    
    Seu saldo atual é de: R${saldo:.2f}
    """)
                    
        if valor_de_saque > LIMITE:
            print (f"""
    Saque não autorizado, seu limite por saque é de R${LIMITE:.2f}
    
    Saldo atual: R${saldo:.2f}
    """)
            
        if (valor_de_saque > saldo) and valor_de_saque < LIMITE:
            print (f"""
    Saque não autorizado, valor de saque excede seu saldo atual!
    
    Saldo atual: R${saldo:.2f}
    """)

        if valor_de_saque < 0:
            print ()
            print ("Numero inválido, favor digitar um número positivo.")
            
        
                            # Extratos
                            
    elif opcao == "e":
        print()
        print ("  EXTRATO  ".center(40, "#"))
        print()
        if len(extrato) == 0:
            print ("    Não foram realizadas movimentações.")
        for item in extrato:
            print(f"{item[0]} de R${item[1]}")
            
                            # Quit
                            
    elif opcao == "q":
        print()
        print("Obrigado por utilizar nossos serviços, até breve!")
        print()
        break
    else:
        print ()
        print ("Operação inválida, por favor selecione novamente a operação desejada.")
        