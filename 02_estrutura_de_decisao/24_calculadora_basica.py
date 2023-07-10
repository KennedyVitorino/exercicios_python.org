# 24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação
# ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga
# se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.


def par_impar(n):
    if n % 2 == 0:
        return 'par'
    else:
        return 'ímpar'


def positivo_negativo(n):
    if n > 0:
        return 'positivo 👍'
    else:
        return 'negativo 👎'


def inteiro_decimal(n):
    if n % 1 == 0:
        return 'inteiro'
    else:
        return 'decimal'


def operacoes_basicas(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    elif op == '//':
        return n1 // n2
    elif op == '**':
        return n1 ** n2
    else:
        raise ValueError('Operação inválida.')


def main():
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    operacao = input('Escolha uma operação (+, -, *, /, //, **): ')
    
    resultado = operacoes_basicas(numero1, numero2, operacao)
    
    print(f'Resultado: {resultado:.1f}'
          f'\nParidade: {par_impar(resultado)}'
          f'\nPositividade: {positivo_negativo(resultado)}'
          f'\nTipo: {inteiro_decimal(resultado)}')


if __name__ == '__main__':
    main()
