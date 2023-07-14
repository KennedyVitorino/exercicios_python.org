# 15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

def fibonacci_while(n):
    t1 = 1
    t2 = 1
    c = 0
    while c < n:
        print(t1)
        proximo_termo = t1 + t2
        t1 = t2
        t2 = proximo_termo
        c += 1
    return n


# ------------------------------------------------------------------------------------------------------------


def fibonacci_for(n):
    termo1 = 1
    termo2 = 1
    
    print(f'{termo1}\n{termo2}')
    
    for _ in range(2, n):
        proximo_termo = termo1 + termo2
        print(proximo_termo)
        
        termo1 = termo2
        termo2 = proximo_termo
    return n


def main():
    numero = int(input('Digite o valor d3 N: '))
    fibonacci_while(numero)
    
    numero1 = int(input('Digite o valor de N: '))
    fibonacci_for(numero1)
    

if __name__ == '__main__':
    main()
    