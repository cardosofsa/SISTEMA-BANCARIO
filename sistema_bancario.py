menu = """
    [1] Depósito
    [2] Saque
    [3] Extrato
    [0] SAIR

"""

LIMITE_SAQUE = 3
saques = 0
saldo = 0
limite = 1500
extrato = ""

while True:
    try:
        escolha = int(input(menu))

        if escolha == 1:
            valor = float(input("Informe o valor de depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R${valor:.2f}\n"
            else:
                print("O valor está incorreto! Deve ser positivo e maior que zero.")

        if escolha == 2:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = saques >= LIMITE_SAQUE

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        if escolha == 3:
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R${saldo:.2f}")
            print("==========================================")

        if escolha == 0:
            print("Obrigado por usar nosso sistema bancário. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

    except ValueError:
        print("Entrada inválida! Por favor, insira um número correspondente ao menu.")