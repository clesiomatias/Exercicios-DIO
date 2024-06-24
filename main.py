
#Escopo de variáveis
saldo=0
limite=500
extrato=''
numero_saques=0
LIMITE_SAQUES=3 

#----------------------------------------------------
#Escopo de funções
def deposito(valor):
    global saldo, extrato
    saldo += valor
    extrato += f"Depósito:R${valor:.2f}\n"


def saque(valor):
    global saldo, numero_saques, extrato
    if valor > saldo:
        print("Saldo insuficiente")
    elif numero_saques >= LIMITE_SAQUES:
        print("Limite de saques excedido")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque:R${valor:.2f}\n"


def imprime_extrato():
    print(
        f"""
================= EXTRATO =================
{extrato if extrato!= '' else' Não foram realizadas movimentações.'}

Saldo: R$ {saldo:.2f}
============================================
          """
    )
#_______________________________________________________________________

menu='''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
''' 

while True:
    opcao=input('Qual operação deseja realizar?\n'+menu)
    if opcao=='d':
        valor=float(input('Digite o valor do depósito:'))
        deposito(valor)
    elif opcao=='s':
        valor=float(input('Digite o valor do saque:'))
        saque(valor)
        
    elif opcao=='e':
        imprime_extrato()
    elif opcao=='q':
        break
    else:
        print('Opção inválida')
