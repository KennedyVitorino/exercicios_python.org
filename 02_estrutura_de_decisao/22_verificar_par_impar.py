# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica:
# utilize o operador módulo (resto da divisão).


def verificar_par_impar(numero):
    if not numero % 2 == 0:
        return 'Número Ímpar'
    else:
        return 'Número par'
    
    
num = int(input('Digite um número: '))
verificar_par_impar = verificar_par_impar(num)

print(verificar_par_impar)
