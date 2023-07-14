# 2. Faça um Programa que peça um número e então mostre a mensagem O
# número informado foi [número].

def exibir_numero(n):
    print(f'O número informado foi -> [{n}]')


def main():
    numero = int(input('Número: '))
    exibir_numero(numero)



if __name__ == '__main__':
    main()