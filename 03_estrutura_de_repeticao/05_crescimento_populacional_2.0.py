# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de
# crescimento iniciais. Valide a entrada e permita repetir a operação.

def anos_populacao(pop_a, taxa_a, pop_b, taxa_b):
    anos = 0
    while pop_a < pop_b:
        pop_a *= 1 + taxa_a
        pop_b *= 1 + taxa_b
        anos += 1
    return anos


def main():
    while True:
        try:
            populacao_a = int(input('População do país A: '))
            taxa_pop_a = float(input('Taxa de crescimento do país A (em decimal): '))
            populacao_b = int(input('População do país B: '))
            taxa_pop_b = float(input('Taxa de crescimento do país B (em decimal): '))
            
            if populacao_a <= 0 or populacao_b <= 0 or taxa_pop_a <= 0 or taxa_pop_b <= 0 or taxa_pop_b == 0:
                raise ValueError

            anos_crescimento = anos_populacao(populacao_a, taxa_pop_a, populacao_b, taxa_pop_b)
            print(f'Serão necessários {anos_crescimento} para a população do país A ultrapassar ou igualar a '
                  f'população do país B.')
            
            opcao = input('Deseja fornecer novos dados? (s/n)')
            if opcao.lower() != 's':
                break
        except ValueError:
            print('Entrada inválida. Certifique-se de fornecer valores númericos positivos para as '
                  'populações e taxas de crescimento.')
        
    print('Fim do programa.')
    
    
if __name__ == '__main__':
    main()
    