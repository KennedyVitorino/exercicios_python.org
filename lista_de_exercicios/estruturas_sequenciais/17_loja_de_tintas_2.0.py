# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a
# tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
# que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
# em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
# considere latas cheias.
import math


def calcular_quantidade_tinta_necessaria(area_metros_quadrados):
    qtd_tinta_necessaria = (area_metros_quadrados / 6) * 1.1
    return qtd_tinta_necessaria


def calcular_qtd_latas_tintas(qtd_total_tinta_necessaria):
    quantidade_latas_tinta = math.ceil(qtd_total_tinta_necessaria / 18)
    return quantidade_latas_tinta


def calcular_qtd_galoes(qtd_total_tinta_necessaria):
    quantidade_galoes = math.ceil(qtd_total_tinta_necessaria / 3.6)
    return quantidade_galoes


def calcular_qtd_latas_galoes(qtd_total_tinta_necessaria):
    qtd_latas_tintas = qtd_total_tinta_necessaria // 18
    resto_tinta = qtd_total_tinta_necessaria % 18
    qtd_galoes_tinta = math.ceil(resto_tinta / 3.6)
    return qtd_latas_tintas, qtd_galoes_tinta


area = float(input('Tamanho da área a ser pintada (em metros quadrados): '))

tinta_necessaria = calcular_quantidade_tinta_necessaria(area)
qtd_latas = calcular_qtd_latas_tintas(tinta_necessaria)
qtd_galoes = calcular_qtd_galoes(tinta_necessaria)
qtd_latas_galoes = calcular_qtd_latas_galoes(tinta_necessaria)

preco_lata_tinta = 80
preco_galao_tinta = 25

custo_latas = qtd_latas * preco_lata_tinta
custo_galoes = qtd_galoes * preco_galao_tinta
custo_total = custo_latas + custo_galoes

print('\n+' + '-' * 45 + '+')
print('Situação 1: comprar apenas latas de 18 litros')
print(f'Quantidade de latas: {qtd_latas}')
print(f'Preco total: R$ {custo_latas:.2f}')

print('\nSituação 2: Comprar apeas galões de 3,6 litros')
print(f'Quantidade de galões: {qtd_galoes}')
print(f'Preço total: R$ {custo_galoes:.2f}')

print('\nSituação 3: Misturar latas e galões')
print(f'Quantidade de latas: {qtd_latas}')
print(f'Quantidade de galões: {qtd_galoes}')
print(f'Preço total: R$ {custo_total:.2f}')
print('\n+' + '-' * 45 + '+')
