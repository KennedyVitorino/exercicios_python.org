# Faça um programa que calcule as raízes de uma equação do segundo grau,
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
# consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
# o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais.
# Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
# informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
from math import sqrt


def calculo_raizes_equacao_segundo_grau(a, b, c):
    if a == 0:
        return 'Não é equação do segundo grau.'
    
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        'A equação não possui raízes reais.'
    elif delta == 0:
        raiz = -b / (2 * a)
        return f'A equação possui uma rais real: {raiz}'
    else:
        raiz1 = (-b + sqrt(delta)) / (2 * a)
        raiz2 = (-b + sqrt(delta)) / (2 * a)
        return f'A equação possui duas raízes reais: {raiz1} - {raiz2}'


def main():
    n1 = float(input('Digite o valor de a: '))
    if n1 != 0:
        n2 = float(input('Digite o valor de b: '))
        n3 = float(input('Digite o valor de c: '))
        
        resultado = calculo_raizes_equacao_segundo_grau(n1, n2, n3)
        print(resultado)
    else:
        print('A equação não é o segundo grau')
        
        
if __name__ == '__main__':
    main()
    