# 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de
# carne da promoção, porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre
# o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
# pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e
# quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


def tabela_precos():
    print('🍖🔪🥩HIPERMERCADO TABAJARA - PROMOÇÃO DE CARNES🥩🔪🍖'
          '\n👇🏽 Tabela de preços abaixo 👇🏽'
          '\n                    Até 5 Kg        Acima de 5 Kg'
          '\nFile Duplo    R$ 39,90 por Kg       R$ 44,80 por Kg'
          '\nAlcatra       R$ 49,90 por Kg       R$ 55,80 por Kg'
          '\nPicanha       R$ 63,90 por Kg       R$ 77,80 por Kg')
    

def calcular_preco_total(tipo_carne, quantidade):
    preco_file_duplo_ate_5kg = 39.90
    preco_alcatra_ate_5kg = 49.90
    preco_picanha_ate_5kg = 63.90
    preco_file_duplo_adimca_5kg = 44.80
    preco_alcatra_acima_5kg = 55.80
    preco_picanha_acima_5kg = 77.80
    
    if tipo_carne == 'File duplo'.lower() or tipo_carne == 'Filé duplo'.lower():
        if quantidade <= 5:
            preco_total = preco_file_duplo_ate_5kg * quantidade
        else:
            preco_total = preco_file_duplo_adimca_5kg * quantidade
    elif tipo_carne == 'Alcatra'.lower():
        if quantidade <= 5:
            preco_total = preco_alcatra_ate_5kg * quantidade
        else:
            preco_total = preco_alcatra_acima_5kg * quantidade
    elif tipo_carne == 'Picanha'.lower():
        if quantidade <= 5:
            preco_total = preco_picanha_ate_5kg * quantidade
        else:
            preco_total = preco_picanha_acima_5kg * quantidade
    else:
        return 'Tipo de carne inválido'
    return preco_total


def calcular_deconto(preco_total, cartao_tabajara):
    preco_total = preco_total
    if cartao_tabajara == 's':
        desconto = 0.05 * preco_total
    else:
        desconto = 0
    return desconto


def gerar_nota_fiscal(tipo_carne, quantidade, preco_total, cartao_tabajara):
    desconto = calcular_deconto(preco_total, cartao_tabajara)
    total_pagar = preco_total - desconto
    
    print('\n----- CUPOM FISCAL -----'
          f'\nTipo de cane: {tipo_carne}'
          f'\nQuantidade: {quantidade:.2f}Kg'
          f'\nPreço sem desconto: R$ {preco_total:.2f}')
    
    if cartao_tabajara.lower() == 's':
        print('Tipo de pagamento: Cartão tabajara'
              f'\nDesconto: R$ {desconto:.2f}')
    else:
        print('Tipo de pagamento: Outro'
              '\nDesconto: Nenhum')
    print(f'Valor total a pagar R$ {total_pagar:.2f}')
    

def main():
    tabela_precos()
    
    carne = input('\nInforme o tipo de carne: (Filé duplo / Alcatra / Picanha): ')
    quantidade_carne = float(input('Informe quantos Kg deseja levar: '))
    credito_tabajara = input('A compra será feita com o Cartão Tabajara? (S / N): ')
    
    preco_total_carne = calcular_preco_total(carne, quantidade_carne)
    gerar_nota_fiscal(carne, quantidade_carne, preco_total_carne, credito_tabajara)
    

if __name__ == '__main__':
    main()
