# 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
# 'Telefonou para a vítima?'
# 'Esteve no local do crime?'
# 'Mora perto da vítima?'
# 'Devia para a vítima?'
# 'Já trabalhou com a vítima?'
# O programa deve no final emitir uma classificação sobre a
# participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
# deve ser classificada como 'Suspeita', entre 3 e 4 como "Cúmplice" e 5 como 'Assassino'.
# Caso contrário, ele será classificado como "Inocente".


def perguntas_respostas():
    contador_sim = 0
    print('Responda as perguntas abaixo com "sim" ou "não".')
    
    resposta = input('Telefonou para a vítima?')
    if resposta.lower() == 'sim':
        contador_sim += 1
        
    resposta = input('Esteve no local do crime?')
    if resposta.lower() == 'sim':
        contador_sim += 1
    
    resposta = input('Mora perto da vítima?')
    if resposta.lower() == 'sim':
        contador_sim += 1
    
    resposta = input('Devia para a vítima?')
    if resposta.lower() == 'sim':
        contador_sim += 1
    
    resposta = input('Já trabalhou com a vítima?')
    if resposta.lower() == 'sim':
        contador_sim += 1
    
    return contador_sim
   

def classificar_jogador(contador_sim):
    if contador_sim == 5:
        classificacao = 'Assassino'
    elif contador_sim == 3 or contador_sim == 4:
        classificacao = 'Cúmplice'
    elif contador_sim == 2:
        classificacao = 'Suspeito'
    else:
        classificacao = 'inocente'
        
    return classificacao


def main():
    respostas_sim = perguntas_respostas()
    classificacao_jogador = classificar_jogador(respostas_sim)
    print(f'Classificação do jogador --> {classificacao_jogador}')
    
    
if __name__ == '__main__':
    main()
