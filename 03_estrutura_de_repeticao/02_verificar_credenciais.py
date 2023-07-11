# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
# ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


def validar_credencial():
    while True:
        nome_usuario = input('Digite seu nome: ')
        senha_usuario = int(input('Digite sua senha: '))
        if senha_usuario != nome_usuario:
            print('Credênciais válidas!')
            break
        else:
            print('Erro a senha nao pode ser igual ao nome de usuário.')


validar_credencial()


# ----------------------------------------------------------------------------------------


def pedir_credenciais():
    nome_usuario = input('Digite seu nome: ')
    senha_usuario = int(input('Digite sua senha: '))
    return nome_usuario, senha_usuario


def validar_exibir_credenciais(nome_usuario, senha_usuario):
    while senha_usuario == nome_usuario:
        print('Senha inválida. Tente novamente')
        nome_usuario, senha_usuario = pedir_credenciais()
    print('Credênciais válidas!')


def main():
    nome, senha = pedir_credenciais()
    validar_exibir_credenciais(nome, senha)


if __name__ == '__main__':
    main()
