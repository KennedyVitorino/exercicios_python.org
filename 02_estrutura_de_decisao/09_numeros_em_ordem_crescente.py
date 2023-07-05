# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.


def ordenar_numeros(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        menor = num1
        if num2 <= num3:
            segundo_menor = num2
            maior = num3
        else:
            segundo_menor = num3
            maior = num2
    elif num2 <= num1 and num2 <= num3:
        menor = num2
        if num1 <= num3:
            segundo_menor = num1
            maior = num3
        else:
            segundo_menor = num3
            maior = num1
    else:
        menor = num3
        if num1 <= num2:
            segundo_menor = num1
            maior = num2
        else:
            segundo_menor = num2
            maior = num1
    
    numeros_ordem_crescente = [menor, segundo_menor, maior]
    return numeros_ordem_crescente


n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
numeros_ordenados = ordenar_numeros(n1, n2, n3)
ordem_crescente = f'Em ordem crescente: {", ".join(map(str, numeros_ordenados))}'

print(ordem_crescente)
