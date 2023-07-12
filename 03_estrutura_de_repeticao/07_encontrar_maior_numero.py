# 7. Faça um programa que leia 5 números e informe o maior número.


def encontrar_maior_numero():
    contador = 1
    maior_numero = float(input('Digite o número 1: '))
    while contador < 5:
        num = float(input(f'Digite o número {contador + 1}: '))
        if num > maior_numero:
            maior_numero = num
        contador += 1
    return maior_numero


def main():
    maior = encontrar_maior_numero()
    print(maior)
    

if __name__ == '__main__':
    main()
    