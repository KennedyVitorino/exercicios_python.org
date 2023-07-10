# 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.


def eh_inteiro_decimal(numero):
    if numero.is_integer():
        return 'inteiro'
    else:
        return 'decimal'
    
    
num = float(input('\nDigite um número: '))
tipo = eh_inteiro_decimal(num)

print(f'O número {num} é do tipo {tipo}')
