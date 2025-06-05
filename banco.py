import sqlite3

def conectar():
    return sqlite3.connect("dados.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT
            valor REAL
            categoria TEXT
            descricao TEXT
            data TEXT
        )
    """)
    conn.commit()
    conn.close()

def inserir_transacao(tipo, valor, categoria, descricao, data):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transacoes (tipo, valor, categoria, descricao, data)
        VALUES (?, ?, ?, ?, ?)
    """, (tipo, valor, categoria, descricao, data))
    conn.commit()
    conn.close()

def listar_transacoes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transacoes ORDER BY data DESC")
    dados = cursor.fetchall()
    conn.close()
    return dados

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
            email TEXT UNIQUE,
            senha TEXT
        )
    """)
    conn.commit()
    conn.close()

def registrar_usuario(nome, email, senha):
    try:
       conn = conectar()
       cursor = conn.cursor()
       cursor.execute("INSERT INTO usuarios(nome, email, senha) VALUES (?, ?, ?)",
                   (nome, email, senha))
       conn.commit()
       conn.close()
       return True
    except:
       return False
    
def autenticar_usuario(email, senha):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        resultado = cursor.fetchall()
        conn.close()
        return resultado #se for sucesso vai retornar (id, nome); se falhar ele vai retornar como none