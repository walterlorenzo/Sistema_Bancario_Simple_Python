# Este código é um programa de caixa eletrônico que permite aos usuários realizar operações bancárias, como saques e depósitos, verificar o saldo da conta e visualizar um extrato das transações. O programa mantém um registro das operações e faz verificações para garantir que as operações sejam válidas, como a disponibilidade de saldo e o cumprimento do limite de saque. O menu do programa é exibido repetidamente até que o usuário escolha sair.

Menu = '''
[ 1 ] Sacar
[ 2 ] Depositar
[ 3 ] Extrato
[ 0 ] Sair
Escolha uma opção:'''

saldo = 0
limite = 500
extrato = ''
quantidade_saques = 0
limite_saques = 3

while True:

    opcao = input(Menu)

    if opcao == '2':
        valor = float(input('Qual o valor do depósito? '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito de R${valor:.2f}\n'

        else:
            print('Operação falhou! o valor informado é inválido.')

    elif opcao == '1':
        valor = float(input('Qual o valor do saque? '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = quantidade_saques >= limite_saques

        if excedeu_saldo:
            print('Operação falhou! Saldo Insuficiente.')

        elif excedeu_limite:
            print('Operação falhou! Limite de saques excedido.')

        elif excedeu_saques:
            print('Operação falhou! Limite de saques excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque de R${valor:.2f}\n'
            quantidade_saques += 1

        else:
            print('Operação falhou! o valor informado é inválido.')

    elif opcao == '3':
        print('\n==============Extrato===============')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo de R${saldo:.2f}')
        print('====================================')

    elif opcao == '4':
        break

    else:
        print('Opção inválida!')
        

