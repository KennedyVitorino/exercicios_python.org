# 5. Faça um Programa que converta metros para centímetros


def converter_metros_para_centimetros(m):
    c = m * 100
    return c


def main():
    metros = float(input('Metros à converter: '))
    centimetros = converter_metros_para_centimetros(metros)
    
    print(f'{metros:.1f} metros convertidos para centímetros é -> {centimetros:.1f}cm')


if __name__ == '__main__':
    main()
