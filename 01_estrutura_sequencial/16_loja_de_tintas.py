# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
# é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

def calcular_quantidade_tinta(area):
    litros_tinta = area / 3
    latas_tinta = (litros_tinta // 18) + (litros_tinta % 18 > 0)
    preco = latas_tinta * 80
    
    return latas_tinta, preco
    
    
def main():
    area_pintada = float(input('Metros quadrados da área a ser pintada: '))
    qtd_latas, preco_total = calcular_quantidade_tinta(area_pintada)
    
    print(f'Quantidade de latas e tinta necessárias: {qtd_latas}')
    print(f'Preço total: R$ {preco_total:.2f}')


if __name__ == '__main__':
    main()
