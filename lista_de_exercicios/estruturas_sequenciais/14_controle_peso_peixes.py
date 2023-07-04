# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
# o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
# de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por
# quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e
# calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na  variável multa
# o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.


def calcular_excesso_multa(peso):
    excesso = 0
    multa = 0
    if peso > 50:
        excesso = peso_peixes - 50
        multa = excesso * 4
    return excesso, multa


def mostrar_resultados(peso, excesso, multa):
    if excesso > 0:
        print(f'O peso foi de -> {peso:.2f}Kg')
        print(f'Houve um excesso de peso. O excesso foi de {excesso:.2f}kg')
        print(f'A multa a ser paga é de R$ {multa:.2f}.')
    else:
        print('Não houve excesso de peso. Nenhuma multa será aplicada')
        
        
peso_peixes = float(input('Peso dos peixes: '))
excesso_peso, valor_multa = calcular_excesso_multa(peso_peixes)
mostrar_resultados(peso_peixes, excesso_peso, valor_multa)
