# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.


def calcular_media(num_notas):
    notas = []
    soma = 0
    
    for i in range(num_notas):
        nota = float(input(f'{i + 1}º nota -> '))
        notas.append(nota)
        soma += nota

    media = soma / len(notas)
    return media


numero_notas = 4
media_notas = calcular_media(numero_notas)
print(f'A média bimetral é: {media_notas:.2f}')
