# 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
# se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
# se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
# Três lados formam um triângulo quando a soma de
# quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;


def verifica_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 'Os valores devem ser maiores que 0.'
    elif a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            return 'Triângulo Equilátero'
        elif a == b or a == c or b == c:
            return 'Triângulo Isósceles'
        else:
            return 'Triângulo Escaleno'
    else:
        return 'Não é possível formar um triângulo.'


def main():
    lado_1 = float(input('Informe o tamanho do primeiro lado: '))
    lado_2 = float(input('Informe o tamanho do segundo lado: '))
    lado_3 = float(input('Informe o tamanho do terceiro lado: '))
    triangulos = verifica_triangulo(lado_1, lado_2, lado_3)
    
    print(triangulos)


if __name__ == '__main__':
    main()
