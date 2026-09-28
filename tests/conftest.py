import sqlite3
import pytest  # type: ignore[reportMissingImports]

@pytest.fixture
def conexao():
    conexao = sqlite3.connect(":memory:")
    cursor = conexao.cursor()
    cursor.execute("""create table if not exists usuarios (
        id text primary key,
        nome text not null,
        idade integer not null,
        email text not null
    )""")
    conexao.commit()
    return conexao
