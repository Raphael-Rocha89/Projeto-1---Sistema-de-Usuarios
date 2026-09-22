#SISTEMA DE USUÁRIOS.
Usuarios = []
def cadastrar_usuarios():
    print("CADASTRAR USUÁRIO")
    print("Insira as informações necessárias para cadastrar o usuário")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("Email: ")
    Usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
    print("Usuário cadastrado com sucesso!")
    Usuarios.append(Usuario)
    
def listar_usuarios():
    if not Usuarios:
        print("Não existem usuários cadastrados")
        return
    
    print("Usuários Cadastrados", len(Usuarios))
    for Usuario in Usuarios:
        print (Usuario["nome"], Usuario["idade"], Usuario["email"])
            
def pesquisar_usuarios():
    if not Usuarios:
        print("Nenhum usuário foi cadastrado!")
        return
    pesq_n = input("Pesquisar por: ")
    encontrado = False
    for Usuario in Usuarios:
        if pesq_n.strip().lower() == Usuario["nome"].strip().lower():
            print("Usuário(s) encontrado(s)!")
            print(Usuario["nome"], Usuario["idade"], Usuario["email"])
            encontrado = True
    if not encontrado:
        print("Usuário não encontrado")

def editar_usuarios():
    if not Usuarios:
        print("Não há usuários cadastrados.")
        return
    pesq_n = input("Pesquisar por: ")
    encontrado = False
    for Usuario in Usuarios:
        if pesq_n.strip().lower() == Usuario["nome"].strip().lower():
            print("Usuário(s) encontrado(s)!")
            print(Usuario["nome"], Usuario["idade"], Usuario["email"])
            encontrado = True
            print("Insira as novas informações")
            novo_nome = input("Digite o novo nome: ")
            novo_idade = int(input("Digite a nova idade: "))
            novo_email = input("Digite o novo email: ")
            Usuario["nome"] = novo_nome
            Usuario["idade"] = novo_idade
            Usuario["email"] = novo_email
            print("Alteração realizada com sucesso")
            break
    if not encontrado:
        print("Usuário não encontrado")
        
def excluir_usuarios():
    if not Usuarios:
        print("Nenhum usuário cadastrado")
        return
    pesq_n = input("Pesquisar por: ")
    encontrado = False
    for Usuario in Usuarios:
        if pesq_n.strip().lower() == Usuario["nome"].strip().lower():
            print("Usuário(s) encontrado(s)!")
            print(Usuario["nome"], Usuario["idade"], Usuario["email"])
            encontrado = True
            print("Deseja Realmente excluir o usuário?")
            print("Insira: SIM - para confirmar")
            print("Insira: NAO - para cancelar")
            excluir = input("Insira alguma das opções acima: ").strip().lower()
            if excluir == "sim":
                print("O usuário", Usuario["nome"], "será excluído")
                Usuarios.remove(Usuario)
                print("Exclusão concluída")
                break
            elif excluir== "nao":
                print("Exclusão cancelada!")
                print("Retornando ao menu")
                return
    if not encontrado:
        print("Usuário não encontrado")
        
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
        cadastrar_usuarios()
    elif opc == 2:
        listar_usuarios()
    elif opc == 3:
        pesquisar_usuarios()
    elif opc == 4:
        editar_usuarios()
    elif opc == 5:
        excluir_usuarios()