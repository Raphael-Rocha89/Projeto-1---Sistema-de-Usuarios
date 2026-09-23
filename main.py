#SISTEMA DE USUÁRIOS.
#Correções pendentes: Resumindo
#Seu programa já está estruturalmente correto: cadastro, listagem, pesquisa, edição, exclusão e menu estão separados em funções, o que é uma boa organização.
#Os problemas mais importantes no código original são:
#❌ if "@" and "." in email → validação incorreta do e-mail.
#❌ Nome pode conter números apesar da mensagem dizer que não pode.
#❌ Edição pode gerar ValueError ao receber uma idade não numérica.
#❌ Edição não verifica limite da idade.
#❌ Edição não valida nome e e-mail.
#⚠️ Pesquisa é apenas por nome completo.
#✅ Cadastro, listagem, pesquisa e exclusão estão, em geral, funcionando.
#✅ O menu principal está funcionando corretamente.
#Um próximo passo interessante seria evitar repetir as validações de nome, idade e e-mail, criando funções como validar_nome(), validar_idade() e validar_email(). Isso deixaria o código consideravelmente mais limpo e profissional.

Usuarios = []
def cadastrar_usuarios(usuarios):
    print("CADASTRAR USUÁRIO")
    print("Insira as informações necessárias para cadastrar o usuário")
    while True:
        nome = input("Nome: ").strip()
        if nome and all(caractere.isalpha() for caractere in nome):
            break
        print("O nome é um campo obrigatório, não é permitido o uso de números.")
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0 or idade > 120:
                print("Sua idade ultrapassa os limites.")
                continue
            break
        except ValueError:
            print("Insira informações válidas")  
    while True: 
        email = input("Email: ").strip()
        if "@" in email and "." in email:
            break
        print("Email inválido, este é um campo obrigatório.")

    Usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
    usuarios.append(Usuario)
    return Usuario
    
def listar_usuarios(usuarios):
    if not usuarios:
        print("Não existem usuários cadastrados")
        return
    
    print("Usuários Cadastrados", len(usuarios))
    for Usuario in usuarios:
        print (Usuario["nome"], Usuario["idade"], Usuario["email"])
            
def pesquisar_usuarios(usuarios):
    if not usuarios:
        return None
    
    pesq_n = input("Pesquisar por: ")
    
    for Usuario in usuarios:
        if pesq_n.strip().lower() == Usuario["nome"].strip().lower():
            return Usuario

    return None



def editar_usuarios(usuarios):
    if not usuarios:
        return None
    pesq_n = input("Pesquisar por: ")
    for Usuario in usuarios:
        if pesq_n.strip().lower() == Usuario["nome"].strip().lower():
            print("Usuário(s) encontrado(s)!")
            print(Usuario["nome"], Usuario["idade"], Usuario["email"])
            print("Insira as novas informações")
            novo_nome = input("Digite o novo nome: ")
            novo_idade = int(input("Digite a nova idade: "))
            novo_email = input("Digite o novo email: ")
            Usuario["nome"] = novo_nome
            Usuario["idade"] = novo_idade
            Usuario["email"] = novo_email
            return Usuario

    return None
        
def excluir_usuarios(usuarios):
    if not usuarios:
        return None
    pesq_n = input("Pesquisar por: ")
    for Usuario in usuarios:
        if pesq_n.strip().lower() == Usuario["nome"].strip().lower():
            print("Usuário(s) encontrado(s)!")
            print(Usuario["nome"], Usuario["idade"], Usuario["email"])
            print("Deseja Realmente excluir o usuário?")
            print("Insira: SIM - para confirmar")
            print("Insira: NAO - para cancelar")
            excluir = input("Insira alguma das opções acima: ").strip().lower()
            if excluir == "sim":
                print("O usuário", Usuario["nome"], "será excluído")
                usuarios.remove(Usuario)
                return Usuario
            elif excluir== "nao":
                print("Exclusão cancelada!")
                print("Retornando ao menu")
                return None
    return None
        
while True:
    print("1 - Cadastrar Usuário")
    print("2 - Listar Usuário")
    print("3 - Pesquisar Usuário")
    print("4 - Editar Usuário")
    print("5 - Excluir Usuário")
    print("6 - Sair")

    while True:
        try:
            opc = int(input("Escolha uma opção: "))
            if opc not in range(1,7):
                print("Valor inválido")
                continue
            break
        except ValueError:
            print("Use números para selecionar uma opção.")
        
    if opc == 6:
        print("Saindo")
        break

    if opc == 1:
        usuario_criado = cadastrar_usuarios(Usuarios)
        if usuario_criado:
            print("Usuário cadastrado com sucesso!")
        else:
            print("Ocorreu um erro no cadastro")
    elif opc == 2:
        listar_usuarios(Usuarios)
    elif opc == 3:
        usuario_encontrado = pesquisar_usuarios(Usuarios)
        if usuario_encontrado:
            print("Usuário encontrado!")
            print(usuario_encontrado["nome"],
                  usuario_encontrado["idade"],
                  usuario_encontrado["email"])
        else:
            print("Usuário não encontrado")
    elif opc == 4:
        usuario_editado = editar_usuarios(Usuarios)
        if usuario_editado:
            print("Usuário editado com sucesso!")
        else:
            print("Usuário não encotrado ou edição cancelada. ")
    elif opc == 5:
        usuario_excluido = excluir_usuarios(Usuarios)
        if usuario_excluido:
            print("Usuário excluído com sucesso!")
        else:
            print("Usuário não encontrado ou exclusão cancelada.")