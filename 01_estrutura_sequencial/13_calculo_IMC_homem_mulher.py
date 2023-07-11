# Tendo como dado de entrada a altura [h] de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7


def calcular_imc_homem(a):
    imc = (72.7 * a) - 58
    return imc


def calcular_imc_mulher(a):
    imc = (62.1 * a) - 44.7
    return imc


altura = float(input('Informe sua altura: '))
imc_homem = calcular_imc_homem(altura)
imc_mulher = calcular_imc_mulher(altura)

print(f'O peso ideal para o homem que mede {altura:.2f} é -> {imc_homem:.2f}Kg')
print(f'O peso ideal para a mulher que pede {altura:.2f} é -> {imc_mulher:.2f}Kg')
