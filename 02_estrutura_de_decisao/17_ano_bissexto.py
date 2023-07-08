# 17. aça um Programa que peça um número correspondente a um determinado ano e em seguida
# informe se este ano é ou não bissexto.


def verificar_ano_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False


def main():
    eh_bissexto = int(input('Digite o ano: '))
    
    if verificar_ano_bissexto(eh_bissexto):
        print(f'O ano {eh_bissexto} é bissexto.')
    else:
        print(f'O ano {eh_bissexto} não é bissexto')
        
    
if __name__ == '__main__':
    main()
    