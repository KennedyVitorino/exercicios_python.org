# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento
# iniciais. Valide a entrada e permita repetir a operação.

def anos_populacao(pop_a, taxa_a, pop_b, taxa_b):
    anos = 0
    while pop_a < pop_b:
        pop_a *= 1 + taxa_a
        pop_b *= 1 + taxa_b
        anos += 1
    return anos

