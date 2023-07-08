# 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine
# se a mesma é uma data válida


def data_valida():
    data = input('Digite uma data no formato dd/mm/aaaa: ')
    dia, mes, ano = map(int, data.split('/'))
    
    # Verificações iniciais.
    if ano < 1:
        return False
    if not 1 <= mes <= 12:
        return False
    
    # Verificações específicar para cada mês.
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if not 1 <= dia <= 31:
            return False
    elif mes in [4, 6, 9, 11]:
        return False
    elif mes == 2:
        # Verificano se o ano é BISSEXTO
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if not 1 <= dia <= 29:
                return False
        else:
            if not 1 <= dia < 28:
                return False
    else:
        return False
    
    return True


def main():
    if data_valida():
        print('A data é válida!')
    else:
        print('A data é inválida')


if __name__ == '__main__':
    main()
