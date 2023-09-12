import re

lista_usuarios = {
    'JLucaz': {'nome': 'João', 'senha': '12345', 'data_aniversario': '27/07/2004'},
    'Lucazy': {'nome': 'Lucas', 'senha': '0000', 'data_aniversario': '01/09/2003'}
}

def validar_nome(nome):
    return re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome)

def validar_ano_nascimento(data):
    if not re.match(r'\d{2}/\d{2}/\d{4}', data):
        return False

    dia, mes, ano = map(int, data.split('/'))
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if not (1 <= mes <= 12):
        return False
    if not (1 <= dia <= dias_por_mes[mes]):
        return False
    return True

def validar_senha(senha):
    return re.match(r'\d{1,5}', senha)
def validar_login(login):
    return re.match(r'^[a-zA-Z0-9]{6,12}$', login)


while True:
    try:
        escolha_login_criar_usuario = int(input("1 - Criar novo usuário\n2 - Log In\n"))
        match escolha_login_criar_usuario:
            case 1:
                while True:
                    login = input("Digite o usuário de login: ")
                    if login not in lista_usuarios.keys() and validar_login(login):
                        lista_usuarios.update({f'{login}': {}})
                        break
                    elif not validar_login(login):
                        print("Nome de log in precisa ter no mínimo 6 e no máximo 12 caracteres")
                    else:
                        print(f"{login} já está cadastrados no nosso banco de dados!")

                while True:
                    nome = input("Digite seu nome: ")
                    if validar_nome(nome):
                        lista_usuarios[login]['nome'] = nome
                        break
                    else:
                        print("Nome inválido! Use apenas letras e espaços.")

                while True:
                    senha = input("Digite sua senha (1-5 dígitos): ")
                    if validar_senha(senha):
                        lista_usuarios[login]['senha'] = senha
                        break
                    else:
                        print("Senha inválida! use entre 1 e 5 dígitos.")

                while True:
                    data_aniversario = input("Digite sua data de aniversário: ")
                    if validar_ano_nascimento(data_aniversario):
                        lista_usuarios[login]['data_aniversario'] = data_aniversario
                        break
                    else:
                        print("Formato inválido! digite a senha nesse paramêtro(00/00/0000)")
                print(f"Sucesso ao cadastrar usuário {login}!")
            case 2:
                login = input("Digite o usuário de login: ")
                senha = input("Digite a sua senha: ")
                if login in lista_usuarios and lista_usuarios[login]['senha'] == senha:
                    print("Sucesso!")
                    break
            case _:
                print("Opção inválida!")
    except ValueError:
        print("Digite apenas números!")
