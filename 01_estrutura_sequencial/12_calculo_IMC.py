# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
# calcule o peso ideal, usando a seguinte fórmula:
# (72.7*altura) - 58


def calcular_imc(a):
    imc = (72.7 * a) - 58
    return imc


def main():
    altura = float(input('Digite sua altura: '))
    calculo_imc = calcular_imc(altura)
    
    print(f'O peso ideal para o homem que mede {altura:.2f} é {calculo_imc:.2f}Kg')


if __name__ == '__main__':
    main()
