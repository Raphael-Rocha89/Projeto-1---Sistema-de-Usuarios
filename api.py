from fastapi import FastAPI
from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str
    idade: int
    email: str
    
app = FastAPI()

@app.get("/")
def inicio():
    return {"mensagem": "API funcionando!"}

@app.get("/usuarios")
def listar_usuarios():
    import sqlite3
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    
    usuarios = []
    
    for usuario in cursor.fetchall():
        usuarios.append({
            "id": usuario[0],
            "nome": usuario[1],
            "idade": usuario[2],
            "email": usuario[3]
        })
    conexao.close()
    return {"usuarios": usuarios}

@app.post("/usuarios")
def cadastrar_usuario(usuario: Usuario):
    import sqlite3
    import uuid
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    
    id_usuario = str(uuid.uuid4())
    
    cursor.execute("""
        INSERT INTO usuarios (id, nome, idade, email)
        VALUES (?, ?, ?, ?)
    """, (id_usuario, usuario.nome, usuario.idade, usuario.email))
    
    conexao.commit()
    conexao.close()
    
    resultado = {
        "id": id_usuario,
        "nome": usuario.nome,
        "idade": usuario.idade,
        "email": usuario.email
    }
    
    return {"mensagem": "Usuário cadastrado com sucesso!", "usuario": resultado}