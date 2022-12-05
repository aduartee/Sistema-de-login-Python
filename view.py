from controller import Cadastro, Controller_login
while True:
    print("========== MENU ==============")
    choice = input('Digite 1 para cadastrar  \n Digite 2 para logar  \n Digite 3 parea sair')

    if choice == 1:
        name = input('Digite seu nome')
        email = input('Digite seu email')
        senha = input('Digite sua senha')
        result = Cadastro.cadastrar(name, email, senha)

        if result == 2:
            print('O nome digita é invalido')

        elif result == 3:
            print('Email não pode ser maior que 40 caracteres')

        elif result == 5:
            print('Email já cadastrado')

    elif choice == 2:
        email = input('Digite seu email')
        senha = input('Digite sua senha')

        result = Controller_login.Login(email, senha)

        if not result:
            print('Email e senha invalidos!')


    else:
        break

