# 13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado
# ao segundo número. Não utilize a função de potência da linguagem.

def potenciacao_for(b, e):
    r = 1
    for _ in range(e):
        r *= b
    return r


# ------------------------------------------------------------------------------------------------------------

def potenciacao_while(b, e):
    r = 1
    c = 0
    while c < e:
        r *= b
        c += 1
    return r


def main():
    base = int(input('Base: '))
    expoente = int(input('Expoente: '))
    potencia = potenciacao_for(base, expoente)
    print(f'A base {base} elevada ao expoente {expoente} é igual a = {potencia}')
    
    base1 = int(input('Base: '))
    expoente1 = int(input('Expoente: '))
    potencia1 = potenciacao_while(base1, expoente1)
    print(f'A base {base1} elevada ao expoente {expoente1} é igual a = {potencia1}')


if __name__ == '__main__':
    main()
    