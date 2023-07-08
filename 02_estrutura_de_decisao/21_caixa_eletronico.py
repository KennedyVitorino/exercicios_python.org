# 21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a
# valor do saque e depois informar quantas notas de cada valor serão fornecidas. As
# notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais
# e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
# existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
# uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


def caixa_eletronico(valor_saque):
    if saque < 10 or saque > 600:
        print("Valor inválido. O saque deve ser entre 10 e 600 reais.")
        return
    
    notas100 = 0
    notas50 = 0
    notas10 = 0
    notas5 = 0
    notas1 = 0
    
    while valor_saque >= 100:
        valor_saque -= 100
        notas100 += 1
    while valor_saque >= 50:
        valor_saque -= 50
        notas50 += 1
    while valor_saque >= 10:
        valor_saque -= 10
        notas10 += 1
    while valor_saque >= 5:
        valor_saque -= 5
        notas5 += 1
    while valor_saque >= 1:
        valor_saque -= 1
        notas1 += 1
   
    print("Notas fornecidas:")
    if notas100 > 0:
        print(f"{notas100} nota(s) de R$ 100")
    if notas50 > 0:
        print(f"{notas50} nota(s) de R$ 50")
    if notas10 > 0:
        print(f"{notas10} nota(s) de R$ 10")
    if notas5 > 0:
        print(f"{notas5} nota(s) de R$ 5")
    if notas1 > 0:
        print(f"{notas1} nota(s) de R$ 1")
   
    
saque = float(input('Quanto deseja sacar hoje: R$💸 '))
caixa_eletronico(saque)


