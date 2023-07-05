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


genero = input('digite o gênero: ')
verifica_genero = verifica_genero(genero)

print(f'{verifica_genero}')
