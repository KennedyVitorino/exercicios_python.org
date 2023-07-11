# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento
# de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa
# que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a
# população do país B, mantidas as taxas de crescimento.


def calcular_anos_populacao(pop_a, taxa_a, pop_b, taxa_b):
    anos = 0
    while pop_a < pop_b:
        pop_a *= 1 + taxa_a
        pop_b += 1 + taxa_b
        anos += 1
    return anos


def main():
    populacao_a = 80000
    taxa_pop_a = 0.03
    populacao_b = 200000
    taxa_pop_b = 0.015
    
    anos_passados = calcular_anos_populacao(populacao_a, taxa_pop_a, populacao_b, taxa_pop_b)
    
    print(f'Serão necessários {anos_passados} anos para a população do país A ultrapassar ou igualar a '
          f'população do país B.')
    
    
if __name__ == '__main__':
    main()
    