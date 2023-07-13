# 8. Faça um programa que leia 5 números e informe a soma e a média dos números


def media_aritmetica():
    contador = 0
    soma = 0
    while contador < 5:
        numero = float(input(f'Digite a {contador + 1}° nota: '))
        soma += numero
        contador += 1
    return soma / 5
    
    
def main():
    print(f'A média das notas é: {media_aritmetica():.2f}')
    
    
if __name__ == '__main__':
    main()
    