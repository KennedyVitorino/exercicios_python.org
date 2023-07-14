# 8. Faça um programa que leia 5 números e informe a soma e a média dos números


def media_aritmetica_while(soma):
    contador = 0
    while contador < 5:
        numero = int(input('Digite um número: '))
        soma += numero
        contador += 1
    return soma / 5


# ------------------------------------------------------------------------------------------------------------


def media_aritmetica_for(soma):
    for contador in range(5):
        numero = float(input(f'Digite a {contador + 1}° nota: '))
        soma += numero
    return soma / 5
    
    
def main():
    soma = 0
    media = media_aritmetica_while(soma)
    print(f'A média das notas é: {media:.2f}')

    soma = 0
    media2 = media_aritmetica_for(soma)
    print(f'A média das notas é: {media2:.2f}')


if __name__ == '__main__':
    main()
    