# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


def obter_dia_semaana(d):
    if d == 1:
        return 'Domingo'
    elif d == 2:
        return 'Segunda-Feira'
    elif d == 3:
        return 'Terça-Feira'
    elif d == 4:
        return 'Quarta-Feira'
    elif d == 5:
        return 'Quinta-Feira'
    elif d == 6:
        return 'Sexta-Feira'
    elif dia == 7:
        return 'Sabado'
    else:
        return 'Esse número não corresponde a um dia da semana válido.'
    

def main():
    dia = int(input('Digite\n''1-Domingo, 2-Segunda, 3-Terça, 4-Quarta, 5-Quinta, 6-Sexta e '
                    '7-Sabado: '))
    dia_semaana = obter_dia_semaana(dia)
    
    print(f'Dia da semana escolhido: {dia_semaana}')


if __name__ == '__main__':
    main()
