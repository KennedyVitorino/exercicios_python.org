# 17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120


def fatorial_while(numero):
    fatorial = 1
    i = numero
    expressao = ''
    while i >= 1:
        fatorial *= i
        expressao += str(i) + ' x '
        i -= 1
    return expressao, fatorial


# ------------------------------------------------------------------------------------------------------------


def fatorial_for(numero):
    fatorial = 1
    expressao = ''
    for i in range(numero, 1, -1):
        fatorial *= i
        expressao += str(i) + ' x '
    
    expressao += '1'
    return expressao, fatorial


# ------------------------------------------------------------------------------------------------------------


def main():
    numero = int(input('Digite um número: '))
    
    expressao, resultado_fat = fatorial_while(numero)
    print(f'{numero}! -> {expressao.strip(" x ")} = {resultado_fat}')
    
    expressao1, resultado_fat1 = fatorial_for(numero)
    print(f'{numero}! -> {expressao1.strip(" x ")} = {resultado_fat1}')


if __name__ == '__main__':
    main()
