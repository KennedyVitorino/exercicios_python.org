# Faça um Programa que leia três números e mostre o maior deles.


def maior_deles(a, b, c):
    if a > b and a > c:
        m = a
    elif b > a and b > c:
        m = b
    else:
        m = c
    return m
    

def main():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    n3 = int(input('Número 3: '))
    maior = maior_deles(n1, n2, n3)
    
    print(maior)


if __name__ == '__main__':
    main()
