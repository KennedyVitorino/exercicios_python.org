# 20. Faça um Programa para leitura de três notas parciais de um aluno.O programa deve
# calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva
# média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.


def media_aluno(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if not 0 <= media <= 10:
        return 'Digite um valor válido.'
    elif 7 <= media < 10:
        return f'Aprovado. Média: {media:.1f}'
    elif media == 10:
        return f'Aprovado com distinção. Média: {media:.1f}'
    elif media < 7:
        return f'Reprovado. Média: {media:.1f}'
    return media
    
    
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media_geral = media_aluno(nota1, nota2, nota3)

print(media_geral)
