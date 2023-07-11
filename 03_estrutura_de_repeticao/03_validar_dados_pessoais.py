# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


def validar_nome(nome_usuario):
    return len(nome_usuario.strip()) > 3


def validar_idade(idade_usuario):
    return 0 <= idade_usuario <= 150


def validar_salario(salario_usuario):
    return salario_usuario > 0


def validar_sexo(sexo_usuario):
    return sexo_usuario.lower() in ['masculino', 'feminino']


def validar_estado_civil(estado_civil_usuario):
    return estado_civil_usuario.lower() in ['solteiro', 'casado', 'viúvo', 'viuvo' 'divorciado',
                                            'solteira', 'casada', 'viúva', 'viuva' 'divorciada']


def main():
    nome = input('Nome: ')
    while not validar_nome(nome):
        print('Nome inválido. O nome deve ter pelo menos 3 letras.')
        nome = input('Digite o nome novamente: ')
    
    idade = int(input('Idade: '))
    while not validar_idade(idade):
        print('Idade inválida. A idade deve ser entre 0 e 150.')
        idade = int(input('Digite a idade novamente: '))
    
    salario = float(input('Salário: R$ '))
    while not validar_salario(salario):
        print('Valor inválido. O salário deve ser maior que 0.')
    
    sexo = input('Sexo: ')
    while not validar_sexo(sexo):
        print('Sexo inválido. O sexo deve ser -> M - Masculino / F - Feminino.')
        sexo = input('Digite o sexo novamente: ')
    
    estado_civil = input('Estado civil: ')
    while not validar_estado_civil(estado_civil):
        print('Estado civil inválido. O estado civil deve ser\n'
              'S - Solteiro / C - Casado / V - Viúvo / D - Divorciado.')
        
    print(f'\nNome: {nome.capitalize()}'
          f'\nIdade: {idade}'
          f'\nSalário: {salario:.2f}'
          f'\nSexo: {sexo.capitalize()}'
          f'\nEstado civil: {estado_civil.capitalize()}')


if __name__ == '__main__':
    main()
