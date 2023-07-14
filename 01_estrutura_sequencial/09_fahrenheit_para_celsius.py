# 9. Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).


def fahrenheit_para_celsius(f):
    c = 5 * ((f - 32) / 9)
    return c


def main():
    fahrenheit = float(input('Temperatura em Fahrenheit: '))
    convertida_para_celsius = fahrenheit_para_celsius(fahrenheit)
    
    print(f'Graus Celsius -> {convertida_para_celsius:.2f}º')


if __name__ == '__main__':
    main()
