# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


def encontra_vogal(v):
    v = v.lower()
    if len(v) == 1 and v.isalpha():
        if v in 'aeiou':
            return 'É vogal'
        else:
            return 'É consoante'
    

letra = input('Digite a letra para verificar: ')
vogal_consoante = encontra_vogal(letra)

print(vogal_consoante)
