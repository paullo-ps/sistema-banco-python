#depositar somente valores positivos
#depositos armazenados em uma variavel e exibi-los no extrato

'''
permitir 3 saques com limite de 500 por saque
sem saldo exibir mensagem de erro
saque devem ser armazendos e exibidos no extrato
'''

'''
Extrato deve listar depositos e saques
no fim do extrato deve ser exibido saldo atual da conta
exibir valores como: 50.45 = R$ 50,45
'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=>
'''

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input('Valor do deposito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
        else: print('Valor inválido para deposito.')

    elif opcao == 2:
        print(numero_saques)
        if numero_saques == LIMITE_SAQUES:
            print('Limite máximo de saques atingido.')
            continue
        else:
            valor = float(input('Valor do saque: '))
            print(valor >= saldo)

            if valor <= limite and valor > 0 and saldo >= valor:
                saldo -= valor
                numero_saques += 1
                extrato += f'Saque: R$ {valor}\n'
            else:
                if saldo < valor :
                    print('Valor do saque maior que o saldo disponivel.')

    elif opcao == 3:
        while True:
            print(f'''
{'Extrato'.center(19, '=')}
{'Nada consta.' if not extrato else extrato}
Saldo atual: R$ {saldo:.2f}\n
            ''')
            sair = input('Deseja sair do extrato? [S/N]: ')
            if sair.upper() == 'S':
                break

    elif opcao == 0:
        break