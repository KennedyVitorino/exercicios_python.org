# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a
# letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.


def verifica_genero(g):
    g = g.lower()
    if len(g) == 1 and g.isalpha():
        if g == 'm':
            return 'Gênero [M]asculino'
        elif g == 'f':
            return 'Gênero [F]eminino'
    return 'Gênero Inválido.'


def main():
    genero = input('digite o gênero: ')
    verificar_genero = verifica_genero(genero)
    
    print(f'{verificar_genero}')


if __name__ == '__main__':
    main()
