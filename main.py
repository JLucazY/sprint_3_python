import re

ista_usuarios = {
    'user01': {'nome': 'João', 'login': 'JLucaz', 'senha': '12345', 'data_aniversario': '27/07/2004'},
    'user02': {'nomw': 'Lucas', 'login': 'Luquinhas01', 'senha': '0000', 'data_aniversario': '01/09/2003'}
}

escolha = int(input("1 - Criar novo usuário\n2 - Log In"))

match escolha:
    case 1:
        try:
            if re.search()
            nome = input("Digite seu nome: ")
            nome_usuario = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")
            data_aniversario = input("Digite sua data de aniversário: ")