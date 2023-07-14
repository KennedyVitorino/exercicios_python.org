# 2. Faça um Programa que peça um valor e mostre na tela se o
# valor é positivo ou negativo.


def verifica_positivo_negativo(n):
    if n < 0:
        return 'Negativo'
    elif n > 0:
        return 'Positivo'
    else:
        return 'Neutro'
    
 
def main():
    numero = int(input('Digite o número: '))
    verifica_numero = verifica_positivo_negativo(numero)
    
    print(verifica_numero)


if __name__ == '__main__':
    main()
