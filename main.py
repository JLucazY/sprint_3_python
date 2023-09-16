#imports
import re
import random

#Dicionários e tuples que simulam o banco de dados da empresa
lista_usuarios = {
    'JLucaz': {'nome': 'João', 'senha': '12345', 'data_aniversario': '27/07/2004', 'dados': {'numero_telefone': '11-95471-5099', 'email': 'joaolucasyudi@gmail.com', 'cep': '06040-470', 'endereco': {'rua': 'Lázaro Suave', 'rua_numero': '283'}, 'tamanho_estabelecimento': 300, 'conta_luz': 5000}},
    'Lucazy': {'nome': 'Lucas', 'senha': '0000', 'data_aniversario': '01/09/2003', 'dados': {'numero_telefone': '11-95471-5099', 'email': 'joaolucasyudi@gmail.com', 'cep': '06040-470', 'endereco': {'rua': 'Lázaro Suave', 'rua_numero': '283'}, 'tamanho_estabelecimento': 200, 'conta_luz': 3000}}
}
horarios_disponiveis = ('11:00', '9:30', '14:00', '17:30')
tarifa_luz = (0.96, 0.88, 0.8, 0.76)



#Função que valida o nome do usuário
def validar_nome(nome):
    return re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome)
#Função que valida o ano de nascimento seguindo a realiadade dos dias do ano
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
#Função que valida senha, max 5 números
def validar_senha(senha):
    return re.match(r'^\d{1,5}$', senha)
#Função que valida login, mín 6 e max 12 carac
def validar_login(login):
    return re.match(r'^[a-zA-Z0-9]{6,12}$', login)
#Função que valida o CEP (00000-000)
def validar_cep(cep):
    return re.match(r'^\d{5}-\d{3}$', cep)
#Função que valida o num de telefone
def validar_telefone(telefone):
    return re.match(r'^\d{2}-\d{5}-\d{4}$', telefone)
#Função que valida o email
def validar_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
#Função que valida a rua
def validar_rua(rua):
    return not re.match(r'\d', rua)
#Função que aceita apenas números
def validar_numero(numero):
    return re.match(r'^[0-9]+$', numero)
#Função que escolhe randomicamente um elemento da tuple
def escolha_random(lista):
    return random.choice(lista)

tarifa = escolha_random(tarifa_luz)
horario_visita = escolha_random(horarios_disponiveis)


#Função de entrada que simula uma tela de login e criação de usuários
def validacao():
    escolha_login_criar_usuario = 0
    while escolha_login_criar_usuario != 1 or escolha_login_criar_usuario != 2:
        try:
            escolha_login_criar_usuario = int(input("1 - Criar novo usuário\n2 - Log In\n3 - Sair"))
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
                        nome = input("Digite seu nome: ").capitalize()
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
                    if not login in lista_usuarios:
                        print("Usuário não encontrado!")
                    else:
                        senha = input("Digite a sua senha: ")
                        if login in lista_usuarios and lista_usuarios[login]['senha'] == senha:
                            print("Sucesso!")
                            main(lista_usuarios[login]['nome'], login)
                        elif not lista_usuarios[login]['senha'] == senha:
                            print("Digite a senha corretamente!")

                case 3:
                    print("Obrigado por usar o programa!")
                    exit()
                case _:
                    print("Opção inválida!")
        except ValueError:
            print("Digite apenas números!")

#Função do menu principalmente
def main(nome, login):
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
                print("Número fora do range usado!")

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
                sair(nome, login)
            else:
                print("Digite um número correspondente!")
        except ValueError:
            print("Digite apenas números!")

#Função de serviços que a empresa presta
def servicos(nome, login):
    while True:
        try:
            print("""Lista de serviços:
                        1 - Previsão de economia
                        2 - inspeção técnica no local
                        3 - Instalação de painéis solares
                        4 - Voltar
                        """)
            tipo_servico = int(input())
            if not isinstance(tipo_servico, int):
                raise ValueError

            elif tipo_servico <= 0 or tipo_servico >= 6:
                print("Número fora do range usado!")
            else:

                match tipo_servico:

                    case 1:

                        while True:
                            print(f"Dados cadastrados:\nConta de luz: R$ {lista_usuarios[login]['dados']['conta_luz']}\nTarifa energética por Kwh no seu estado: {tarifa}R$/kWh")
                            print("Calculando...")

                            conta_luz = (lista_usuarios[login]['dados']['conta_luz'] * tarifa)

                            print(f"{nome}, baseado em cálculos aritméticos, a conta de luz que o senhor(a) pagará após a eficiência energética é de {conta_luz:.2f}!\n")
                            break

                    case 2:
                        print("Digite o dia para a realização da inspeção!")
                        while True:
                            try:
                                dia = int(input())
                                if not isinstance(dia, int):
                                    raise ValueError

                                elif dia <= 31 and dia >= 1:

                                    print(f"Agendado senhor(a) {nome}, o dia para a realização da inspeção será {dia} ás {horario_visita}!\n")
                                    break

                                else:
                                    print("Dia inválido!")

                            except ValueError:
                                print("Digite apenas números!")

                    case 3:
                        while True:
                            print(f"{nome}, quantos metros quadrados dispoviveis você tem para a instalação dos paíneis em {lista_usuarios[login]['dados']['tamanho_estabelecimento']} m²")
                            try:
                                m2 = float(input())
                                if not isinstance(m2, float):
                                    raise ValueError

                                elif m2 > lista_usuarios[login]['dados']['tamanho_estabelecimento'] or m2 <= 0:
                                    print("Digite um tamanho válido!")

                                else:
                                    preco_painel_solar = m2 * 100
                                    print(f"{nome}, o orçamento de instalação será de R${preco_painel_solar:.2f}\n")
                                    break
                            except ValueError:
                                print("Digite apenas números")

                    case 4:
                        main(nome, login)

        except ValueError:
            print("Digite uma opção correspondente!")

def cadastrar_dados(login, nome):
    lista_usuarios[login].update({'dados': {}})
    print(f"{nome}, precisamos coletar alguns dados!")
    while True:
        numero_telefone = input("Digite seu número de telefone 00-00000-0000: ")
        if validar_telefone(numero_telefone):
            lista_usuarios[login]['dados']['numero_telefone'] = numero_telefone
            break
        else:
            print("Digite o telefone no formato 00-00000-0000")

    while True:
        email = input("Digite seu e-mail: ")
        if validar_email(email):
            lista_usuarios[login]['dados']['email'] = email
            break
        else:
            print("Digite o email no formato (***@***.com)")

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
        rua = input("Digite sua rua (apenas o nome): Rua ")
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
        try:
            tamanho_estab_metros = float(input("Digite o tamanho do local (m2): "))
            if isinstance(tamanho_estab_metros, float):
                lista_usuarios[login]['dados']['tamanho_estabelecimento'] = tamanho_estab_metros
                break
            else:
                raise ValueError
        except ValueError:
            print("Digite apenas números")
    while True:
        try:
            conta_luz = float(input("Digite a sua conta de luz: R$ "))
            if isinstance(conta_luz, float):
                lista_usuarios[login]['dados']['conta_luz'] = conta_luz
                break
            else:
                raise ValueError
        except ValueError:
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

#Função que simula uma aba de 'sobre nós'
def sobre_nos(nome, login):
    while True:
        print("""
                   Buscamos oferecer soluções customizadas que atendam suas demandas. 
                   Trazendo-lhe alternativas que visam uma maior economia, eficiência e segurança energética, 
                   estimulando a sustentabilidade e a competitividade para que você tenha um destaque ainda maior no mercado.

                   Soluções usadas por nós:
                       1 - Uso de fontes de energia renováveis
                       2 - Monitoramento e gerenciamento de energia
                       3 - Melhorias na eficiência dos equipamentos
                           """)
        print("1 - voltar")
        try:
            decisao = int(input())
            if not isinstance(decisao, int):
                raise ValueError
            elif decisao <= 0 or decisao >= 2:
                print("Número fora do range usado!")
            else:
                main(nome, login)
        except ValueError:
            print("Digite apenas números!")

def sair(nome, login):
    if 'dados' in lista_usuarios[login]:

        print(f"""
            Resumo da operação
            
            Dados registrados:
            nome - {nome}
            login - {login}
            senha - {lista_usuarios[login]['senha']}
            data aniversário - {lista_usuarios[login]['data_aniversario']}
            número de telefone - {lista_usuarios[login]['dados']['numero_telefone']}
            email - {lista_usuarios[login]['dados']['email']}
            cep - {lista_usuarios[login]['dados']['cep']}
            endereço - Rua {lista_usuarios[login]['dados']['endereco']['rua']}, {lista_usuarios[login]['dados']['endereco']['rua'] }
            tamanho do estabelecimento - {lista_usuarios[login]['dados']['tamanho_estabelecimento']}
            conta de luz - {lista_usuarios[login]['dados']['conta_luz']}
            
          
    """)

    else:
        print(f"""
           Resumo da operação
    
           Dados registrados:
           nome - {nome}
           login - {login}
           senha - {lista_usuarios[login]['senha']}
           data aniversário - {lista_usuarios[login]['data_aniversario']}
           número de telefone - não registrado
           email - não registrado
           cep - não registrado
           endereço - não registrado
           tamanho do estabelecimento - não registrado
           conta de luz - não registrado
           """)

    while True:
        try:
            print("1 - nova operação\n2 - Encerrar")
            continuar = int(input())
            if continuar <= 0 or continuar >=3:
                print("Número fora do range usado!")
            elif not isinstance(continuar, int):
                raise ValueError
            elif continuar == 1:
                validacao()
            elif continuar == 2:
                print("Obrigado por usar o programa\nEncerrando...")
                exit()
        except ValueError:
            print("Digite um número correspondente!")


validacao()