import sys


#variaveis
saldo = 0
limite = 500
extrato = ""
num_saque = 0
LIMITE_SAQUES = 3


menu = """
    =   MENU DE OPÇÕES:
    =   [d] DEPOSITO
    =   [s] SACAR
    =   [e] EXTRATO
    =   [q] Sair
    =   Informe a opção desejada:
    =   ->> """


while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar\nR$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito EFETUADO: {valor:.2f}\n"
            print("Operação realizada com sucesso!")
        else:
            print("Informe um valor válido!")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar\nR$ "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = num_saque >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação negada!\nSaldo Insuficiente!")
        elif excedeu_limite:
            print("Operação Negada!\nValor excede o limite de saque diario.")
        elif excedeu_saques:
            print("Operação Negada!\nLimite de operação diario excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saques EFETUADO: R$ {valor:.2f}\n"
            num_saque += 1
            print("Operação realizada com sucesso!")
    
        else:
            extrato =+ f"Saque NEGADO: R${valor:.2f}"
            print("Falha na Operação\nO verifique o valor informado!")

    elif opcao == "e":
        print("========== EXTRATO ==========")
        print(extrato if extrato else "Não foram realizadas movimentações.\n")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")

    elif opcao == "q":
        break

    else:
        print("\n\n===============================\n= Opção Inválida!             =\n= Seleione uma opção válida   =\n===============================\n\n")