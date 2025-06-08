import sqlite3

def conectar():
    return sqlite3.connect("dados.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(""" 
         CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT  UNIQUE NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            tipo TEXT,
            valor REAL,
            categoria TEXT,
            descricao TEXT,
            data TEXT,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
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

def registrar_usuario(nome, email, senha):
    conn = None
    try:
       conn = conectar()
       cursor = conn.cursor()
       cursor.execute("INSERT INTO usuarios(nome, email, senha) VALUES (?, ?, ?)",
                   (nome, email, senha))
       conn.commit()    
       conn.close()
       return True
    except Exception as e:
       print("Erro ao registar usuário:", e)
       return False
    finally:
        if conn:
            conn.close()
    
def autenticar_usuario(email, senha):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        resultado = cursor.fetchone()
        conn.close()
        return resultado
        

def salvar_transacao(usuario_id, tipo, valor, categoria, descricao, data):
    conn = sqlite3.connect("dados.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transacoes (usuario_id, tipo, valor, categoria, descricao, data) VALUES (?, ?, ?, ?, ?, ?)",
        (usuario_id, tipo, valor, categoria, descricao, data))
    conn.commit()
    conn.close()
    