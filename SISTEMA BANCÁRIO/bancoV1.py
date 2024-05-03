menu = """ 
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("INFORME O VALOR DO DEPÓSITO: "))

        if valor > 0:
            saldo += valor
            extrato += f"+ R$ {valor:.2f}\n"
        else:
            print("OPERAÇÃO FALHOU. VALOR INFORMADO É INVÁLIDO.")

    elif opcao == "2":
        valor = float(input("INFORME O VALOR DO SAQUE: "))

        saldo_insuficiente = saldo < valor
        limite_exedido = valor > limite
        saques_exedido = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("OPERAÇÃO FALHOU. SALDO INSUFICIENTE.")
        elif limite_exedido:
            print("OPERAÇÃO FALHOU. LIMITE EXEDIDO.")
        elif saques_exedido:
            print("OPERAÇÃO FALHOU. QUANTIDADE DE SAQUES EXEDIDA.")
        elif valor > 0:
            saldo -= valor
            extrato += f"- R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("OPERAÇÃO FALHOU. VALOR INFORMADO É INVÁLIDO.")

    elif opcao == "3":
        print("\n ===================== EXTRATO =====================")
        if not extrato:
            print("\n NÃO FORAM FEITAS MOVIMENTAÇÕES")
            print("\n ===================================================")
        else:
            print(extrato)
            print(f"\n SALDO: R$ {saldo:.2f}")
            print("\n ===================================================")

    elif opcao == "4":
        break
    else:
        print("OPÇÃO INVÁLIDA.")