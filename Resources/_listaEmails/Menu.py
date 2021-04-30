from Resources._login.loginA import login


def menu():
    dados = []
    while True:
        menu = str(
            input('''Bem vindo ao pegador de presentes Habbo.
    1 - Registrar e-mail
    2 - Listar e-mails
    3 - Iniciar automação
    4 - Sair
    '''))
        if menu == '1':
            arquivo = open('emailList.txt', 'a')
            email = str(input('E-mail: ')).strip()
            arquivo.write(f'E-mail: {email}\n')
            senha = str(input('Senha: ')).strip()
            arquivo.write(f'Senha: {senha}\n')
            dados.append([email, senha])
            arquivo.close()

        elif menu == '2':
            email = []
            senha = []
            Arquivo = []
            arquivo = open('emailList.txt', 'r')
            arquivoRead = arquivo.read()
            Arquivo.append(arquivoRead.split('\n'))

            j = 1
            i = 0
            while i <= (len(Arquivo[0]) - 1):
                print(Arquivo[0][i], end='\n')
                email.append(Arquivo[0][i])
                i += 2

            while j <= len(Arquivo[0]):
                senha.append(Arquivo[0][j])
                j += 2

            arquivo.close()

        elif menu == '3':
            email = []
            senha = []
            Arquivo = []
            arquivo = open(r'C:\Users\lucas\Downloads\emailList.txt',
                           'r')  #Arquivo txt com email e senha
            #por linha
            arquivoRead = arquivo.read()
            Arquivo.append(arquivoRead.split('\n'))

            j = 1
            i = 0
            while i <= (len(Arquivo[0]) - 1):
                email.append(Arquivo[0][i])
                i += 2

            while j <= len(Arquivo[0]):
                senha.append(Arquivo[0][j])
                j += 2
            arquivo.close()
            # Mudar email

            login(email, senha)

            break

        elif menu == '4':
            break
