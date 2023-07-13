# 8. Faça um programa que leia 5 números e informe a soma e a média dos números


def media_aritmetica_while(s):
    c = 0
    while c < 5:
        n = float(input(f'Digite a {c + 1}° nota: '))
        s += n
        c += 1
    return s / 5


# ------------------------------------------------------------------------------------------------------------


def media_aritmetica_for(s):
    for c in range(5):
        n = float(input(f'Digite a {c + 1}° nota: '))
        s += n
    return s / 5
    
    
def main():
    soma = 0
    media = media_aritmetica_while(soma)
    print(f'A média das notas é: {media:.2f}')

    soma = 0
    media2 = media_aritmetica_for(soma)
    print(f'A média das notas é: {media2:.2f}')


if __name__ == '__main__':
    main()
    