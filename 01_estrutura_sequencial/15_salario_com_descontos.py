# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


def calcular_salario_bruto(valor_hora, horas_trabalhadas):
    return valor_hora * horas_trabalhadas


def calcular_imposto_renda(salario):
    return salario * 0.11


def calcular_inss(salario):
    return salario * 0.08


def calcular_sindicato(salario):
    return salario * 0.05


def calcular_salario_liquido(salario, desconto_ir, desconto_inss, desconto_sindicato):
    return salario - desconto_ir - desconto_inss - desconto_sindicato


def main():
    preco_hora = float(input('Quanto você recebe por hora: R$ '))
    carga_horaria = int(input('Quantas horas você trabalhou esse mês: '))
    
    salario_bruto = calcular_salario_bruto(preco_hora, carga_horaria)
    imposto_renda = calcular_imposto_renda(salario_bruto)
    inss = calcular_inss(salario_bruto)
    sindicato = calcular_sindicato(salario_bruto)
    salario_liquido = calcular_salario_liquido(salario_bruto, imposto_renda, inss, sindicato)
    
    print('\n+' + '-' * 40 + '+')
    print(f'Salário Bruto: R$ {salario_bruto:.2f}')
    print(f'Valor desconto do Imposto de Renda R$ {imposto_renda:.2f}')
    print(f'Valor desconto do INSS: R$ {inss:.2f}')
    print(f'Valor desconto do Sindicato R$ {sindicato:.2f}')
    print(f'Salário liquido: R$ {salario_liquido:.2f}')
    print('+' + '-' * 40 + '+')


if __name__ == '__main__':
    main()
