import textwrap


def saque(*,
          saldo,
          valor,
          limite,
          extrato_da_conta,
          numero_saques,
          limite_saques
          ):
    if numero_saques >= limite_saques or valor > limite:
        print(f'''Pode-se sacar {
            limite_saques} vezes por dia um valor máximo de R${limite}''')
        return False
    elif valor > saldo:
        print('não será possível sacar dinheiro por falta de saldo.')
        return False
    else:
        extrato_da_conta.append(f'- {valor:.2f}'.replace('.', ','))
        return True


def deposito(saldo, valor, extrato_da_conta, /):
    if valor > 0:
        extrato_da_conta.append(f'+ {valor:.2f}'.replace('.', ','))
        return True
    else:
        print('O valor precisa ser maior que zero!')
        if saldo > extrato_da_conta:
            return False
        return False


def extrato(saldo, /, *, extrato_da_conta):
    print(f'Extrato é de: R${saldo:.2f}'.replace('.', ','))
    for ext in extrato_da_conta:
        print(f'{ext}')


def valor_input(operation):
    deposito = float(input(f'\n\ndigite o valor para {operation}: '))
    if deposito <= 0:
        print('\n\nvalor inválido!\n\n')
        return 0.00
    return deposito


def criar_usuario(usuarios):
    cpf = input('Informe o CPF: ')
    userExist = user(cpf, usuarios)
    if userExist:
        print('Não é possivel criar outro usuario como mesmo cpf')
        return

    name = input('Informe o nome: ')
    birtyday = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
        )
    usuarios.append({
        "nome": name,
        "data_nascimento": birtyday,
        "cpf": cpf,
        "endereco": endereco
    })


def user(cpf, usuarios):
    userByCpf = [usuario for usuario in usuarios if usuario[cpf] == cpf]
    return userByCpf[0] if userByCpf else None


def criar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = user(cpf, usuarios)
    agencia = '0001'
    numero_conta = len(contas) + 1
    if user:
        contas.append({
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        })


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def painel_to_account():
    lim_saque = 3
    saldo = 0.00
    option = '0'
    number_saque = 0
    extrato_da_conta = []
    max_saque = 500.00
    usuarios = []
    contas = []
    while option != 'q':
        option = input('''
digite os valor para as opções:
[n] novo usuário;
[c] nova conta;
[l] lista as contas;
[d] Depósito;
[s] Saque;
[e] Saldo;
[q] Sair.

Opção: ''')
        if option == 'd':
            value = valor_input('depósito')
            if deposito(saldo, value, extrato_da_conta):
                saldo += value
        elif option == 's':
            value = valor_input('saque')
            if saque(
                saldo=saldo,
                extrato_da_conta=extrato_da_conta,
                valor=value,
                limite=max_saque,
                numero_saques=number_saque,
                limite_saques=lim_saque,
            ):
                saldo -= value
                number_saque += 1
        elif option == 'e':
            extrato(saldo, extrato_da_conta=extrato_da_conta)
        elif option == 'n':
            criar_usuario(usuarios)
        elif option == 'c':
            criar_conta(contas, usuarios)
        elif option == 'l':
            listar_contas(contas)
        elif option == 'q':
            print('\n\ntchau!\n\n')
        else:
            print('\n\ndigite uma alternativa válida!\n\n')


if __name__ == '__main__':
    painel_to_account()
