# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.


def media_aritmetica(n1, n2):
    m = float(n1 + n2) / 2
    if m < 0:
        return '⚠️ Digite um valor válido ⚠️'
    elif m > 10:
        return '⚠️ Digite um valor válido ⚠️'
    elif not m != 10:
        return f'Média -> {m:.1f}\n🥳👏🏽 APROVADO COM HONRAS 👏🏽🥳'
    elif m >= 7:
        return f'Média -> {m:.1f}\n🥳👏🏽 APROVADO 🥳👏🏽'
    return f'Média -> {m:.1f}\n⚠️☠️ REPROVADO ☠️⚠️'


def main():
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))
    media = media_aritmetica(nota_1, nota_2)
    
    print(f'\n{media}')

    
if __name__ == '__main__':
    main()
