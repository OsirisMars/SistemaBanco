import textwrap


def menu():
    menu = """\n
    ========= Menu ========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nu]\tNovo Usuário
    [0]\tSair
    ➣"""
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Valor depositado: \tR${valor:.2f}"
        print("\n Depósito realizado com sucesso!!")
    else:
        print("\n Operação falhou! Valor inválido, tente novamente mais tarde")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, num_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = num_saques >= limite_saque

    if excedeu_saldo:
        print("\nOperação falhou! Saldo insuficiente.")
    elif excedeu_limite:
        print("\nOperação falhou! O valor de saque excede o limite")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR${valor:.2f}"
        num_saques += 1
        print("\n Operação Realizada com Sucesso!")
    else:
        print("\n Operação falhou! Valor informado é inválido tente novamente mais tarde")
    return saldo, extrato, num_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n =================EXTRATO ==============")
    if not extrato:
        print("Não houveram movimentações")
    else:
        print(extrato)
    print(f"\n Saldo: \t\t{saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("\nDigite o CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nERROR: Já existe um usuário com esse CPF")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento(dd/mm/aaaa): ")
    endereco = input("Informe o endereço(logradouro, nro - bairro - cidade/sigla estado):")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }

    print("\n Usuário não encontrado, criação de conta encerrada!!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular: \t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    num_saque = 0
    limite = 500  # limite maximo de saque
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor a ser sacado: "))
            saldo, extrato, num_saque = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saque,
                limite_saque=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Opção invalida, favor escolher uma opção válida")
