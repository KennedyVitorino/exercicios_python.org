# 7. Faça um Programa que calcule a área de um quadrado, em seguida
# mostre o dobro desta área para o usuário.


def calcular_area_quadrado(lado):
    area = (lado ** 2) * 2
    return area


lado_quadrado = float(input('Lado do quadrado: '))
area_quadrado = calcular_area_quadrado(lado_quadrado)

print(f'A área do quadrado é {area_quadrado:.1f}')
