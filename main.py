import re
import random

lista_usuarios = {
    'JLucaz': {'nome': 'João', 'senha': '12345', 'data_aniversario': '27/07/2004', 'dados': {'numero_telefone': '11-95471-5099', 'email': 'joaolucasyudi@gmail.com', 'cep': '06040-470', 'endereco': {'rua': 'Lázaro Suave', 'rua_numero': '283'}, 'tamanho_estabelecimento': 300, 'conta_luz': 5000 }},
    'Lucazy': {'nome': 'Lucas', 'senha': '0000', 'data_aniversario': '01/09/2003', 'dados': {'numero_telefone': '11-95471-5099', 'email': 'joaolucasyudi@gmail.com', 'cep': '06040-470' , 'endereco': {'rua': 'Lázaro Suave', 'rua_numero': '283'}, 'tamanho_estabelecimento': 200, 'conta_luz': 3000}}
}

horarios_disponiveis = ('11:30', '9:00', '14:00', '17:00')
tarifa_luz = (0.96, 0.88, 0.8, 0.76)

def escolha_random(lista):
    return random.choice(lista)
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
def validar_numero(numero):
    return re.match(r'\d', numero)
def horario_random():
    return random.choice(horarios_disponiveis)

def cadastrar_dados(login, nome):
    lista_usuarios[login].update({'dados': {}})
    print(f"{nome}, precisamos coletar alguns dados!")
    while True:
        numero_telefone = input("Digite seu número de telefone 00-00000-0000: ")
        if validar_telefone(numero_telefone):
            lista_usuarios[login]['dados']['telefone'] = numero_telefone
            break
        else:
            print("Digite o telefone no formato (00)00000-0000")
    while True:
        email = input("Digite seu e-mail: ")
        if validar_email(email):
            lista_usuarios[login]['dados']['email'] = email
            break
        else:
            print("Digite o email no formato (...@....com)")
    while True:
        cep = input("Digite seu cep: ")
        if validar_cep(cep):
            lista_usuarios[login]['dados']['cep'] = cep
            break
        else:
            print("Digite o cep no formato (00000-000)")
    print("Agora vamos para o endereço do local que quer otimizar!")
    lista_usuarios[login]['dados']['endereco'] = {}
    while True:
        rua = input("Digite sua rua (apenas o nome): ")
        if validar_rua(rua):
            lista_usuarios[login]['dados']['endereco']['rua'] = rua
            break
        else:
            print("Digite o endereço corretamente!")
    while True:
        rua_numero = input("Digite o número de sua residência: ")
        if validar_numero(rua_numero):
            lista_usuarios[login]['dados']['endereco']['numero_rua'] = rua_numero
            break
        else:
            print("Digite apenas números!")
    while True:
        tamanho_estab_metros = int(input("Digite o tamanho do local (m2): "))
        if validar_numero(tamanho_estab_metros):
            lista_usuarios[login]['dados']['tamanho_estabelecimento'] = tamanho_estab_metros
            break
        else:
            print("Digite apenas números!")
    while True:
        conta_luz = int(input("Digite a sua conta de luz: R$ "))
        if validar_numero(conta_luz):
            lista_usuarios[login]['dados']['conta_luz'] = conta_luz
            break
        else:
            print("Digite apenas números!")

    print(f"""
    Dados cadastrados!
    cep - {cep}
    número de telefone - {numero_telefone}
    email - {email}
    endereço - Rua {rua}, {rua_numero}
    tamanho do estabelecimento - {tamanho_estab_metros}
    conta de energia - {conta_luz}
    """)
    main(nome, login)

def servicos(nome, login):
    print(f"{nome}, agora vamos para o orçamento")
    while True:
        try:
            print("""Lista de serviços:
                            1 - Previsão de economia
                            2 - inspeção técnica no local
                            3 - Instalação de painéis solares
                            4 - Voltar
                            5 - Sair""")
            tipo_servico = int(input())
            if not isinstance(tipo_servico, int):
                raise ValueError
            else:
                break
        except ValueError:
            print("Digite uma opção correspondente!")
    match tipo_servico:
        case 1:
            while True:
                tarifa = escolha_random(tarifa_luz)
                print(f"Senhor(a) {nome}, sua conta de luz atual é de R$ {lista_usuarios[login]['dados']['conta_luz']} e com a tarifa do seu estado sendo {tarifa} RS/kWh\n"
                      f"CALCULANDO...")
                conta_luz = (lista_usuarios[login]['dados']['conta_luz'] * tarifa)
                print(f"{nome}, baseado em cálculos aritméticos, a conta de luz que o senhor(a) pagará após a eficiência energética é de {conta_luz:.2f}!")
                break
        case 2:
            while True:
                print("digite o dia para a realização da inspeção")
                try:
                    dia = int(input())
                    if not type(dia) is int:
                        raise ValueError
                    elif dia <= 31 and dia >= 1:
                        print(f"Agendado senhor(a) {nome}, o dia para a realização da inspeção será {dia} ás {escolha_random(horarios_disponiveis)}!")
                        break
                    else:
                        print("Dia inválido! Digite um dia valido")
                    continue
                except ValueError:
                    print("Digite apenas números!")
                    continue
        case 3:
            while True:
                try:
                    print(f"{nome}, quantos metros quadrados dispoviveis você tem para a instalação dos paíneis em {lista_usuarios[login]['dados']['tamanho_estabelecimento']} m²")
                    m = float(input())
                    if not type(m) is float:
                        raise ValueError
                    elif m > lista_usuarios[login]['dados']['tamanho_estabelecimento'] or m <= 0:
                        print("Digite um tamanho correto!")
                        continue
                    else:
                        preco_painel_solar = m * 100
                        print(f"Senhor(a) {nome}, o orçamento de instalação será de R${preco_painel_solar:.2f}")
                        break
                except ValueError:
                    print("Digite apenas números")
                    continue
        case 4:
            main(nome, login)
        case _:
            exit()

def sobre_nos(nome, login):
    print("""
                   Buscamos oferecer soluções customizadas que atendam suas demandas. 
                   Trazendo-lhe alternativas que visam uma maior economia, eficiência e segurança energética, 
                   estimulando a sustentabilidade e a competitividade para que você tenha um destaque ainda maior no mercado.

                   Soluções usadas por nós:
                       1 - Uso de fontes de energia renováveis
                       2 - Monitoramento e gerenciamento de energia
                       3 - Melhorias na eficiência dos equipamentos
                   """)
    print("(1) Voltar  (2) Sair")
    decisao = int(input())
    match decisao:
        case 1:
            main(nome, login)
        case 2:
            exit()
def main(nome, login):
    menu = 0
    print(f"Bem vindo {nome}")
    while True:
        print("""
            ------------------------
                    MENU
            ------------------------
                1 - Tipos de serviço
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
                if not 'dados' in lista_usuarios[login]:
                    print(f"{nome}, você precisa registrar os dados energéticos primeiro!")
                else:
                    servicos(nome, login)
            elif menu == 2:
                if 'dados' in lista_usuarios[login]:
                    print("Você já cadastrou seus dados!")
                else:
                    cadastrar_dados(login, nome)
            elif menu == 3:
                sobre_nos(nome, login)
            elif menu == 4:
                exit()
            else:
                print("Digite um número correspondente!")
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