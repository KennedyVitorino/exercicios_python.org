# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine
# se a mesma é uma data válida
from datetime import datetime


def validar_data_datetime(data_1):
    try:
        data_objeto = datetime.strptime(data_1, '%d/%m/%Y')
        if data_objeto.year >= 1:
            if data_objeto <= datetime.now():
                return True
    except ValueError as e:
        print(f'Error: {e}')
    
    return False


def main():
    data_verificar = input('Digite a data no formato dd/mm/aaaa: ')
    validar_data = validar_data_datetime(data_verificar)
    
    if validar_data:
        print('A data é válida.')
    else:
        print('A data é inválida.')


if __name__ == '__main__':
    main()
