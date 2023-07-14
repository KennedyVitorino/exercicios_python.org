# Faça um Programa que pergunte em que turno você estuda. Peça para digitar
# M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
# "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


def verificar_turno_estudo(turno_estudo):
    turno_estudo = turno_estudo.strip().lower()
    if turno_estudo == 'm':
        return 'Bom dia!'
    elif turno_estudo == 'v':
        return 'Boa tarde!'
    elif turno_estudo == 'n':
        return 'Boa noite!'
    else:
        return 'Digite um valor válido.'
    

def main():
    turno = input('Em qual turno voce estuda?\n[M]atutino, [V]espertino ou [N]Noturno: ')
    verificar_turno = verificar_turno_estudo(turno)
    
    print(f'\n{verificar_turno}')


if __name__ == '__main__':
    main()
