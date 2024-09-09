menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = []  # Agora extrato é uma lista que armazena cada transação
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":  # Depósito
        while True:
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print("Depósito realizado com sucesso!")
                break
            else:
                print("Operação falhou! O valor informado é inválido.")
                tentar_novamente = input("Deseja tentar novamente? (s/n): ")
                if tentar_novamente.lower() != 's':
                    break

    elif opcao == "2":  # Saque
        while True:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato.append(f"Saque: R$ {valor:.2f}")
                numero_saques += 1
                print("Saque realizado com sucesso!")
                break
            else:
                print("Operação falhou! O valor informado é inválido.")

            # Pergunta se o usuário quer tentar novamente
            tentar_novamente = input("Deseja tentar novamente? (s/n): ")
            if tentar_novamente.lower() != 's':
                break

    elif opcao == "3":  # Extrato
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in extrato:
                print(transacao)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":  # Sair
        print("Encerrando o sistema. Obrigado por utilizar nossos serviços.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
