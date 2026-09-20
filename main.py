#SISTEMA DE USUÁRIOS.
while True:
    print("1 - Cadastrar Usuário")
    print("2 - Listar Usuário")
    print("3 - Pesquisar Usuário")
    print("4 - Editar Usuário")
    print("5 - Excluir Usuário")
    print("6 - Sair")

    opc = int(input("Escolha uma opção: "))
    Usuarios = []
    
    if opc == 6:
        break
    if opc >= 7 or opc <= 0:
        print("Valor inválido")
        break



    if opc == 1:
        print("CADASTRAR USUÁRIO")
        print("Insira as informações necessárias para cadastrar o usuário")
        nome = input("Nome: ")
        idade = int(input("Idade:"))
        email = input("Email: ")
        Usuario = {
            "nome": nome,
            "idade": idade,
            "email": email
        }
        print("Usuário cadastrado com sucesso!")
        Usuarios.append(Usuario)
if opc == 2:

if opc == 3:
    
if opc == 4:
    
if opc == 5: