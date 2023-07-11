# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o
# valor seja inválido e continue pedindo até que o usuário informe um valor válido


def pedir_nota():
    nota = float(input('Digite uma nota entre 0 e 10: '))
    return nota


def validar_nota(validacao_nota):
    while validacao_nota < 0 or validacao_nota > 10:
        print('Valor inválido')
        validacao_nota = pedir_nota()
    print(f'Valor válido: {validacao_nota}')
    return validacao_nota


def main():
    pedindo_nota = pedir_nota()
    validar_nota(pedindo_nota)
    
    
if __name__ == '__main__':
    main()
    
# forma mais "básica" de fazer este programa
# while True:
#     n = float(input('Número: '))
#     if 0 <= n <= 10:
#         print('Valor válido.')
#         break
#     else:
#         print('Valor inválido.')


# valida_nota()
