# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a
# quantidade de números impares.


def pares_impares_while():
    p = 0
    i = 0
    c = 0
    while c < 10:
        n = int(input('Digite um número inteiro: '))
        c += 1
        if n % 2 == 0:
            p += 1
        else:
            i += 1
    return p, i


# ------------------------------------------------------------------------------------------------------------


def pares_impares_for():
    p = 0
    i = 0
    for _ in range(10):
        n = int(input('Digite um número inteiro: '))
        if n % 2 == 0:
            p += 1
        else:
            i += 1
    return p, i
            
            
def main():
    pares1, impares1 = pares_impares_while()
    print(f'Quantidade de pares: {pares1}')
    print(f'Quantidade de ímpares: {impares1}')
    
    pares, impares = pares_impares_for()
    print(f'Quantidade de pares: {pares}')
    print(f'Quantidade de ímpares: {impares}')




if __name__ == '__main__':
    main()
    