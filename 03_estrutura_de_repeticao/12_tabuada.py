# 12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada.
# A saída deve ser conforme o exemplo abaixo:

def tabuada_while(n):
    if 0 <= n <= 10:
        c = 1
        while c <= 10:
            r = n * c
            print(f'{n} x {c} = {r}')
            c += 1
    else:
        print('Digite um número entre 0 e 10.')

    
# ------------------------------------------------------------------------------------------------------------


def tabuada_for(n):
    if 0 <= n <= 10:
        for c in range(10):
            c += 1
            r = n * c
            print(f'{n} x {c} = {r}')
    else:
        print('Digite um número entre 0 e 10.')


def main():
    num = int(input('numero: '))
    tabuada_while(num)
    
    num2 = int(input('Número: '))
    tabuada_for(num2)
    
    
if __name__ == '__main__':
    main()

