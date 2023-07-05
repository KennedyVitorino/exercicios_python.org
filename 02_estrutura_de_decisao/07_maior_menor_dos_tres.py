# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

def encontrar_maior(a, b, c):
    if a > b and a > c:
        maior = a
    elif b > a and b > c:
        maior = b
        
n1 = int(input('n :'))
n2 = int(input('n :'))
n3 = int(input('n :'))

ma, me = encontrar_maior_menor(n1, n2, n3)

print(ma, me)