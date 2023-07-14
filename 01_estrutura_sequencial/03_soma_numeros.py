# 3. Faça um Programa que peça dois números e imprima a soma.


def somar(n1, n2):
    s = n1 + n2
    return s
    
    
def main():
    numero_1 = int(input('Número 1: '))
    numero_2 = int(input('Número 2: '))
    soma = somar(numero_1, numero_2)
    
    print(f'A soma é [{soma}]')


if __name__ == '__main__':
    main()
    