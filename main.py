def sacar(saldo, valor):
    if valor < 0:
        raise Exception("Erro: O valor de saque deve ser positivo")
    elif valor <= saldo:
        saldo -= valor
        return saldo
    else:
        raise Exception("Erro: Saldo Insuficiente")
def depositar(saldo, valor):
    if valor < 0:
        raise Exception("Erro: Esse valor é negativo verifique se digitou corretamente")
    saldo += valor
    return saldo


if __name__ == '__main__':
    saldo = 1000
    num_saque = 0
    LIMITE_SAQUE = 3
    while True:
        print("Escolha sua opção(S, D, E, 0): ")
        opcao = input("Digite uma opção: ")
        if opcao == "S":
            if num_saque == LIMITE_SAQUE:

                print("Limite diario de saques alcançado")
            else:
                valor = int(input("Digite um valor para saque: "))
                sacar(saldo, valor)
                num_saque += 1
                print(saldo)
                print(num_saque)    
        elif opcao == "D":
            valor = int(input("Digite um valor para depositar: "))
            try:
                depositar(saldo, valor)
                print("Valor depositado com sucesso, novo saldo: ", saldo)
            except Exception as f:
                print("Erro ao depositar")
        elif opcao == "E":
            print("Hello World")
        elif opcao == "0":
            print("Encerrando a sessão")
            break
        else:
            print("Opção Inválida")
