menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

valor_deposito = 0
valor_de_saque = 0
saldo = 0
LIMITE = 500
extrato_deposito = []
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor_deposito = float(input("Digite o valor que deseja DEPOSITAR: "))
        saldo += valor_deposito
        extrato.insert(0, ["Depósito", valor_deposito])
        print (f"""
    Deposito de R${valor_deposito:.2f}, efetuado com sucesso!

    Seu saldo atual é de R${saldo:.2f}
    """)
        
    elif opcao == "s":
        
        valor_de_saque = float(input("Digite o valor que deseja SACAR: "))
        
        if (valor_de_saque <= LIMITE) and (valor_de_saque <= saldo):
            saldo -= valor_de_saque
            LIMITE_SAQUES -= 1
            extrato.insert(0, ["Saque", valor_de_saque])
            print (f"""
    Seu saque no valor de: {valor_de_saque:.2f}, foi efetuado com sucesso!
    
    Seu saldo atual é de: {saldo:.2f}
    """)
        
        if LIMITE_SAQUES == 0:
            print ("Limite diário de 3 saques foi atingido!")
            break
        
        if valor_de_saque > LIMITE:
            print ("Saque não autorizado, seu limite por saque é de R$500,00")
            print ("Saldo atual: ", saldo)
            
        if (valor_de_saque > saldo) and valor_de_saque < LIMITE:
            print ("Saque não autorizado, seu saldo é inferior, ao valor de saque!")
            print ("Saldo atual: ", saldo)

            
    elif opcao == "e":
        print ("Extrato")
        if len(extrato) == 0:
            print ("Não foram realizadas movimentações.")
        for item in extrato:
            print(f"{item[0]} de R${item[1]}")
        
    elif opcao == "q":
        break
    else:
        print ("Operação inválida, por favor selecione novamente a operação desejada.")
        