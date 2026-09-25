#SISTEMA DE USUÁRIOS.

import json
import uuid
import sqlite3

id_usuario = input("Digite o ID: ")
def buscar_usuario_id (conexao, id_usuario):
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("""
               SELECT * FROM usuarios
               WHERE id = ?
    """, (id_usuario,))
    conexao.commit()
    usuarios = cursor.fetchone()
    for usuarios in usuarios:
        print(usuarios)

conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios (
                   id TEXT PRIMARY KEY,
                   nome TEXT NOT NULL,
                   idade INTEGER NOT NULL,
                   email TEXT NOT NULL)
               """)
conexao.commit()
cursor.execute("""
    INSERT INTO usuarios (id, nome, idade, email)
    VALUES (?, ?, ?, ?)
""", ("idteste6", "Luana", 18, "luana@email.com"))
conexao.commit()
buscar_usuario_id(conexao, id_usuario)
conexao.close()



def carregar_usuarios():
    cursor = conexao.cursor()
    try:
        with open("usuarios.exemplo.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo JSON não encontrado")
        return []
    except json.JSONDecodeError:
        print("Existem alterações inválidas em usuarios.exemplo.json")
        return []
        
def salvar_usuarios(usuarios):
    with open("usuarios.exemplo.json", "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4)
        
usuarios = carregar_usuarios()

def solicitar_nome():
    while True:
        nome = input("Nome: ").strip()
        if nome and all(
            caractere.isalpha() or caractere.isspace()
            for caractere in nome
            ):
            return nome
        print("O nome é um campo obrigatório, não é permitido o uso de números.")
    
def solicitar_idade():
    while True:
        try:
            idade = int(input("Idade: "))
            if idade <= 0 or idade > 120:
                print("Sua idade ultrapassa os limites.")
                continue
            return idade
        except ValueError:
            print("Insira informações válidas")
            
def solicitar_email():
    while True: 
        email = input("Email: ").strip()
        if "@" in email and "." in email:
            return email
        print("Email inválido, este é um campo obrigatório.")

def cadastrar_usuarios(usuarios):
    print("CADASTRAR USUÁRIO")
    print("Insira as informações necessárias para cadastrar o usuário")
    nome = solicitar_nome()    
    idade = solicitar_idade()
    email = solicitar_email()

    usuario = {
        "id": str(uuid.uuid4()),
        "nome": nome,
        "idade": idade,
        "email": email
    }
    usuarios.append(usuario)
    return usuario
    
def listar_usuarios(usuarios):
    if not usuarios:
        print("Não existem usuários cadastrados")
        return
    
    print("Usuários Cadastrados:", len(usuarios))
    print("Id | Nome | Idade | Email")
    for usuario in usuarios:
        print (usuario["id"],"|",usuario["nome"],"|", usuario["idade"],"|", usuario["email"])
          
def localizar_usuario(usuarios):
    if not usuarios:
        return None
    print("Escolha um método de pesquisa:")
    print("1 - Pesquisar por nome")
    print("2 - Pesquisar por ID")
    while True:
        try:
            selecionar_pesq = int(input("Selecione alguma das opções: "))
            if selecionar_pesq not in (1,2):
                print("Digite apenas números entre 1 ou 2.")
                continue
            break
            
        except ValueError:
            print("Use apenas os números 1 ou 2 para selecionar um modo de pesquisa.")
            continue
    if selecionar_pesq == 1:
        pesq_n = input("Pesquisar pelo nome: ")
        for usuario in usuarios:
            if pesq_n.strip().lower() in usuario["nome"].strip().lower():
                return usuario
        return None
    elif selecionar_pesq == 2:
        pesq_id = input("Insira seu ID completo: ")
        for usuario in usuarios:
            if pesq_id == str(usuario["id"]):
                return usuario
        return None
    
def editar_usuarios(usuarios):
    usuario = localizar_usuario(usuarios)
    if not usuario:
        return None
    print("Usuário(s) encontrado(s)!")
    print(usuario["nome"], usuario["idade"], usuario["email"])
    print("Insira as novas informações")
    novo_nome = solicitar_nome()
    novo_idade = solicitar_idade()
    novo_email = solicitar_email()
                    
    usuario["nome"] = novo_nome
    usuario["idade"] = novo_idade
    usuario["email"] = novo_email
    return usuario
            
def excluir_usuarios(usuarios):
    usuario = localizar_usuario(usuarios)
    if not usuario:
        return None
    print("Usuário(s) encontrado(s)!")
    print(usuario["nome"], usuario["idade"], usuario["email"], usuario["id"])
    print("Deseja Realmente excluir o usuário?")
    print("Insira: SIM - para confirmar")
    print("Insira: NAO - para cancelar")
    while True:
        excluir = input("Insira alguma das opções acima: ").strip().lower()
        if excluir == "sim":
            print("O usuário", usuario["nome"], "será excluído")
            usuarios.remove(usuario)
            return usuario
        elif excluir== "nao":
            print("Exclusão cancelada!")
            print("Retornando ao menu")
            return None
        print("Use apenas SIM ou NAO para prosseguir.")
        
while True:
    print("-------- Menu -------")
    print("1 - Cadastrar Usuário")
    print("2 - Listar Usuário")
    print("3 - Pesquisar Usuário")
    print("4 - Editar Usuário")
    print("5 - Excluir Usuário")
    print("6 - Sair e salvar")

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
        salvar_usuarios(usuarios)
        print("Saindo")
        break

    if opc == 1:
        usuario_criado = cadastrar_usuarios(usuarios)
        if usuario_criado:
            salvar_usuarios(usuarios)
            print("Usuário cadastrado com sucesso!")
        else:
            print("Ocorreu um erro no cadastro")
    elif opc == 2:
        listar_usuarios(usuarios)
    elif opc == 3:
        usuario_encontrado = localizar_usuario(usuarios)
        if usuario_encontrado:
            print("Usuário encontrado!")
            print(usuario_encontrado["id"],"|", usuario_encontrado["nome"],"|", usuario_encontrado["idade"],"|", usuario_encontrado["email"])
        else:
            print("Usuário não encontrado ou não há nenhum usuário cadastrado")
    elif opc == 4:
        usuario_editado = editar_usuarios(usuarios)
        if usuario_editado:
            salvar_usuarios(usuarios)
            print("Usuário editado com sucesso!")
        else:
            print("Usuário não encontrado ou edição cancelada. ")
    elif opc == 5:
        usuario_excluido = excluir_usuarios(usuarios)
        if usuario_excluido:
            salvar_usuarios(usuarios)
            print("Usuário excluído com sucesso!")
        else:
            print("Usuário não encontrado ou exclusão cancelada.")