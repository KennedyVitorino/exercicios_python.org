# 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a
# quantidade de centenas, dezenas e unidades do mesmo.


def separar_centenas_dezenas_unidades(num):
    if num >= 1000:
        print('Número inválido. Digite um número menor que 1000')
    
    unidade = num % 10
    num = num // 10
    dezena = num % 10
    num = num // 10
    centena = num
    
    if centena > 0:
        if centena == 1:
            print(centena, 'centena', end=' ')
        else:
            print(centena, 'centenas', end=' ')
            
    if dezena > 0:
        if dezena == 1:
            print(dezena, 'dezena e', end=' ')
        else:
            print(dezena, 'dezenas e', end=' ')
            
    if unidade > 0:
        if unidade == 1:
            print(unidade, 'unidade', end=' ')
        else:
            print(unidade, 'unidades', end=' ')
          
            
# numeros para teste
# n = [326 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

def main():
    numero = int(input('Digite um número para verificar: '))
    separar_centenas_dezenas_unidades(numero)
    
    print(numero)
    
    
if __name__ == '__main__':
    main()
    