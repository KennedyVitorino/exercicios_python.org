# 22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais
# número ele é divisível.


def eh_primo(num):
	divisor = 2
	while divisor * divisor <= num:
		if num % divisor == 0:
			divisores = [str(divisor) for divisor in range(2, num) if num % divisor == 0]
			print(f'{num} não é primo. Seus divisores são: {" ,".join(divisores)}')
			return False
		divisor += 1
	return True


def main():
	numero = int(input('Digite um número inteiro: '))
	if eh_primo(numero):
		print(f'{numero} é primo.')


if __name__ == '__main__':
	main()
