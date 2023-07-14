# 9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.


def sequencia_impares_while(c, n):
    while c < 50 and n <= 50:
        if n % 2 == 1:
            print(n)
            c += 1
        n += 1


# ------------------------------------------------------------------------------------------------------------


def sequencia_impares_for(c):
    for c in range(50):
        if c % 2 == 1:
            print(c)
    return c


def main():
    contador = 0
    numero = 1
    sequencia_impares_while(contador, numero)
    
    cont = 0
    sequencia_impares_for(cont)


if __name__ == '__main__':
    main()
