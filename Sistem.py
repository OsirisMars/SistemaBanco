saldo = 0
num_saque = 0
LIMITE_SAQUE = 3
max_limite  = 500 #limite maximo de saque
extrato = []


while True:
    print("""
    [1] Saque
    [2] Deposito
    [3] Extrato
    [0] Sair
    """)
    opcao = input("Digite a sua opção: ")
    if opcao == '1':
        saque = float(input("Digite o valor a ser sacado: "))
        if num_saque == LIMITE_SAQUE:
            raise Exception("Limite de saques diarios excedidos")
        elif saque > max_limite:
            raise Exception("O valor máximo para saque é de R$ 500")
        elif saldo > saque:
            saldo = saldo - saque
            print("Valor sacado com sucesso!")
            print("Saldo: R$ {:.2f}".format(saldo))
            extrato.append("Saldo Sacado: R$ -{:.2f}".format(saldo))
            num_saque += 1
        elif saque < 0:
            print("Valor de Saque inválido favor corrigir")
        else:
            raise Exception("Erro a conta não contém esse valor!!")
    elif opcao == '2':
        deposito = float(input("Digite o valor a ser deposito: "))
        saldo = saldo + deposito
        print("Valor de Deposito com sucesso!")
        extrato.append("Saldo Depositado: +R$ {:.2f}".format(saldo))
        print("Saldo: R$ {:.2f}".format(saldo))
    elif opcao == '3':
        if not extrato:
            print("Não há extrato")
        else:
            for transacao in extrato:
                print(f" - {transacao}")
    elif opcao == '0':
        print("Encerrando...")
        break

