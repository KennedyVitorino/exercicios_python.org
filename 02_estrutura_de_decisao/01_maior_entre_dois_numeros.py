# 1. Faça um Programa que peça dois números e imprima o maior deles.

def numero_maior(num1, num2):
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    return maior
    

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

maior_numero = numero_maior(n1, n2)
print(maior_numero)
