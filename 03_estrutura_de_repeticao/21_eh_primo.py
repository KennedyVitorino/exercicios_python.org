# 21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.


def eh_primo(numero):
	for i in range(2, numero):
		if numero % 2 == 0:
			return 'Não é primo!'
	return 'É primo'


def main():
	while True:
		num = int(input('Digite um número: '))
		if num == 0:
			break
		primo = eh_primo(num)
		print(primo)
	print('Programa encerrado.')


if __name__ == '__main__':
	main()
