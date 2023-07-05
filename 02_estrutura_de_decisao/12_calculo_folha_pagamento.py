# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
# são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3%
# para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
# (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
# descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade
# de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
# dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00


def calcular_salario_bruto(preco_hora, horas_mensais):
    return preco_hora * horas_mensais


def calcular_desconto_ir(salario):
    if salario < 900:
        return 0
    elif salario <= 1500:
        return salario * 0.05
    elif salario <= 2500:
        return salario * 0.1
    else:
        return salario * 0.2


def calcular_desconto_sindicato(salario):
    return salario * 0.03


def calcular_desconto_inss(salario):
    return salario * 0.1


def calcular_desconto_fgts(salario):
    return salario * 0.11


def calcular_total_desconto(ir, inss, sindicato):
    return ir + inss + sindicato


def calcular_salario_final(salario, total_descontos):
    return salario - total_descontos


valor_hora = float(input('Digite quanto vale sua hora de trabalho: R$ '))
horas_trabalhadas = float(input('Horas trabalhadas este mês: '))

salario_bruto = calcular_salario_bruto(valor_hora, horas_trabalhadas)
desconto_ir = calcular_desconto_ir(salario_bruto)
desconto_inss = calcular_desconto_inss(salario_bruto)
desconto_sindicato = calcular_desconto_sindicato(salario_bruto)
fgts = calcular_desconto_fgts(salario_bruto)
desconto_total = calcular_total_desconto(desconto_ir, desconto_inss, desconto_sindicato)
salario_liquido = calcular_salario_final(salario_bruto, desconto_total)

print(f'Salário bruto: R$ {salario_bruto:.2f}'
      f'\n(-) sindicato R$ {desconto_sindicato:.2f}'
      f'\n(-) IR ({desconto_ir / salario_bruto * 100}%): R$ {desconto_ir:.2f}'
      f'\n(-) INSS (10%): R$ {desconto_inss:.2f}'
      f'\nFGTS (11%): R$ {fgts:.2f}'
      f'\nTotal de descontos: R$ {desconto_total:.2f}'
      f'\nSalário liquidoo: R$ {salario_liquido:.2f}')

