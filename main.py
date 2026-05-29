import sqlite3


def buscar_usuario(nome):
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()

    query = f"SELECT * FROM usuarios WHERE nome = '{nome}'"

    cursor.execute(query)

    return cursor.fetchall()
