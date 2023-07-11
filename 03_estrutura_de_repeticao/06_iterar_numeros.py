# 6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

# usando FOR

def imprimir_numeros_horizontal():
    for c in range(1, 21):
        print(c)


def imprimir_numeros_vertical():
    n = ', '.join(str(i) for i in range(1, 21))
    print(n)


# usando WHILE


def imprimir_num_horizontal():
    i = 0
    while i < 20:
        i += 1
        print(i)


def imprimir_num_vertical():
    i = 0
    while i < 20:
        i += 1
        print(i, end=' ')


def main():
    imprimir_numeros_horizontal()
    imprimir_numeros_vertical()
    
    imprimir_num_horizontal()
    imprimir_num_vertical()


if __name__ == '__main__':
    main()
