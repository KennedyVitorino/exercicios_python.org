# [Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em
# graus Fahrenheit. F = (C * 9/5) + 32


def celsius_para_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f


def main():
    temperatura = float(input('Temperatura: '))
    convertida_para_fahren = celsius_para_fahrenheit(temperatura)
    
    print(f'Fahrenheit -> {convertida_para_fahren:.2f}º')


if __name__ == '__main__':
    main()
