# 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos
# obedece à tabela abaixo
# Média de Aproveitamento Conceito
# Entre 9.0 e 10.0           A
# Entre 7.5 e 9.0            B
# Entre 6.0 e 7.5            C
# Entre 4.0 e 6.0            D
# Entre 4.0 e zero           E


def calcular_media_aritmetica(n1, n2):
    m = (n1 + n2) / 2
    if 9 <= m <= 10:
        return f'Média: {m:.2f} -> A'
    elif 7.5 <= m <= 9:
        return f'Média: {m:.2f} -> B'
    elif 6.0 <= m <= 7.5:
        return f'Média: {m:.2f} -> C'
    elif 4 <= m <= 6:
        return f'Média: {m:.2f} -> D'
    elif m <= 4 or m == 0:
        return f'Média: {m:.2f} -> E'
    else:
        return 'Média inválida.'


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = calcular_media_aritmetica(nota1, nota2)

print(media)
