print("\n"+" MENU ".center(50, "="))

def menu():
    menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato

        [q] Sair

    Digite a opção desejada: => """
    return input(menu)

def deposito (valor_deposito, saldo, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += valor_deposito
        print(f"\nDeposito de R$ {valor_deposito:.2f} foi efetuado com sucesso!")
        print(f"\nSeu saldo atual é de R$ {saldo:.2f}\n")
    else:
        print ("\nO valor informado é inválido, tente novamente.")
    return saldo, valor_deposito,
deposito(500, 200, 100)