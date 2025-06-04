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

    