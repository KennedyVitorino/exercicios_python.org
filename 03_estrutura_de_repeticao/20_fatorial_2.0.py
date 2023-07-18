# 18. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
# limitando o fatorial a números inteiros positivos e menores que 16.


def fatorial(num):
    if num < 0 or num > 16:
        return 0
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado


def main():
    while True:
        numero = int(input('Digite um número inteiro: '))
        if numero == 0:
            break
        print(f'O fatorial de {numero} é {fatorial(numero)}')
    print('\nPrograma encerrado.')


if __name__ == '__main__':
    main()
