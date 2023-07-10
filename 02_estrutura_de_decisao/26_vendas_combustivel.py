# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de
# litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser
# pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do
# litro do álcool é R$ 1,90.


def calcular_valor_pago_alcool(litros):
    preco_alcool = 1.90
    if litros < 20:
        valor_pago = litros * (preco_alcool - (preco_alcool * 0.03))
    else:
        valor_pago = litros * (preco_alcool - (preco_alcool * 0.05))
    return valor_pago


def calcular_valor_pago_gasolina(litros):
    preco_gasolina = 2.50
    if litros < 20:
        valor_pago = litros * (preco_gasolina - (preco_gasolina * 0.04))
    else:
        valor_pago = litros * (preco_gasolina - (preco_gasolina * 0.06))
    
    return valor_pago


def msg_volte_sempre():
    print('\nVolte sempre ao nosso posto onde o futuro é agora.')
    

def main():
    print('⛽ POSTO DE GASOLINA DE VOLTA PARA O FUTURO ⛽'
          '\nRecarregue sua jornada com combustível do futuro!')
    tipo_combustivel = input('\n⛽ Informe o tipo de combustível que deseja abastecer'
                             '\n⛽ A - Álcool / G - Gasolina / H - Híbrido: ')
    if tipo_combustivel.lower() in 'agh':
        if tipo_combustivel.lower() == 'h':
            lts_alcool = float(input('Quantos litros de álcool deseja abastecer: '))
            lts_gasolina = float(input('Quantos litros de gasolina deseja abastecer: '))
            alcool_pago = calcular_valor_pago_alcool(lts_alcool)
            gasolina_paga = calcular_valor_pago_gasolina(lts_gasolina)
            
            print(f'\nÁlcool: {lts_alcool} litros. Preço: R$ {alcool_pago:.2f}'
                  f'\nGasolina: {lts_gasolina} litros. Preco: R$ {gasolina_paga:.2f}'
                  f'\nTotal: R$ {alcool_pago + gasolina_paga:.2f}')
            msg_volte_sempre()
        else:
            litros_vendidos = float(input('\n⛽ Informe quantos litros deseja abastecer: '))
            if tipo_combustivel.lower() == 'a':
                alcool_pago = calcular_valor_pago_alcool(litros_vendidos)
                print(f'Álcool {litros_vendidos} litros. Preco: R$ {alcool_pago:.2f}')
            elif tipo_combustivel.lower() == 'g':
                gasolina_paga = calcular_valor_pago_gasolina(litros_vendidos)
                print(f'Gasolina {litros_vendidos}litros. Preço: R$ {gasolina_paga:.2f}')
            msg_volte_sempre()
    else:
        print("Tipo de combustível inválido.")


if __name__ == '__main__':
    main()
