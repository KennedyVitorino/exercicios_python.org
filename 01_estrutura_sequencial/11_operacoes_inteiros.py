# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

def calcular_produto_dobro_metade(num1, num2):
    resultado = (num1 * 2) * (num2 / 2)
    return int(resultado)


def calcular_soma_triplo_terceiro(num1, num3):
    resultado = (3 * num1) + num3
    return resultado


def calcular_cubo_terceiro(num3):
    resultado = num3 ** 3
    return resultado


def main():
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    numero3 = int(input('Digite o terceiro número: '))
    
    prod_dobro_metade = calcular_produto_dobro_metade(numero1, numero2)
    soma_tiplo_terceiro = calcular_soma_triplo_terceiro(numero1, numero3)
    cubo_terceiro = calcular_cubo_terceiro(numero3)
    
    print(f'O produto do dobro do primeiro com metade do segundo: {prod_dobro_metade}')
    print(f'A soma do triplo do primeiro com o terceiro: {soma_tiplo_terceiro}')
    print(f'O cubo do terceiro: {cubo_terceiro}')


if __name__ == '__main__':
    main()
