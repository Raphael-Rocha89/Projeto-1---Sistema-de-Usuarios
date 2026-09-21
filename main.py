#SISTEMA DE USUÁRIOS.
Usuarios = []

while True:
    print("1 - Cadastrar Usuário")
    print("2 - Listar Usuário")
    print("3 - Pesquisar Usuário")
    print("4 - Editar Usuário")
    print("5 - Excluir Usuário")
    print("6 - Sair")

    opc = int(input("Escolha uma opção: "))

    if opc == 6:
        print("Saindo")
        break
    elif opc >= 7 or opc <= 0:
        print("Valor inválido")
        continue

    if opc == 1:
        print("CADASTRAR USUÁRIO")
        print("Insira as informações necessárias para cadastrar o usuário")
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        email = input("Email: ")
        Usuario = {
            "nome": nome,
            "idade": idade,
            "email": email
        }
        print("Usuário cadastrado com sucesso!")
        Usuarios.append(Usuario)
    elif opc == 2:
        if not Usuarios:
            print("Não existem usuários cadastrados")
            continue
        else:
            print("Usuários Cadastrados", len(Usuarios))
            for Usuario in Usuarios:
                print (Usuario["nome"], Usuario["idade"], Usuario["email"])
    elif opc == 3:
        if not Usuarios:
            print("Nenhum usuário foi cadastrado!")
            continue
        pesq_n = (input("Pesquisar por: "))
        encontrado = False
        for Usuario in Usuarios:
            if pesq_n.strip().lower() == Usuario["nome"].strip().lower():
                print("Usuário(s) encontrado(s)!")
                print(Usuario["nome"], Usuario["idade"], Usuario["email"])
                encontrado = True
                continue
        if not encontrado:
            print("Usuário não encontrado")
            continue
    elif opc == 4:
        print("a")
    elif opc == 5:
        print("a")