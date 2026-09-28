def test_solicitar_idade_completo(monkeypatch):
    from main import solicitar_idade
    entradas = iter(["-5", "abc", "150", "25"])
    substituir_input = lambda _: next(entradas)
    monkeypatch.setattr('builtins.input', substituir_input)
    resultado = solicitar_idade()
    assert resultado == 25
    
def test_solicitar_nome_completo(monkeypatch):
    from main import solicitar_nome
    entradas = iter(["", "123", "Maria"])
    substituir_input = lambda _: next(entradas)
    monkeypatch.setattr('builtins.input', substituir_input)
    resultado = solicitar_nome()
    assert resultado == "Maria"
    
def test_solicitar_email_completo(monkeypatch):
    from main import solicitar_email
    entradas = iter(["", "maria@", "maria.com", "email@correto.com"])
    substituir_input = lambda _: next(entradas)
    monkeypatch.setattr('builtins.input', substituir_input)
    resultado = solicitar_email()
    assert resultado == "email@correto.com"
    
def test_cadastrar_usuarios(conexao, monkeypatch):
    from main import cadastrar_usuarios
    entradas = iter(["Maria", "30", "maria@example.com"])
    substituir_input = lambda _: next(entradas)
    monkeypatch.setattr('builtins.input', substituir_input)
    cadastrar_usuarios(conexao)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ?", ("Maria",))
    resultado = cursor.fetchone()
    assert resultado is not None

def test_buscar_usuario_id(conexao):
    from main import buscar_usuario_id
    cursor = conexao.cursor()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("123", "João", 25, "joao@example.com"))
    conexao.commit()
    resultado = buscar_usuario_id(conexao, "123")
    assert resultado == ("123", "João", 25, "joao@example.com")

def test_buscar_usuario_id_invalido(conexao):
    from main import buscar_usuario_id
    cursor = conexao.cursor()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("123", "João", 25, "joao@example.com"))
    conexao.commit()
    resultado = buscar_usuario_id(conexao, "999")
    assert resultado is None
    
def test_buscar_usuario_nome(conexao):
    from main import buscar_usuario_nome
    cursor = conexao.cursor()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("234", "Maria", 30, "maria@example.com"))
    conexao.commit()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("456", "Joana", 30, "joana@example.com"))
    conexao.commit()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("789", "José", 40, "jose@example.com"))
    conexao.commit()
    resultado = buscar_usuario_nome(conexao, "Ma")
    assert resultado == [("234", "Maria", 30, "maria@example.com")]

def test_buscar_usuario_nome_nao_encontrado(conexao):
    from main import buscar_usuario_nome
    cursor = conexao.cursor()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("234", "Maria", 30, "maria@example.com"))
    conexao.commit()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("456", "Joana", 30, "joana@example.com"))
    conexao.commit()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("789", "José", 40, "jose@example.com"))
    conexao.commit()
    resultado = buscar_usuario_nome(conexao, "pedro")
    assert resultado == []

def test_buscar_usuario_nome_invalido(conexao):
    from main import buscar_usuario_nome
    cursor = conexao.cursor()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("234", "Maria", 30, "maria@example.com"))
    conexao.commit()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("456", "Joana", 30, "joana@example.com"))
    conexao.commit()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("789", "José", 40, "jose@example.com"))
    conexao.commit()
    resultado = buscar_usuario_nome(conexao, "123")
    assert resultado == []

def test_editar_usuarios(conexao, monkeypatch):
    from main import editar_usuarios
    entradas = iter(["2", "333", "Carlos", "20", "Carlos@email.com"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    cursor = conexao.cursor()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("333", "testeid", 1, "teste@email.com"))
    conexao.commit()
    resultado = editar_usuarios(conexao)
    assert resultado is True
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", ("333",))
    resultado = cursor.fetchone()
    assert resultado == ("333", "Carlos", 20, "Carlos@email.com")

def test_editar_usuarios_nome(conexao, monkeypatch):
    from main import editar_usuarios
    entradas = iter(["1", "testenome", "Carlos", "20", "Carlos@email.com"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    cursor = conexao.cursor()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("444", "testenome", 1, "teste@email.com"))
    conexao.commit()
    resultado = editar_usuarios(conexao)
    assert resultado is True
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", ("444",))
    resultado = cursor.fetchone()
    assert resultado == ("444", "Carlos", 20, "Carlos@email.com")

def test_editar_usuarios_nao_encontrado(conexao, monkeypatch):
    from main import editar_usuarios
    entradas = iter(["2", "999"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    cursor = conexao.cursor()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("098", "teste", 1, "teste@email.com"))
    conexao.commit()
    resultado = editar_usuarios(conexao)
    assert resultado is None
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", ("098",))
    resultado = cursor.fetchone()
    assert resultado == (("098", "teste", 1, "teste@email.com"))

def test_excluir_usuarios(conexao, monkeypatch):
    from main import excluir_usuarios
    entradas = iter(["111", "sim"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    cursor = conexao.cursor()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("111", "TesteExcluir", 1, "excluir@email.com"))
    conexao.commit()
    resultado = excluir_usuarios(conexao)
    assert resultado is True
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", ("111",))
    resultado = cursor.fetchone()
    assert resultado is None

def test_excluir_usuarios_nao_encontrado(conexao, monkeypatch):
    from main import excluir_usuarios
    entradas = iter(["999"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    cursor = conexao.cursor()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("222", "TesteExcluir", 1, "excluir@email.com"))
    conexao.commit()
    resultado = excluir_usuarios(conexao)
    assert resultado is None

def test_nao_excluir_usuarios(conexao, monkeypatch):
    from main import excluir_usuarios
    entradas = iter(["222", "nao"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    cursor = conexao.cursor()
    cursor.execute("insert into usuarios (id, nome, idade, email) values (?, ?, ?, ?)", ("222", "TesteExcluir", 1, "excluir@email.com"))
    conexao.commit()
    resultado = excluir_usuarios(conexao)
    assert resultado is None
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", ("222",))
    resultado = cursor.fetchone()
    assert resultado == ("222", "TesteExcluir", 1, "excluir@email.com")
