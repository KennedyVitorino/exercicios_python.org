# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
# critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o
# aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.


def calcular_reajuste_salarial(salario_atual):
    salario_atual = float(salario_atual)
    if salario_atual <= 280:
        aumento_percentual = 20
    elif 280 < salario_atual <= 700:
        aumento_percentual = 15
    elif 70 <= salario_atual <= 1500:
        aumento_percentual = 10
    else:
        aumento_percentual = 5
    
    aumento_salarial = salario_atual * (aumento_percentual / 100)
    salario_novo = salario_atual + aumento_salarial
    
    return aumento_percentual, aumento_salarial, salario_novo


def main():
    salario = float(input('Digite o salário atual do colaborador: R$ '))
    percentual, aumento, novo_salario = calcular_reajuste_salarial(salario)
    
    print(f'\nSalário antes do reajuste: R${salario:.2f}'
          f'\nPercentual de aumento: {percentual:.1f}%'
          f'\nValor do aumento: R$ {aumento:.2f}'
          f'\nNovo salário após aumento: R$ {novo_salario:.2f}')


if __name__ == '__main__':
    main()
