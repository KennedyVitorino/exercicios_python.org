# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


def calcular_area_circulo(r):
    a = 3.14159 * (r ** 2)
    return a


def main():
    raio = float(input('Raio: '))
    area = calcular_area_circulo(raio)
    
    print(f'A área do círculo é: {area:.1f}')


if __name__ == '__main__':
    main()
