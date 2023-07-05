# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

def encontrar_maior(a, b, c):
    if a > b and a > c:
        maior = a
    elif b > a and b > c:
        maior = b
    else:
        maior = c
    return maior
    

def encontrar_menor(a, b, c,):
    if a < b and a < c:
        menor = a
    elif b < a and b < c:
        menor = b
    else:
        menor = c
    return menor
    
    
n1 = int(input('Número 1 -> '))
n2 = int(input('Número 2 -> '))
n3 = int(input('Número 3 -> '))

maior_numero = encontrar_maior(n1, n2, n3)
menor_numero = encontrar_menor(n1, n2, n3)

print(f'\nO maior número é: {maior_numero}')
print(f'O menor número é: {menor_numero}')

