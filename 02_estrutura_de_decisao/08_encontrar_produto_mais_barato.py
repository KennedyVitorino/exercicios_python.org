# 8. Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


def encontrar_prod_mais_barato(p1, p2, p3):
    if p1 <= p2 <= p3:
        return f'Produto 1 - R$ {p1:.2f}'
    elif p2 <= p1 and p2 <= p3:
        return f'Produto 2 - R$ {p2:.2f}'
    else:
        return f'Produto 3 - R$ {p3:.2f}'


def main():
    preco_prod1 = float(input('Digite o preço do produto 1 -> R$ '))
    preco_prod2 = float(input('Digite o preço do produto 2 -> R$ '))
    preco_prod3 = float(input('Digite o preço do produto 3 -> R$ '))
    produto_mais_barato = encontrar_prod_mais_barato(preco_prod1, preco_prod2, preco_prod3)
    
    print(f'\nO produto mais barato é: {produto_mais_barato}')


if __name__ == '__main__':
    main()
