# 11. Altere o programa anterior para mostrar no final a soma dos números.


def somar_inteiros_gerados_while(n1, n2):
    soma = 0
    if n1 > n2:
        n1, n2 = n2, n1
    num = n1
    while num <= n2:
        print(num)
        soma += num
        num += 1
    print('Soma:', soma)


# ------------------------------------------------------------------------------------------------------------


def somar_inteiros_gerados_for(n1, n2):
    soma = 0
    if n1 > n2:
        n1, n2 = n2, n1
    for num in range(n1, n2 + 1):
        print(num)
        soma += num
    print('Soma:', soma)
    
    
def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    somar_inteiros_gerados_while(n1, n2)
    
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    somar_inteiros_gerados_for(num1, num2)


if __name__ == '__main__':
    main()
