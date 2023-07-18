# 19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.


def conjuntos(elementos_conjunto, primeiro_numero):
    menor_numero = primeiro_numero
    maior_numero = primeiro_numero
    soma_numeros = primeiro_numero

    for _ in range(elementos_conjunto - 1):
        numero = float(input('Digite um número: '))
        if numero < 0 or numero > 1000:
            print('Número inválido. Digite um número entre 0 e 1000.')
            continue
        menor_numero = min(menor_numero, numero)
        maior_numero = max(maior_numero, numero)
        soma_numeros += numero
    return menor_numero, maior_numero, soma_numeros


def main():
    conjunto = int(input('Elementos: '))
    primeiro_numero = float(input('Primeiro Número: '))
    menor, maior, soma = conjuntos(conjunto, primeiro_numero)
    print(f'Menor: {menor}\nMaior: {maior}\nSoma: {soma}')


if __name__ == '__main__':
    main()
