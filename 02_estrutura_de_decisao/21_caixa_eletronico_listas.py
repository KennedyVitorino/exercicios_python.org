# 21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a
# # valor do saque e depois informar quantas notas de cada valor serão fornecidas. As
# # notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais
# # e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
# # existentes na máquina.
# # Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
# # uma nota de 50, uma nota de 5 e uma nota de 1;
# # Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
# # uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

def boca_do_caixa(saque):
    if not 10 <= saque <= 600:
        return 'Digite um valor entre R$ 10 e R$ 600 para sacar.'
    
    notas = [100, 50, 10, 5, 1]
    quantidades = [0, 0, 0, 0, 0]
    
    for i in range(len(notas)):
        while saque >= notas[i]:
            saque -= notas[i]
            quantidades[i] += 1
    
    print('💸Cédulas disponíveis💸')
    for i in range(len(notas)):
        if quantidades[i] > 0:
            print(f'{quantidades[i]} nota(s) de R$ {notas[i]:.2f}')
            

valor_saque = int(input('Quanto deseja sacar: '))
boca_do_caixa(valor_saque)
