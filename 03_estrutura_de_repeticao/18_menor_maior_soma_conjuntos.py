# 18. Faça um programa que, dado um conjunto de N números, determine
# o menor valor, o maior valor e a soma dos valores.


def conjuntos(elementos_conjunto, primeiro_numero):
    menor_numero = primeiro_numero
    maior_numero = primeiro_numero
    soma_numeros = primeiro_numero
    
    for _ in range(elementos_conjunto - 1):
        numero = float(input('Digite um número: '))
        menor_numero = min(menor_numero, numero)
        maior_numero = max(maior_numero, numero)
        soma_numeros += numero
    return menor_numero, maior_numero, soma_numeros


def main():
    elementos_conjunto = int(input('Elementos: '))
    primeiro_numero = float(input('Primeiro número: '))
    menor, maior, soma = conjuntos(elementos_conjunto, primeiro_numero)
    print(f'Menor: {menor}'
          f'\nMaior: {maior}'
          f'\nSoma: {soma}')


if __name__ == '__main__':
    main()
