# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de
# um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando
# este link (em minutos).


def tempo_download(tamanho_arquivo, vel_internet):
    velocidade_mbs = (tamanho_arquivo * 8) / vel_internet  # conversão de Mbps para MB/s
    download_segundos = tamanho_arquivo / velocidade_mbs
    download_minutos = download_segundos / 60
    return download_minutos

    
def main():
    tam_arquivo = float(input('Tamanho do arquivo para download: '))
    velocidade_internet = float(input('Velocidade da internet: '))
    
    download = tempo_download(tam_arquivo, velocidade_internet)
    print(f'O tempo médio de download é: {download:.2f} minutos.')
    
    
if __name__ == '__main__':
    main()
    