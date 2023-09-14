import re
lista_usuarios = {
    'JLucaz': {'nome': 'João', 'senha': '12345', 'data_aniversario': '27/07/2004', 'dados': {'cep': '06040-470', 'numero_telefone': '11-95471-5099', 'email': 'joaolucasyudi@gmail.com', 'endereco': {'rua': 'Lázaro Suave', 'rua_numero': '283'}}},
    'Lucazy': {'nome': 'Lucas', 'senha': '0000', 'data_aniversario': '01/09/2003', 'dados': {'cep': '06040-470', 'numero_telefone': '11-95471-5099', 'email': 'joaolucasyudi@gmail.com', 'endereco': {'rua': 'Lázaro Suave', 'rua_numero': '283'}}}
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
def validar_cep(cep):
    return re.match(r'^\d{5}-\d{3}$', cep)
def validar_telefone(telefone):
    return re.match(r'^\d{2}-\d{5}-\d{4}$', telefone)
def validar_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
def validar_rua(rua):
    return not re.match(r'\d', rua)
def validar_rua_numero(numero):
    return re.match(r'\d', numero)
def cadastrar_dados(login, nome, lista):
    lista[login].update({'dados': {}})
    print(f"{nome}, precisamos coletar alguns dados!")
    while True:
        cep = input("Digite seu cep: ")
        if validar_cep(cep):
            lista[login]['dados']['cep'] = cep
            break
        else:
            print("Digite o cep no formato (00000-000)")
    while True:
        numero_telefone = input("Digite seu número de telefone 00-00000-0000: ")
        if validar_telefone(numero_telefone):
            lista[login]['dados']['telefone'] = numero_telefone
            break
        else:
            print("Digite o telefone no formato (00)00000-0000")
    while True:
        email = input("Digite seu e-mail: ")
        if validar_email(email):
            lista[login]['dados']['email'] = email
            break
        else:
            print("Digite o email no formato (...@...)")

    print("Agora vamos para o endereço do local que quer otimizar!")
    lista[login]['dados']['endereco'] = {}
    while True:
        rua = input("Digite sua rua (apenas o nome): ")
        if validar_rua(rua):
            lista[login]['dados']['endereco']['rua'] = rua
            break
        else:
            print("Digite o endereço corretamente!")
    while True:
        rua_numero = input("Digite o número de sua residência: ")
        if validar_rua_numero(rua_numero):
            lista[login]['dados']['endereco']['numero_rua'] = rua_numero
            break
        else:
            print("Digite apenas números!")
    print(f"""
    Dados cadastrados!
    cep - {cep}
    número de telefone - {numero_telefone}
    email - {email}
    endereço - Rua {rua}, {rua_numero}
    """)
    main(nome, login)
def main(nome, login):
    menu = 0
    print(f"Bem vindo {nome}")
    while True:
        print("""
            ------------------------
                    MENU
            ------------------------
                1 - Orçamento
                2 - Cadastrar dados energéticos
                3 - Sobre nós
                4 - Sair 
        """)

        try:
            menu = int(input())
            if not isinstance(menu, int):
                raise ValueError
            elif menu <= 0 or menu >= 5:
                print("Digite um número correspondente!")
                continue
            elif menu == 1:
                print("Opção 1")
            elif menu == 2:
                if 'dados' in lista_usuarios[login]:
                    print("Você já cadastrou seus dados!")
                else:
                    cadastrar_dados(login, nome, lista_usuarios)
            else:
                break
        except ValueError:
            print("Digite apenas números!")
            continue
def validacao():
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
                        main(lista_usuarios[login]['nome'], login)
                    elif login not in lista_usuarios:
                        print("Digite o usuário corretamente!")
                    elif not lista_usuarios[login]['senha'] == senha:
                        print("Digite a senha corretamente!")

                case _:
                    print("Opção inválida!")
        except ValueError:
            print("Digite apenas números!")

validacao()