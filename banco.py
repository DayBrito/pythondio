import datetime
import time


hoje = datetime.datetime.now().strftime('%d-%m-%Y')


cliente = input("Olá! Insira o seu nome: ")


menu = f"""
Bem vindo (a) {cliente}, por favor selecione uma opção:
a-Sacar
b-Depositar
c-Extrato

q-Sair
"""


saldo = 0.0
limite_saque = 500
extrato = ""
qtd_saques = 3
sleep = time.sleep(2)

while True:
    opcao = input(menu)

    if opcao == 'a':
        if qtd_saques <= 0:
            print('Não há saque disponível.')
            time.sleep(2)
        else:
            saque = input('Digite o valor que deseja sacar: R$')
            if saque.isdigit():
                saque = float(saque)
                if saque <= saldo:
                    saldo -= saque
                    print(f'\n**R${saque} retirado com sucesso.**')
                    extrato += f'\n\n--Saque: R${saque}-- \nData: {hoje}\nUsuário: {cliente}'
                    qtd_saques -= 1
                    time.sleep(2)
                else:
                    print(f'\n\nValor R${saque} não disponível. \n*Saldo atual: R${saldo}*')
                    time.sleep(2)
            else:
                print('\n\nOperação inválida, tente novamente.\n\n') 
                time.sleep(2)
    elif opcao == 'b':
        valor = input('Insira o valor de depósito: R$')
        if valor.isdigit():
            valor = float(valor)
            if valor > 0:
                saldo += valor
                print(f'\nDepósito de R${valor} realizado. \n*Saldo atual R${saldo}*')
                time.sleep(2)     
                extrato += f'\n\n--Depósito: R${valor}-- \nData: {hoje}\nUsuário: {cliente}-'
            else:
                print('\n\nOperação inválida, tente novamente.\n\n') 
                time.sleep(2)
        else:
            print('\n\nOperação inválida, tente novamente.\n\n') 
            time.sleep(2)

    elif opcao == 'c':
        print(f'{extrato}')
        print(f'\n\n**Saldo atual: R${saldo}**')
        print(f'\n\n**Saques disponíveis: {qtd_saques}**')
        time.sleep(2)
    elif opcao == 'q':
        print('Finalizando a operação.')
        break
    else:
        print('Opção inválida! Tente novamente')
        time.sleep(2)
