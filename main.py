#SISTEMA DE USUÁRIOS.

import uuid
import sqlite3

def buscar_usuario_id (conexao, id_usuario):
    cursor = conexao.cursor()
    cursor.execute("""
               SELECT * FROM usuarios
               WHERE id = ?
    """, (id_usuario,))
    usuarios = cursor.fetchone()
    return usuarios

def buscar_usuario_nome (conexao, nome_usuario):
    cursor = conexao.cursor()
    cursor.execute("""
               SELECT * FROM usuarios
               WHERE nome LIKE ?
    """, (f"%{nome_usuario}%",))
    usuarios = cursor.fetchall()
    return usuarios

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

def cadastrar_usuarios(conexao):
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
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO usuarios (id, nome, idade, email)
        VALUES (?, ?, ?, ?)
    """, (usuario["id"], usuario["nome"], usuario["idade"], usuario["email"]))
    conexao.commit()
    return usuario

def listar_usuarios(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    if not usuarios:
            print("Não existem usuários cadastrados")
            return
    print("Usuários Cadastrados:", len(usuarios))
    print("Id | Nome | Idade | Email")
    for usuario in usuarios:
        print (usuario [0], "|", usuario [1], "|", usuario [2], "|", usuario [3])
    
    
def localizar_usuario(conexao):
    cursor = conexao.cursor()
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
        cursor.execute("SELECT * FROM usuarios WHERE nome LIKE ?", (f"%{pesq_n}%",))
        usuarios = cursor.fetchall()
        
        if not usuarios:
            return None
        return usuarios
    
    elif selecionar_pesq == 2:
        pesq_id = input("Insira seu ID completo: ")
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (pesq_id,))
        usuario = cursor.fetchone()
        
        if not usuario:
            return None
        return usuario

    
def editar_usuarios(conexao):
    resultado = localizar_usuario(conexao)
    if not resultado:
        print("Usuário não encontrado ou não há nenhum usuário cadastrado.")
        return None
    if isinstance(resultado, list):
        if len(resultado) > 1:
            print("Foram encontrados vários usuários:")
            print("Id | Nome | Idade | Email")
            for usuario in resultado:
                print(usuario[0], "|", usuario[1], "|", usuario[2], "|", usuario[3])
            id_usuario = input("Insira o ID completo do usuário que deseja editar: ").strip()
            usuario = buscar_usuario_id(conexao, id_usuario)
            if not usuario:
                print("Usuário não encontrado.")
                return None
        else:
            id_usuario = resultado[0]
    else:
        usuario = resultado
        
    print("Usuário(s) encontrado(s)!")
    print(usuario)
    print("Insira as novas informações")
    novo_nome = solicitar_nome()
    novo_idade = solicitar_idade()
    novo_email = solicitar_email()

    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE usuarios
        SET nome = ?, idade = ?, email = ?
        WHERE id = ?
    """, (novo_nome, novo_idade, novo_email, usuario[0]))
    conexao.commit()
    return True
            
def excluir_usuarios(conexao):
    id_usuario = input("Insira seu ID completo: ").strip()
    usuario = buscar_usuario_id(conexao, id_usuario)
    if not usuario:
        print("Usuário não encontrado ou não há nenhum usuário cadastrado.")
        return None

    print("Usuário encontrado!")
    print(usuario)

    print("Deseja Realmente excluir o usuário?")
    print("Insira: SIM - para confirmar")
    print("Insira: NAO - para cancelar")
    while True:
        excluir = input("Insira alguma das opções acima: ").strip().lower()
        if excluir == "sim":
            print("O usuário", usuario[1], "será excluído")
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
            conexao.commit()
            return True
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
        print("Saindo")
        break

    if opc == 1:
        usuario_criado = cadastrar_usuarios(conexao)
        if usuario_criado:
            print("Usuário cadastrado com sucesso!")
        else:
            print("Ocorreu um erro no cadastro")
            
    elif opc == 2:
        listar_usuarios(conexao)
        
    elif opc == 3:
        usuario_encontrado = localizar_usuario(conexao)
        if usuario_encontrado:
            print("Usuário encontrado!")
            print(usuario_encontrado)
        else:
            print("Usuário não encontrado ou não há nenhum usuário cadastrado")
    
    elif opc == 4:
        usuario_editado = editar_usuarios(conexao)
        if usuario_editado:
            print("Usuário editado com sucesso!")
        else:
            print("Usuário não encontrado ou edição cancelada.")
    
    elif opc == 5:
        usuario_excluido = excluir_usuarios(conexao)
        if usuario_excluido:
            print("Usuário excluído com sucesso!")
        else:
            print("Usuário não encontrado ou exclusão cancelada.")