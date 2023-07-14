# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.


def ordenar_numeros(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        maior = num1
        if num2 >= num3:
            segundo_maior = num2
            menor = num3
        else:
            segundo_maior = num3
            menor = num2
    elif num2 >= num1 and num2 >= num3:
        maior = num2
        if num1 >= num3:
            segundo_maior = num1
            menor = num3
        else:
            segundo_maior = num3
            menor = num1
    else:
        maior = num3
        if num1 >= num2:
            segundo_maior = num1
            menor = num2
        else:
            segundo_maior = num2
            menor = num1
    
    numeros_ordem_decrescente = [maior, segundo_maior, menor]
    return numeros_ordem_decrescente


def main():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    numeros_ordenados = ordenar_numeros(n1, n2, n3)
    ordem_decrescente = f'Ordem decrescente: {", ".join(map(str, numeros_ordenados))}'
    
    print(ordem_decrescente)


if __name__ == '__main__':
    main()
