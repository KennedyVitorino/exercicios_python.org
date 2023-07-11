# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


def pedir_dados():
    nome = input('Nome do usuario: ')
    idade = int(input('Idade: '))
    salario = float(input('Salario: R$ '))
    sexo = input('Sexo: [M/F]')
    estado_civil = input(
        'Estado civil\nS - Solteiro(a) C - Casado(a) V - Viuvo(a) - D - Divorciado(a)')
    return nome, idade, salario, sexo, estado_civil


def main():
    n, i, s, s, e = pedir_dados()
    
    