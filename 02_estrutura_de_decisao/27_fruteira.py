# 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg


def calcular_preco_morangos(peso_morangos):
    preco_morangos = 2.50
    if peso_morangos <= 0:
        return 'Digite um peso válido.'
    elif peso_morangos >= 5:
        preco_morangos = 2.10
        preco_morangos *= peso_morangos
    else:
        preco_morangos *= peso_morangos
    return preco_morangos


def calcular_peso_maca(peso_macas):
    preco_macas = 1.80
    if peso_macas <= 0:
        return 'Digite um peso válido'
    elif peso_macas >= 5:
        preco_macas = 1.50
        preco_macas *= peso_macas
    else:
        preco_macas *= peso_macas
    return preco_macas


def tabela_precos():
    print('👇🏽 Tabela de preços abaixo 👇🏽'
          '\nFrutas              Até 5 Kg           Acima de 5 Kg'
          '\nMorango       R$ 2,50 por Kg          R$ 2,20 por Kg'
          '\nMaçã          R$ 1,80 por Kg          R$ 1,50 por Kg')


def main():
    tabela_precos()
    peso_morango = float(input('\nQuantos Kg de 🍓 você vai levar hoje: '))
    peso_maca = float(input('Quantos Kg de 🍎 você vai levar hoje: '))
    preco_mor = calcular_preco_morangos(peso_morango)
    preco_maca = calcular_peso_maca(peso_maca)

    print(f'\nPeso: {peso_morango:.2f}Kg - Preço do morango: R$ {preco_mor:.2f}'
          f'\nPeso {peso_maca:.2f}Kg - Preço da maçã: R$ {preco_maca:.2f}'
          f'\nPreço total das compras: R$ {preco_maca + preco_mor:.2f}'
          f'\n\n🛒 Volte sempre à nossa feirinha. 🛒')
    

if __name__ == '__main__':
    main()
