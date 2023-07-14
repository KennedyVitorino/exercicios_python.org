# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
# compreendido por eles.


def gerar_intervalo_inteiros_while(n1, n2):
    if n1 > n2:
        n1, n2 = n2, n1
    num = n1
    while num <= n2:
        print(num)
        num += 1

# ------------------------------------------------------------------------------------------------------------


def gerar_intervalo_inteiros_for(n1, n2):
    if n1 > n2:
        n1, n2 = n2, n1
    for num in range(n1, n2 + 1):
        print(num)

    
def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    gerar_intervalo_inteiros_while(n1, n2)
    
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    gerar_intervalo_inteiros_for(num1, num2)
    
    
if __name__ == '__main__':
    main()
    