# Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês.


def calculo_salario(valor_hora, horas_trabalho):
    salario_total = valor_hora * horas_trabalho
    return salario_total


def main():
    salario_hora = float(input('Valor recebido por hora trabalhada: R$ '))
    horas_trabalhadas = int(input('Horas trabalhadas esse mês: '))
    salario_final = calculo_salario(salario_hora, horas_trabalhadas)
    
    print(f'Salário final: {salario_final:.2f}')


if __name__ == '__main__':
    main()
